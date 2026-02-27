# Preparazione Sessione Laboratoriale - AI-PACT

Sei un Esperto di Innovazione dei Processi nella Pubblica Amministrazione. Il tuo compito è analizzare le idee progettuali proposte dai partecipanti, selezionare i casi migliori, formare i gruppi di lavoro e produrre un HTML presentabile in plenaria.

## Argomento

$ARGUMENTS - Percorso della sede (es. LABORATORIO_A/FIRENZE) e data del laboratorio

## Input

I dati dei partecipanti si trovano nella cartella `valutazione_idee_progettuali/`. La fonte principale è il file **LABORATORIO.xlsx** (export del Google Form).

### Come leggere l'xlsx

Usa un venv temporaneo con openpyxl:
```bash
python3 -m venv /tmp/xlsx-venv 2>/dev/null; /tmp/xlsx-venv/bin/pip install openpyxl -q 2>/dev/null
/tmp/xlsx-venv/bin/python3 -c "
import openpyxl, json
wb = openpyxl.load_workbook('valutazione_idee_progettuali/LABORATORIO.xlsx', read_only=True)
ws = wb[wb.sheetnames[0]]
rows = list(ws.iter_rows(values_only=True))
header = [str(c) if c else '' for c in rows[0]]
data = []
for r in rows[1:]:
    data.append({header[i]: (str(r[i]) if r[i] else '') for i in range(len(header))})
print(json.dumps(data, ensure_ascii=False, indent=2))
"
```

### Filtrare per sede

La colonna chiave è **`LABORATORIO DI...`** (o simile). Filtra i dati in base alla sede richiesta nell'argomento:
- Se l'argomento contiene "AREZZO" → filtra per righe con "AREZZO"
- Se l'argomento contiene "LIVORNO" → filtra per righe con "LIVORNO"
- Se l'argomento contiene "FIRENZE" → filtra per righe con "FIRENZE"

**Se non ci sono dati per la sede richiesta**, comunica chiaramente: "Non ci sono ancora risposte per la sede di [SEDE]. Il file LABORATORIO.xlsx contiene N risposte, tutte per [altre sedi]." e fermati.

### Colonne attese dal Google Form

| Colonna | Contenuto |
|---------|-----------|
| Informazioni cronologiche | Timestamp di compilazione |
| Squadra o Individuo? | "Squadra" o "Individuo" |
| Nome e cognome | Nome (solo per individui) |
| RUOLO / SETTORE | Ruolo dell'individuo |
| Nome e Cognome dei componenti della squadra | Nomi separati da punto e virgola (solo per squadre) |
| RUOLO / SETTORE dei partecipanti alla squadra | Ruolo della squadra |
| SCRIVI LA TUA IDEA | L'idea proposta |
| email individuale / email del capogruppo del team | Email |
| LABORATORIO DI... | Sede (AREZZO, LIVORNO, FIRENZE) |

### Deduplicazione

Attenzione: possono esserci risposte duplicate (stessa squadra che ha compilato più volte). Verifica per email o nomi simili e tieni solo l'ultima risposta cronologica.

Se l'xlsx non esiste o non è leggibile, cerca altri file nella cartella (CSV, TSV, TXT, MD) o chiedi all'utente.

## Processo in 2 Fasi

### FASE A: Valutazione e Classifica

1. **Leggi i dati** dalla cartella `valutazione_idee_progettuali/`
2. **Calcola il numero di gruppi** necessari:
   - Dimensione ideale: 4-6 persone (mai meno di 3, mai più di 6)
   - Sotto 20 partecipanti → gruppi da 4
   - Sopra 30 partecipanti → gruppi da 5-6
3. **Valuta ogni idea** con punteggio 1-10 su 3 criteri:

| Criterio | Peso | Cosa valutare |
|----------|------|---------------|
| **Realizzabilità in 45 min** | 40% | Il problema può essere affrontato nel tempo? I dati sono generabili/reperibili? |
| **Impatto pratico** | 35% | La soluzione è applicabile "lunedì mattina"? Il problema è sentito come urgente? |
| **Valore didattico** | 25% | Mostra le capacità dell'IA in modo chiaro? Richiede vera intelligenza (analisi, sintesi, strategia)? |

4. **Classifica le idee** e seleziona le migliori (tante quanti i gruppi)
5. **Assegna un nome a ogni gruppo** composto da due parti:
   - **Archetipo**: uno degli 8 personaggi della lezione base (vedi tabella sotto), scelto per affinità tematica col problema del gruppo
   - **Nome creativo**: un nome breve, evocativo e memorabile che descriva il problema/missione del gruppo
   - Formato: **"Team [Archetipo] - [Nome Creativo]"** (es. "Team Galilei - I Previsori del Bilancio", "Team Dante - Gli Semplificatori")

   | Archetipo | Concetto IA | Affinità tematica | Colore |
   |-----------|-------------|-------------------|--------|
   | **Galilei** | Analisi Predittiva | Progetti su dati, previsioni, KPI, statistiche | #3498db (blu) |
   | **Machiavelli** | Alberi Decisionali | Progetti su regole, procedure, decisioni binarie, burocrazia | #e67e22 (arancione) |
   | **Michelangelo** | Deep Learning | Progetti su classificazione, pattern, dati non strutturati | #27ae60 (verde) |
   | **Dante** | LLM / Generazione testi | Progetti su scrittura, comunicazione, sintesi, traduzione | #9b59b6 (viola) |
   | **Leonardo** | Agente Autonomo | Progetti su automazione, workflow, orchestrazione multi-step | #e74c3c (rosso) |
   | **Ada Lovelace** | Visione / Input | Progetti su strategia, pianificazione, definizione obiettivi | #1abc9c (teal) |
   | **Simone Weil** | Processo / Senso | Progetti su ottimizzazione del lavoro, riduzione fatica, dignità | #f39c12 (giallo) |
   | **Mary Oliver** | Output / Cura | Progetti su servizi al cittadino, qualità, attenzione, verifica | #2c3e50 (antracite) |

   **Regole di assegnazione**: scegli l'archetipo la cui affinità tematica è più vicina al problema del gruppo. Ogni archetipo può essere usato una sola volta. Se ci sono meno di 8 gruppi, usa solo quelli più pertinenti. Se un gruppo ha un tema davvero lontano da tutti gli archetipi, usa solo il nome creativo senza forzare un archetipo fuori contesto (es. "Gli Esploratori del Territorio" invece di "Team Galilei - Gli Esploratori del Territorio").

6. **Categorizza ogni idea** in una delle 4 aree di lavoro:
   - **SOS Burocrazia** → Semplificare comunicazioni, atti, procedure
   - **Sfera di Cristallo** → Decisioni strategiche basate su dati
   - **Pompiere** → Gestione crisi, polemiche, comunicazione
   - **Segretario Perfetto** → Verbali, email, task management, workflow
6. **Assegna una Track** della Fase 2 a ogni gruppo:
   - **📊 Dati** → per progetti quantitativi (KPI, budget, classifiche)
   - **⚙️ Processo** → per workflow e coordinamento tra uffici
   - **📜 Normativa** → per atti, regolamenti, conformità
   - **📣 Comunicazione** → per servizi al pubblico, social, crisi

**MOSTRA la classifica all'utente e CHIEDI CONFERMA prima di procedere alla Fase B.**

### FASE B: Formazione Gruppi e Output

Dopo conferma dell'utente:

1. **Componi i gruppi** seguendo queste regole:
   - Le SQUADRE già formate restano intatte
   - Gli INDIVIDUI la cui idea è selezionata diventano TEAM LEADER
   - I partecipanti "liberi" vanno distribuiti per: affinità tematica, competenze complementari, equilibrio tecnici/amministrativi
   - MAI smembrare squadre già formate

2. **Prepara il rompighiaccio** per ogni gruppo: 5 domande per lo STEP 1 (Intervista Strategica) che coprono:
   - Perimetro del problema (cosa include e cosa no)
   - Utenti/beneficiari e dimensioni
   - Dati, documenti o normative necessarie
   - Risorse, budget, personale per la soluzione
   - Metriche di successo e vincoli

3. **Scrivi 3 file di output** usando il tool Write:

#### File 1: `{SEDE}/selezione_gruppi.html`
L'HTML per la presentazione in plenaria (vedi template sotto).

#### File 2: `{SEDE}/divisione_in_gruppi.md`
Il markdown strutturato con la composizione dei gruppi.

#### File 3: Cartelle `{SEDE}/Gruppo_N_Tema/README.md`
Crea le cartelle per ogni gruppo con un README iniziale contenente: nome del gruppo, tema, membri, track assegnata.

## Regole di Valutazione

- Se un problema contiene più sotto-problemi, valutalo come caso unico sulla fattibilità complessiva
- Se il proponente suggerisce una soluzione tecnica irrealizzabile in 45 min, valuta il PROBLEMA sottostante e suggerisci un approccio alternativo nel rompighiaccio
- Privilegia problemi che permettano di produrre un deliverable HTML concreto

## Template HTML — `selezione_gruppi.html`

Il file HTML DEVE essere ottimizzato per **proiezione in plenaria su schermo orizzontale**:

### Principi di layout
- **Vista iniziale**: tutti i gruppi visibili senza scroll su schermo 16:9
- **Card orizzontali affiancate** in griglia responsive (3-4 colonne su desktop)
- **Font grandi e leggibili** da distanza (nomi partecipanti almeno 0.9rem)
- **Colore del gruppo** per identificazione visiva rapida
- **Due viste**: Dashboard (panoramica gruppi) e Dettaglio (rompighiaccio per ogni gruppo)

### Struttura della pagina

**1. Header compatto** — Titolo sessione, sede, data, numero partecipanti/gruppi

**2. Dashboard Gruppi (vista principale)** — Griglia di card, una per gruppo:
```
┌─────────────────────────┐
│ 📊 Team Galilei         │
│ "I Previsori del        │
│  Bilancio"              │
│ ─────────────────────── │
│ 👤 Team Leader: Nome    │
│ • Membro 1 (Ruolo)     │
│ • Membro 2 (Ruolo)     │
│ • Membro 3 (Ruolo)     │
│ • Membro 4 (Ruolo)     │
│ ─────────────────────── │
│ Track: 📜 Normativa     │
│ Area: SOS Burocrazia    │
└─────────────────────────┘
```
Ogni card ha un colore di accento diverso (bordo superiore colorato) per distinguere i gruppi a colpo d'occhio. Il Team Leader è evidenziato in grassetto.

**3. Tabella Valutazione** (sotto la dashboard, scrollabile) — Classifica completa di TUTTE le idee con punteggi, anche quelle non selezionate (in grigio).

**4. Dettaglio Gruppi** (sezioni espandibili o card grandi) — Per ogni gruppo:
- Tema e motivazione della selezione (2 righe)
- Rompighiaccio: le 5 domande per STEP 1
- Track consigliata con il prompt di partenza dalla pagina ISTRUZIONI

**5. Footer** — Credits AI-PACT, data

### Palette Colori AI-PACT
```
--primary: #1a3a5c
--primary-light: #2c5f8a
--accent: #e67e22
--success: #27ae60
--warning: #f39c12
--danger: #e74c3c
--bg: #f0f4f8
--card-bg: #ffffff
--text: #2c3e50
--text-light: #7f8c8d
--border: #e1e8ed
```

### Colori card gruppi (bordo superiore, 8 colori ciclici)
```
Gruppo 1: #3498db (blu)
Gruppo 2: #e67e22 (arancione)
Gruppo 3: #27ae60 (verde)
Gruppo 4: #9b59b6 (viola)
Gruppo 5: #e74c3c (rosso)
Gruppo 6: #1abc9c (teal)
Gruppo 7: #f39c12 (giallo)
Gruppo 8: #2c3e50 (antracite)
```

### Specifiche tecniche
- HTML singolo autocontenuto (CSS nel `<style>`, NO dipendenze esterne)
- JavaScript SOLO per toggle vista dashboard/dettaglio (click su card per espandere)
- Font: `'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif`
- Max-width: 1400px (più largo del solito per sfruttare lo schermo)
- Responsive e print-friendly
- I nomi dei partecipanti devono essere leggibili da 3-4 metri di distanza su un proiettore

### Navigazione
- **Click su una card** → mostra il dettaglio del gruppo (rompighiaccio, track, prompt di partenza)
- **Pulsante "Torna alla dashboard"** → torna alla vista panoramica
- **Sezione "Classifica idee"** → accessibile tramite link/pulsante nell'header

## Note

- Leggi la pagina `LABORATORIO_A/ISTRUZIONI/index.html` per allinearti al metodo e alle track della Fase 2
- I prompt di partenza per ogni track sono nella pagina ISTRUZIONI (Step 2)
- Se la sede ha già file esistenti (es. da una sessione precedente), NON sovrascriverli
