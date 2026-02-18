#!/usr/bin/env python3
"""
Estrattore HTML da file MD e TXT

Analizza i file markdown e testo alla ricerca di:
- Documenti HTML completi (con CSS inline/embedded)
- Blocchi HTML significativi
- Template di documenti amministrativi

I file estratti vengono salvati nella stessa cartella
del file sorgente, mantenendo HTML e CSS insieme.

Uso: poetry run python extract_html.py [directory]
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class HtmlDocument:
    """Rappresenta un documento HTML estratto."""
    content: str
    source_file: str
    source_path: Path  # Path completo del file sorgente
    doc_type: str
    has_css: bool = False
    has_js: bool = False
    css_blocks: list = field(default_factory=list)

    @property
    def length(self) -> int:
        return len(self.content)

    @property
    def is_complete(self) -> bool:
        """Verifica se il documento ha struttura HTML completa."""
        lower = self.content.lower()
        return '<html' in lower and '</html>' in lower

    @property
    def output_dir(self) -> Path:
        """Directory di output (stessa del file sorgente)."""
        return self.source_path.parent


def extract_full_html_documents(content: str, filename: str, filepath: Path) -> list[HtmlDocument]:
    """
    Estrae documenti HTML completi mantenendo CSS e JS insieme.
    """
    documents = []

    # Pattern 1: Documento completo con DOCTYPE
    doctype_pattern = r'(<!DOCTYPE[^>]*>[\s\S]*?</html>)'
    matches = re.findall(doctype_pattern, content, re.IGNORECASE)

    for match in matches:
        doc = HtmlDocument(
            content=match.strip(),
            source_file=filename,
            source_path=filepath,
            doc_type='full_document'
        )
        doc.has_css = '<style' in match.lower() or 'style=' in match.lower()
        doc.has_js = '<script' in match.lower()
        css_pattern = r'<style[^>]*>([\s\S]*?)</style>'
        doc.css_blocks = re.findall(css_pattern, match, re.IGNORECASE)
        documents.append(doc)

    # Pattern 2: Tag HTML senza DOCTYPE
    if not documents:
        html_pattern = r'(<html[^>]*>[\s\S]*?</html>)'
        matches = re.findall(html_pattern, content, re.IGNORECASE)

        for match in matches:
            doc = HtmlDocument(
                content=match.strip(),
                source_file=filename,
                source_path=filepath,
                doc_type='html_block'
            )
            doc.has_css = '<style' in match.lower() or 'style=' in match.lower()
            doc.has_js = '<script' in match.lower()
            documents.append(doc)

    return documents


def extract_html_fragments(content: str, filename: str, filepath: Path) -> list[HtmlDocument]:
    """
    Estrae frammenti HTML significativi (div, table, etc.)
    """
    fragments = []
    significant_tags = ['div', 'table', 'section', 'article', 'form']

    for tag in significant_tags:
        pattern = rf'(<{tag}\s+[^>]*(?:class|id|style)[^>]*>[\s\S]*?</{tag}>)'
        matches = re.findall(pattern, content, re.IGNORECASE)

        for match in matches:
            if len(match) > 200:
                doc = HtmlDocument(
                    content=match.strip(),
                    source_file=filename,
                    source_path=filepath,
                    doc_type=f'{tag}_fragment'
                )
                doc.has_css = 'style=' in match.lower()
                fragments.append(doc)

    return fragments


def extract_admin_templates(content: str, filename: str, filepath: Path) -> list[HtmlDocument]:
    """
    Estrae template di atti amministrativi.
    """
    templates = []

    patterns = [
        (r'(\[INTESTAZIONE[^\]]*\][\s\S]{100,}?(?:IL DIRIGENTE|DETERMINA|DELIBERA)[\s\S]*?(?:\[Firma|Cognome del Dirigente\]))',
         'atto_amministrativo'),
        (r'(DETERMINAZIONE DIRIGENZIALE[\s\S]{200,}?(?:IL DIRIGENTE|Firma))',
         'determina'),
        (r'(DELIBERAZIONE[\s\S]{200,}?(?:IL CONSIGLIO|IL SINDACO|Firma))',
         'delibera'),
    ]

    for pattern, doc_type in patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        for match in matches:
            if len(match) > 300:
                templates.append(HtmlDocument(
                    content=match.strip(),
                    source_file=filename,
                    source_path=filepath,
                    doc_type=doc_type
                ))

    return templates


def process_file(filepath: Path) -> dict:
    """Processa un singolo file ed estrae tutti i contenuti."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        try:
            content = filepath.read_text(encoding='latin-1')
        except Exception as e:
            return {'error': str(e), 'documents': [], 'fragments': [], 'templates': []}

    return {
        'documents': extract_full_html_documents(content, filepath.name, filepath),
        'fragments': extract_html_fragments(content, filepath.name, filepath),
        'templates': extract_admin_templates(content, filepath.name, filepath)
    }


def scan_directory(directory: Path) -> dict:
    """Scansiona directory per file MD e TXT."""
    results = {
        'scanned_files': [],
        'documents': [],
        'fragments': [],
        'templates': [],
        'stats': {
            'total_files': 0,
            'files_with_content': 0,
            'total_documents': 0,
            'total_fragments': 0,
            'total_templates': 0
        }
    }

    extensions = ['.md', '.txt']

    for ext in extensions:
        for filepath in directory.rglob(f'*{ext}'):
            # Salta file nella cartella tools
            if 'tools' in filepath.parts:
                continue

            results['stats']['total_files'] += 1
            results['scanned_files'].append(str(filepath))

            extracted = process_file(filepath)

            has_content = False

            if extracted.get('documents'):
                results['documents'].extend(extracted['documents'])
                results['stats']['total_documents'] += len(extracted['documents'])
                has_content = True
                print(f"  [HTML] {filepath.name}: {len(extracted['documents'])} documenti completi")

            if extracted.get('fragments'):
                results['fragments'].extend(extracted['fragments'])
                results['stats']['total_fragments'] += len(extracted['fragments'])
                has_content = True
                print(f"  [FRAG] {filepath.name}: {len(extracted['fragments'])} frammenti")

            if extracted.get('templates'):
                results['templates'].extend(extracted['templates'])
                results['stats']['total_templates'] += len(extracted['templates'])
                has_content = True
                print(f"  [TMPL] {filepath.name}: {len(extracted['templates'])} template")

            if has_content:
                results['stats']['files_with_content'] += 1
            else:
                print(f"  [--] {filepath.name}: nessun contenuto HTML")

    return results


def save_document(doc: HtmlDocument, index: int) -> Path:
    """
    Salva un documento nella stessa cartella del file sorgente.
    """
    # Determina nome file basato sul tipo
    type_names = {
        'full_document': 'estratto_html',
        'html_block': 'estratto_html',
        'atto_amministrativo': 'template_atto',
        'determina': 'template_determina',
        'delibera': 'template_delibera',
    }

    base_name = type_names.get(doc.doc_type, f'estratto_{doc.doc_type}')

    # Aggiungi indice se necessario
    if index > 1:
        base_name = f"{base_name}_{index}"

    # Estensione basata sul tipo
    if doc.is_complete or doc.doc_type.endswith('_fragment'):
        filename = f"{base_name}.html"
    else:
        filename = f"{base_name}.txt"

    filepath = doc.output_dir / filename
    content = doc.content

    # Per documenti HTML, assicura struttura valida
    if filepath.suffix == '.html':
        if not content.strip().lower().startswith('<!doctype'):
            if '<html' not in content.lower():
                content = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estratto da {doc.source_file}</title>
    <style>
        body {{ font-family: sans-serif; padding: 2rem; line-height: 1.6; }}
    </style>
</head>
<body>
{content}
</body>
</html>"""
            else:
                content = '<!DOCTYPE html>\n' + content

    filepath.write_text(content, encoding='utf-8')
    return filepath


def generate_report(results: dict, base_dir: Path) -> Path:
    """Genera report HTML riepilogativo."""

    stats = results['stats']

    # Raggruppa per cartella
    by_folder = {}
    for doc in results['documents'] + results['templates']:
        folder = doc.source_path.parent.name
        if folder not in by_folder:
            by_folder[folder] = []
        by_folder[folder].append(doc)

    html = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Report Estrazione HTML/CSS</title>
    <style>
        :root {{
            --primary: #2563eb;
            --success: #16a34a;
            --warning: #f59e0b;
            --bg: #f1f5f9;
            --card: #ffffff;
            --text: #1e293b;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: system-ui, -apple-system, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
            padding: 2rem;
        }}
        .container {{ max-width: 1000px; margin: 0 auto; }}
        h1 {{ color: var(--primary); margin-bottom: 0.5rem; }}
        .subtitle {{ color: #64748b; margin-bottom: 2rem; }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 1rem;
            margin-bottom: 2rem;
        }}
        .stat {{
            background: var(--card);
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        .stat-value {{
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--primary);
        }}
        .stat-label {{ color: #64748b; font-size: 0.9rem; }}
        .section {{
            background: var(--card);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        .section h2 {{
            color: var(--primary);
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid var(--bg);
        }}
        .folder {{ margin-bottom: 1rem; }}
        .folder-name {{
            font-weight: 600;
            color: var(--primary);
            margin-bottom: 0.5rem;
        }}
        .item {{
            padding: 0.5rem 0.75rem;
            margin: 0.25rem 0;
            background: var(--bg);
            border-radius: 6px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.9rem;
        }}
        .badge {{
            padding: 0.2rem 0.5rem;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 500;
        }}
        .badge-html {{ background: #dbeafe; color: #1d4ed8; }}
        .badge-css {{ background: #dcfce7; color: #16a34a; }}
        .badge-tmpl {{ background: #fef3c7; color: #d97706; }}
        .empty {{ color: #94a3b8; text-align: center; padding: 2rem; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Report Estrazione HTML/CSS</h1>
        <p class="subtitle">Generato il {datetime.now().strftime('%d/%m/%Y alle %H:%M')}</p>

        <div class="stats">
            <div class="stat">
                <div class="stat-value">{stats['total_files']}</div>
                <div class="stat-label">File Analizzati</div>
            </div>
            <div class="stat">
                <div class="stat-value">{stats['total_documents']}</div>
                <div class="stat-label">Documenti HTML</div>
            </div>
            <div class="stat">
                <div class="stat-value">{stats['total_templates']}</div>
                <div class="stat-label">Template Atti</div>
            </div>
        </div>

        <div class="section">
            <h2>File Estratti per Cartella</h2>
"""

    if by_folder:
        for folder, docs in sorted(by_folder.items()):
            html += f'<div class="folder"><div class="folder-name">{folder}/</div>'
            for doc in docs:
                badge_class = 'badge-html' if doc.is_complete else 'badge-tmpl'
                badge_text = 'HTML+CSS' if doc.has_css else doc.doc_type
                html += f'''
                <div class="item">
                    <span>{doc.source_file}</span>
                    <span class="badge {badge_class}">{badge_text}</span>
                </div>'''
            html += '</div>'
    else:
        html += '<p class="empty">Nessun contenuto estratto</p>'

    html += """
        </div>
    </div>
</body>
</html>"""

    report_path = base_dir / 'tools' / 'report_estrazione.html'
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(html, encoding='utf-8')
    return report_path


def main():
    if len(sys.argv) > 1:
        base_dir = Path(sys.argv[1])
    else:
        base_dir = Path(__file__).parent.parent

    if not base_dir.exists():
        print(f"Errore: Directory '{base_dir}' non trovata")
        sys.exit(1)

    print(f"\n{'='*60}")
    print("ESTRATTORE HTML/CSS DA FILE MD/TXT")
    print("(salva nella cartella del progetto)")
    print(f"{'='*60}")
    print(f"\nDirectory: {base_dir}")
    print(f"\nScansione in corso...\n")

    results = scan_directory(base_dir)

    stats = results['stats']
    print(f"\n{'='*60}")
    print("RISULTATI")
    print(f"{'='*60}")
    print(f"File analizzati: {stats['total_files']}")
    print(f"Documenti HTML completi: {stats['total_documents']}")
    print(f"Frammenti HTML: {stats['total_fragments']}")
    print(f"Template atti: {stats['total_templates']}")

    # Salva documenti nelle rispettive cartelle
    saved_count = 0

    if results['documents']:
        print(f"\nSalvataggio documenti HTML...")
        # Raggruppa per cartella
        by_folder = {}
        for doc in results['documents']:
            folder = str(doc.output_dir)
            if folder not in by_folder:
                by_folder[folder] = []
            by_folder[folder].append(doc)

        for folder, docs in by_folder.items():
            for i, doc in enumerate(docs, 1):
                filepath = save_document(doc, i)
                print(f"  [SALVATO] {filepath.relative_to(base_dir)}")
                saved_count += 1

    if results['templates']:
        print(f"\nSalvataggio template atti...")
        by_folder = {}
        for doc in results['templates']:
            folder = str(doc.output_dir)
            if folder not in by_folder:
                by_folder[folder] = []
            by_folder[folder].append(doc)

        for folder, docs in by_folder.items():
            for i, doc in enumerate(docs, 1):
                filepath = save_document(doc, i)
                print(f"  [SALVATO] {filepath.relative_to(base_dir)}")
                saved_count += 1

    # Genera report
    report_path = generate_report(results, base_dir)
    print(f"\nReport: {report_path}")

    print(f"\n{'='*60}")
    print(f"COMPLETATO - {saved_count} file salvati nelle cartelle progetto")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
