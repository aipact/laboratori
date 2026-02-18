# Laboratorio A - Design Thinking e Problem Solving per l'IA nei Comuni

**Docente:** Marco Scarselli

Raccolta dei materiali prodotti durante i laboratori di "vibe coding" per la Pubblica Amministrazione.

## Contenuti del Laboratorio

- Design Thinking e Problem Solving per l'IA nei Comuni
- Mappatura di sfide comunali (es. traffico, rifiuti, servizi sociali)
- Di quali dati ho bisogno, quali sfide potenziali? Esempio costruito e guidato su un caso d'uso
- Lavoro in gruppo e simulazioni

**Output:** un mini-template (prompt di sistema, dati, contesto, esempi che aiutano LLM) che i partecipanti possono ri-applicare ai loro casi d'uso.

---

## Struttura

```
LABORATORIO_A/
├── AREZZO/                          # 20 gennaio 2026
│   ├── Gruppo_1_VAS_Sintesi_Normativa/
│   ├── Gruppo_2_Gestione_Segnalazioni/
│   ├── Gruppo_3_Revisione_Regolamenti/
│   └── divisione_in_gruppi.md
│
├── LIVORNO/                         # 11 febbraio 2026
│   ├── Gruppo_1_Atti_Amministrativi/
│   ├── Gruppo_3_Tributi_Allegati/
│   ├── Gruppo_4_Comunicazione_Social/
│   ├── Gruppo_5_Protocollo_Segnalazioni/
│   ├── Gruppo_7_Rifiuti_Territorio/
│   └── divisione_in_gruppi.md
│
├── FIRENZE/                         # 26 febbraio 2026 (in arrivo)
│
└── tools/                           # Strumenti di supporto
```

---

## AREZZO - 20 gennaio 2026

3 gruppi | Vincitore: Gruppo 2 (8.5/10) | 📊 **[Classifica completa](AREZZO/classifica_sessione.html)**

### Gruppo 1 — VAS e Sintesi Normativa
Sintesi automatica di documentazione VAS (Valutazione Ambientale Strategica) e normativa multilivello (europea, nazionale, regionale) per supportare i tecnici comunali nella redazione di atti conformi.

| Punteggio | Valutazione | Deliverable |
|-----------|-------------|-------------|
| 7.1/10 | [Scheda valutazione](AREZZO/Gruppo_1_VAS_Sintesi_Normativa/valutazione.html) | [gruppo1.html](AREZZO/Gruppo_1_VAS_Sintesi_Normativa/gruppo1.html) |

### Gruppo 2 — Gestione Segnalazioni Cittadini
Sistema di ingestion multicanale (email, WhatsApp, web) con smistamento AI delle segnalazioni, dashboard operativa split-screen e meccanismo anti-contraddizione tra uffici. Mockup interattivo con simulazione di due scenari.

| Punteggio | Valutazione | Deliverable |
|-----------|-------------|-------------|
| 8.5/10 | [Scheda valutazione](AREZZO/Gruppo_2_Gestione_Segnalazioni/valutazione.html) | [gruppo2.html](AREZZO/Gruppo_2_Gestione_Segnalazioni/gruppo2.html) |

### Gruppo 3 — Revisione Regolamenti Comunali
Piattaforma AI per la revisione e l'aggiornamento dei regolamenti comunali, con architettura modulare a 5 componenti e analisi economica a due scenari di implementazione.

| Punteggio | Valutazione | Deliverable |
|-----------|-------------|-------------|
| 8.3/10 | [Scheda valutazione](AREZZO/Gruppo_3_Revisione_Regolamenti/valutazione.html) | [index.html](AREZZO/Gruppo_3_Revisione_Regolamenti/index.html) |

---

## LIVORNO - 11 febbraio 2026

5 gruppi valutati | Vincitore: Gruppo 1 (9.0/10) | 📊 **[Classifica completa](LIVORNO/classifica_sessione.html)**

### Gruppo 1 — Atti Amministrativi
Assistente IA alla redazione di atti amministrativi. Uso iterativo e critico di Gemini 2.5 Flash per produrre 4 template di atti reali (determine di autorizzazione/diniego, pareri CUP). Dialogo documentato con correzione degli errori del modello. Piano di adozione RAG su 12 mesi.

| Punteggio | Valutazione | Deliverable |
|-----------|-------------|-------------|
| 9.0/10 | [Scheda valutazione](LIVORNO/Gruppo_1_Atti_Amministrativi/valutazione.html) | Template atti (.txt) |

### Gruppo 3 — Tributi e Allegati
Screening automatico di conformita per istruttorie tributarie. Due report HTML: un calcolatore interattivo per il Bando Contributi TARI e un'analisi completa del processo di autorizzazione pubblicitaria con mappatura di tutti gli uffici coinvolti.

| Punteggio | Valutazione | Deliverable |
|-----------|-------------|-------------|
| 8.1/10 | [Scheda valutazione](LIVORNO/Gruppo_3_Tributi_Allegati/valutazione.html) | [report_bando_tari.html](LIVORNO/Gruppo_3_Tributi_Allegati/report_bando_tari.html), [report_autorizzazione.html](LIVORNO/Gruppo_3_Tributi_Allegati/report_autorizzazione_pubblicitaria.html) |

### Gruppo 4 — Comunicazione Social
Dashboard di moderazione social con Voice Chart multi-canale (sito istituzionale, Facebook, Telegram), gestione commenti con template di risposta differenziati per tono, dark mode e persistenza dati via localStorage.

| Punteggio | Valutazione | Deliverable |
|-----------|-------------|-------------|
| 8.6/10 | [Scheda valutazione](LIVORNO/Gruppo_4_Comunicazione_Social/valutazione.html) | [dashboard_moderazione_social.html](LIVORNO/Gruppo_4_Comunicazione_Social/dashboard_moderazione_social.html) |

### Gruppo 5 — Protocollo e Segnalazioni
Proposta strategica per lo smistamento intelligente del protocollo e delle segnalazioni, con tre flussi operativi (ingresso, interni, uscita), sistema di priorita a tre livelli e piano di formazione. Deliverable HTML professionale con navigazione sticky, accordion e grafici Chart.js.

| Punteggio | Valutazione | Deliverable |
|-----------|-------------|-------------|
| 8.3/10 | [Scheda valutazione](LIVORNO/Gruppo_5_Protocollo_Segnalazioni/valutazione.html) | [Gruppo5-Output.html](LIVORNO/Gruppo_5_Protocollo_Segnalazioni/Gruppo5-Output.html) |

### Gruppo 7 — Rifiuti e Territorio
Piano di raccolta e spazzamento rifiuti data-driven per comuni costieri con forte stagionalita turistica. Doppio deliverable: template generico riutilizzabile e piano specifico per il Comune di Orbetello con modulazione stagionale delle frequenze e comunicazione multilingue.

| Punteggio | Valutazione | Deliverable |
|-----------|-------------|-------------|
| 8.1/10 | [Scheda valutazione](LIVORNO/Gruppo_7_Rifiuti_Territorio/valutazione.html) | [piano_rifiuti_orbetello.html](LIVORNO/Gruppo_7_Rifiuti_Territorio/piano_rifiuti_orbetello.html.html), [report_rifiuti.html](LIVORNO/Gruppo_7_Rifiuti_Territorio/report_rifiuti.html) |

*Nota: I gruppi 2 (Flussi Turistici) e 6 (Pratiche Edilizie) sono stati scartati in fase di selezione idee.*

---

## FIRENZE - 26 febbraio 2026

> Materiali in arrivo dopo lo svolgimento del laboratorio.

---

## Criteri di Valutazione

### Selezione delle idee (Fase 1)

| Criterio | Peso | Descrizione |
|----------|------|-------------|
| **Realizzabilità** | 40% | Fattibilità tecnica in 45 minuti di laboratorio |
| **Impatto** | 35% | Beneficio potenziale per l'amministrazione |
| **Valore Didattico** | 25% | Capacità di mostrare le potenzialità dell'AI |

### Valutazione dei progetti (Fase 3)

| Criterio | Peso |
|----------|------|
| Completezza dell'analisi | 20% |
| Qualità della soluzione | 20% |
| Innovatività e uso dell'IA | 20% |
| Presentabilità del report | 20% |
| Impatto potenziale sulla PA | 20% |

> **Nota:** Il processo di valutazione non è definitivo. Sia i criteri, i pesi e i suggerimenti sono parte di un percorso di apprendimento continuo: evolvono sessione dopo sessione sulla base di ciò che osserviamo nei laboratori. Le valutazioni vanno lette come feedback formativo, non come giudizi chiusi.

---

## Tematiche Principali

1. **Redazione atti amministrativi** - Determine, delibere, verbali con AI
2. **Gestione segnalazioni** - Multicanale con smistamento automatico
3. **Conformità normativa** - Verifica e aggiornamento regolamenti
4. **Comunicazione** - Social media, chatbot, multilingue
5. **Workflow documentali** - Protocollo, fascicolazione, priorità
6. **Gestione territoriale** - Rifiuti, edilizia, turismo

---

## Tecnologie Utilizzate

- **Frontend**: HTML5, CSS3, JavaScript
- **Librerie**: Chart.js, Mermaid.js, Font Awesome, html2pdf.js
- **AI**: Gemini, RAG (Retrieval Augmented Generation)
- **Integrazione**: API Sicraweb EVO (Maggioli)

---

## Note sulla Privacy

Tutti i materiali sono stati anonimizzati. I nomi dei partecipanti e i riferimenti specifici a persone fisiche sono stati rimossi dai file di output.
