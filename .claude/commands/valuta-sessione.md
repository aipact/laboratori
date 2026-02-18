# Valutatore Sessione Laboratoriale - AI-PACT (Report HTML)

Sei un valutatore esperto che analizza l'intera sessione laboratoriale, confrontando tutti i progetti dei gruppi e producendo un report HTML professionale e visivamente accattivante.

## CONTESTO FONDAMENTALE: Vincoli Temporali del Laboratorio

**I partecipanti hanno avuto SOLO 1 ora / 1 ora e mezza** per completare l'intero percorso: dall'individuazione del problema alla realizzazione del deliverable. Il report HTML deve riflettere questa consapevolezza nel tono dell'analisi: i commenti devono essere calibrati sul tempo realmente a disposizione. Evitare critiche che presuppongano tempi di lavoro maggiori (es. "manca l'analisi AS-IS dettagliata", "assenza di piano di implementazione"). I punteggi nelle valutazioni.md riflettono già questa calibrazione.

## Il tuo compito

1. Leggi tutti i file `valutazione.html` presenti nelle cartelle dei gruppi
2. Produci un report comparativo HTML con ranking, grafici CSS e analisi trasversale
3. **SCRIVI il file `classifica_sessione.html`** nella cartella della sede usando il tool Write

## Input atteso

L'utente ti fornirà il percorso della cartella della sede (es. `LABORATORIO_A/LIVORNO/`)

## Processo di Valutazione

### Step 1: Raccolta Dati
Per ogni cartella Gruppo_* nella sede:
- Leggi il file `valutazione.html` (se esiste)
- Se non esiste, segnalalo nel report
- Raccogli TUTTI i punteggi: totale e per singolo criterio

### Step 2: Analisi Comparativa
Confronta tutti i gruppi su ogni criterio:
- Chi eccelle in cosa?
- Quali pattern emergono?
- Quali errori sono comuni?

### Step 3: Proclamazione Vincitore
Identifica il gruppo con il punteggio totale più alto e motiva la scelta.

### Step 4: Scrivi il file HTML
**IMPORTANTE: Scrivi il file `classifica_sessione.html` dentro la cartella della sede usando il tool Write**

## Criteri di Valutazione (reminder)

| Criterio | Peso |
|----------|------|
| Completezza dell'analisi | 20% |
| Qualità della soluzione | 20% |
| Innovatività e uso dell'IA | 20% |
| Presentabilità del report | 20% |
| Impatto potenziale sulla PA | 20% |

## Standard Grafici AI-PACT

Il report HTML DEVE seguire questi standard grafici:

### Palette Colori
```
--primary: #1a3a5c        /* Blu istituzionale scuro - header, titoli */
--primary-light: #2c5f8a  /* Blu medio - hover, accenti */
--accent: #e67e22         /* Arancione - elementi di spicco, badge vincitore */
--accent-gold: #f1c40f    /* Oro - medaglie */
--accent-silver: #95a5a6  /* Argento - medaglie */
--accent-bronze: #cd7f32  /* Bronzo - medaglie */
--success: #27ae60        /* Verde - punteggi alti (>=8) */
--warning: #f39c12        /* Giallo/Arancio - punteggi medi (6-7.9) */
--danger: #e74c3c         /* Rosso - punteggi bassi (<6) */
--bg: #f0f4f8             /* Sfondo pagina */
--card-bg: #ffffff        /* Sfondo card */
--text: #2c3e50           /* Testo principale */
--text-light: #7f8c8d     /* Testo secondario */
--border: #e1e8ed         /* Bordi */
```

### Tipografia
- Font: `'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif`
- Titoli h1: 2rem, font-weight 700
- Titoli h2: 1.4rem, font-weight 600
- Corpo: 1rem, line-height 1.7

### Layout
- Max-width: 1100px centrato
- Card con border-radius: 12px, box-shadow: 0 4px 15px rgba(0,0,0,0.08)
- Padding card: 30px
- Gap tra card: 25px

### Barre di Punteggio (CSS puro, NO JavaScript)
Per ogni punteggio, usare una barra orizzontale colorata:
```css
.score-bar {
    background: #e8ecf1;
    border-radius: 10px;
    height: 24px;
    position: relative;
    overflow: hidden;
}
.score-bar-fill {
    height: 100%;
    border-radius: 10px;
    transition: width 0.3s;
    /* width calcolata inline: style="width: XX%" dove XX = (punteggio/10)*100 */
}
```
- Colore barra: verde se >=8, arancione se >=6, rosso se <6
- Testo del punteggio sovrapposto alla barra

### Medaglie Podio
```css
.medal { font-size: 2.5rem; }
.gold { color: #f1c40f; text-shadow: 0 2px 4px rgba(0,0,0,0.2); }
.silver { color: #95a5a6; }
.bronze { color: #cd7f32; }
```

### Tabella Comparativa
- Header con sfondo primary
- Righe alternate con sfondo leggermente diverso
- Cella punteggio totale in grassetto
- Riga vincitore con bordo sinistro accent e sfondo leggermente dorato

### Header Pagina
- Sfondo gradient: `linear-gradient(135deg, var(--primary), var(--primary-light))`
- Testo bianco
- Badge con sede e data
- Logo testuale "AI-PACT" in alto a destra

### Footer
- Sfondo primary
- Testo "Valutazione generata automaticamente - Progetto AI-PACT"
- Data di generazione

### Responsività
- Su schermi < 768px: tabella con scroll orizzontale
- Card full-width su mobile
- Font-size ridotti del 10% su mobile

### Stampa
```css
@media print {
    body { background: white; }
    .card { box-shadow: none; border: 1px solid #ddd; break-inside: avoid; }
    header { background: var(--primary) !important; -webkit-print-color-adjust: exact; }
}
```

## Struttura HTML del Report

Il file HTML deve contenere queste sezioni nell'ordine:

1. **Header** - Titolo "Classifica Sessione Laboratoriale", sede, data laboratorio, data valutazione, numero gruppi
2. **Podio** - I primi 3 gruppi con medaglie (oro, argento, bronzo), nome progetto e punteggio in grande
3. **Tabella Comparativa** - Tutti i gruppi con punteggi per ogni criterio e totale, ordinati per punteggio decrescente. Ogni punteggio ha la barra colorata
4. **Radar/Analisi per Criterio** - Per ogni criterio: barre comparative di tutti i gruppi affiancate, con il nome del criterio e la media della sessione
5. **Analisi Trasversale** - Card con punti di forza della sessione, aree di miglioramento comuni, e osservazioni per criterio
6. **Il Vincitore** - Card speciale con bordo dorato, motivazione dettagliata della vittoria
7. **Menzioni Speciali** - Badge per: Miglior Innovazione, Miglior Presentazione, Maggior Impatto
8. **Raccomandazioni** - Suggerimenti per i prossimi laboratori basati sui pattern osservati
9. **Footer** - Credits e data

## Template HTML di Riferimento

```html
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Classifica Sessione - [SEDE] | AI-PACT</title>
    <style>
        :root {
            --primary: #1a3a5c;
            --primary-light: #2c5f8a;
            --accent: #e67e22;
            --accent-gold: #f1c40f;
            --accent-silver: #95a5a6;
            --accent-bronze: #cd7f32;
            --success: #27ae60;
            --warning: #f39c12;
            --danger: #e74c3c;
            --bg: #f0f4f8;
            --card-bg: #ffffff;
            --text: #2c3e50;
            --text-light: #7f8c8d;
            --border: #e1e8ed;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.7;
            color: var(--text);
            background: var(--bg);
        }

        .container { max-width: 1100px; margin: 0 auto; padding: 0 20px; }

        /* HEADER */
        header {
            background: linear-gradient(135deg, var(--primary), var(--primary-light));
            color: white;
            padding: 2.5rem 0;
            margin-bottom: 2rem;
        }
        header .container { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; }
        header h1 { font-size: 2rem; font-weight: 700; }
        header .subtitle { opacity: 0.85; font-size: 1rem; margin-top: 0.3rem; }
        .header-badge { background: rgba(255,255,255,0.15); padding: 8px 16px; border-radius: 8px; font-size: 0.9rem; backdrop-filter: blur(4px); }
        .header-brand { font-size: 1.1rem; font-weight: 700; letter-spacing: 1px; opacity: 0.9; }

        /* CARDS */
        .card {
            background: var(--card-bg);
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            padding: 30px;
            margin-bottom: 25px;
            border: 1px solid var(--border);
        }
        .card h2 {
            font-size: 1.4rem;
            font-weight: 600;
            color: var(--primary);
            margin-bottom: 1.2rem;
            padding-bottom: 0.6rem;
            border-bottom: 2px solid var(--border);
        }
        .card-accent { border-left: 4px solid var(--accent); }
        .card-winner { border: 2px solid var(--accent-gold); background: linear-gradient(135deg, #fffdf0, #fff9e6); }

        /* PODIO */
        .podium { display: flex; justify-content: center; align-items: flex-end; gap: 20px; margin: 2rem 0; flex-wrap: wrap; }
        .podium-item { text-align: center; padding: 25px 30px; border-radius: 12px; background: var(--card-bg); box-shadow: 0 4px 15px rgba(0,0,0,0.08); border: 1px solid var(--border); min-width: 200px; }
        .podium-item.first { order: 0; transform: scale(1.08); border-color: var(--accent-gold); box-shadow: 0 6px 20px rgba(241,196,15,0.3); }
        .podium-item.second { order: -1; }
        .podium-item.third { order: 1; }
        .medal { font-size: 2.5rem; display: block; margin-bottom: 0.5rem; }
        .podium-score { font-size: 2rem; font-weight: 700; color: var(--primary); }
        .podium-name { font-size: 0.95rem; color: var(--text-light); margin-top: 0.3rem; }
        .podium-group { font-weight: 600; font-size: 1.1rem; margin-top: 0.5rem; }

        /* TABELLA */
        .table-wrap { overflow-x: auto; }
        table { width: 100%; border-collapse: collapse; font-size: 0.95rem; }
        thead th { background: var(--primary); color: white; padding: 12px 15px; text-align: left; font-weight: 600; white-space: nowrap; }
        tbody td { padding: 12px 15px; border-bottom: 1px solid var(--border); }
        tbody tr:nth-child(even) { background: #f8fafc; }
        tbody tr:hover { background: #edf2f7; }
        tbody tr.winner-row { background: #fffdf0; border-left: 4px solid var(--accent-gold); }
        .total-cell { font-weight: 700; font-size: 1.05rem; }

        /* BARRE PUNTEGGIO */
        .score-bar { background: #e8ecf1; border-radius: 10px; height: 24px; position: relative; overflow: hidden; min-width: 80px; }
        .score-bar-fill { height: 100%; border-radius: 10px; display: flex; align-items: center; justify-content: flex-end; padding-right: 8px; }
        .score-bar-fill span { font-size: 0.75rem; font-weight: 700; color: white; text-shadow: 0 1px 2px rgba(0,0,0,0.3); }
        .score-high { background: linear-gradient(90deg, #2ecc71, #27ae60); }
        .score-mid { background: linear-gradient(90deg, #f39c12, #e67e22); }
        .score-low { background: linear-gradient(90deg, #e74c3c, #c0392b); }

        /* CONFRONTO CRITERI */
        .criteria-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        .criteria-card { background: #f8fafc; border-radius: 8px; padding: 20px; border: 1px solid var(--border); }
        .criteria-card h3 { font-size: 1rem; color: var(--primary); margin-bottom: 0.8rem; }
        .criteria-bar-row { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }
        .criteria-bar-label { font-size: 0.85rem; min-width: 70px; color: var(--text-light); }
        .criteria-bar-container { flex: 1; }
        .criteria-avg { font-size: 0.85rem; color: var(--text-light); margin-top: 0.5rem; font-style: italic; }

        /* MENZIONI SPECIALI */
        .mentions { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; }
        .mention-badge { padding: 20px; border-radius: 10px; text-align: center; }
        .mention-badge .mention-icon { font-size: 1.8rem; display: block; margin-bottom: 0.5rem; }
        .mention-badge .mention-title { font-weight: 600; font-size: 0.9rem; color: var(--text-light); text-transform: uppercase; letter-spacing: 0.5px; }
        .mention-badge .mention-group { font-size: 1.1rem; font-weight: 700; color: var(--primary); margin-top: 0.3rem; }
        .mention-innovation { background: linear-gradient(135deg, #e8f8f5, #d5f5e3); border: 1px solid #a3d9c8; }
        .mention-presentation { background: linear-gradient(135deg, #eaf2f8, #d4e6f1); border: 1px solid #a9cce3; }
        .mention-impact { background: linear-gradient(135deg, #fef9e7, #fdebd0); border: 1px solid #f5cba7; }

        /* LISTA PUNTI */
        .point-list { list-style: none; padding: 0; }
        .point-list li { padding: 10px 15px; margin-bottom: 8px; border-radius: 8px; border-left: 4px solid var(--primary-light); background: #f8fafc; }
        .point-list.strengths li { border-left-color: var(--success); }
        .point-list.weaknesses li { border-left-color: var(--danger); }
        .point-list.recommendations li { border-left-color: var(--accent); }

        /* FOOTER */
        footer {
            background: var(--primary);
            color: white;
            text-align: center;
            padding: 1.5rem;
            margin-top: 2rem;
            font-size: 0.9rem;
            opacity: 0.9;
        }

        /* RESPONSIVE */
        @media (max-width: 768px) {
            header h1 { font-size: 1.5rem; }
            .card { padding: 20px; }
            .podium { flex-direction: column; align-items: center; }
            .podium-item.first { order: -1; transform: scale(1); }
            .podium-item.second { order: 0; }
            .podium-item.third { order: 1; }
            .criteria-grid { grid-template-columns: 1fr; }
            body { font-size: 0.9rem; }
        }

        /* STAMPA */
        @media print {
            body { background: white; }
            .card { box-shadow: none; border: 1px solid #ddd; break-inside: avoid; }
            header { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
            footer { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
        }
    </style>
</head>
<body>
    <!-- Segui la struttura delle 9 sezioni descritte sopra -->
    <!-- Popola con i dati reali estratti dalle valutazioni -->
</body>
</html>
```

## Istruzioni DETTAGLIATE per il contenuto

1. Trova tutte le cartelle Gruppo_* nella sede
2. Leggi il file `valutazione.html` da ogni cartella gruppo
3. Estrai i punteggi totali e per criterio (i 5 voti singoli E il totale pesato)
4. Ordina i gruppi per punteggio totale (decrescente)
5. Costruisci il podio con i primi 3 (o meno se ci sono meno di 3 gruppi)
6. Costruisci la tabella comparativa con barre colorate per ogni punteggio
7. Per ogni criterio, crea le barre comparative e calcola la media
8. Identifica pattern trasversali (punti di forza comuni, aree di miglioramento comuni)
9. Proclama il vincitore con motivazione dettagliata
10. Assegna le menzioni speciali: Miglior Innovazione (punteggio più alto in Innovatività), Miglior Presentazione (punteggio più alto in Presentabilità), Maggior Impatto (punteggio più alto in Impatto)
11. Scrivi 3 raccomandazioni per i prossimi laboratori
12. **IMPORTANTE: Scrivi il file `classifica_sessione.html` dentro la cartella della sede usando il tool Write**

## Calcolo larghezza barre

Per ogni punteggio X (su scala 1-10):
- Larghezza percentuale: `(X / 10) * 100`%
- Classe colore: `score-high` se X >= 8, `score-mid` se X >= 6, `score-low` se X < 6

## Note

- Il file è un singolo HTML autocontenuto (CSS inline nel `<style>`, NO JavaScript, NO dipendenze esterne)
- Tutti i dati devono essere reali, estratti dalle valutazioni
- Se un gruppo non ha valutazione, mostralo in grigio con "Non valutato"
- I punteggi nelle barre devono essere numerici con 1 decimale

## Argomento

$ARGUMENTS - Percorso della cartella della sede (es. LABORATORIO_A/LIVORNO)
