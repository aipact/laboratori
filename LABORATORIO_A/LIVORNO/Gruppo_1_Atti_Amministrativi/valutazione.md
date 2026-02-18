# Valutazione Progetto: Assistente alla Redazione Atti Amministrativi

**Gruppo:** 1
**Sede:** Livorno
**Data laboratorio:** 11 febbraio 2026
**Data valutazione:** 2026-02-16
**Tempo a disposizione:** ~1 ora

---

## Punteggi per Criterio

| Criterio | Voto (1-10) | Peso | Punteggio |
|----------|-------------|------|-----------|
| Completezza dell'analisi | 8.5 | 25% | 2.13 |
| Qualita della soluzione | 8.5 | 30% | 2.55 |
| Innovativita e uso dell'IA | 8.0 | 20% | 1.60 |
| Presentabilita del report | 7.0 | 15% | 1.05 |
| Impatto potenziale sulla PA | 9.0 | 10% | 0.90 |
| **TOTALE** | | **100%** | **8.23/10** |

---

## Punti di Forza

1. **Eccellente radicamento nel contesto reale della PA.** Il gruppo ha lavorato partendo da un caso d'uso concreto e ben conosciuto: la redazione di determine, delibere e verbali di gara nei Comuni medio/piccoli toscani che utilizzano Sicraweb EVO (Maggioli). L'analisi dei requisiti funzionali (aggiornamento normativo continuo, template per tipologia di atto, integrazione API con il gestionale esistente, conformita GDPR/AGID) dimostra una profonda conoscenza del dominio e dei vincoli operativi reali. La competenza di dominio emerge anche nella correzione puntuale che il gruppo ha fatto all'IA riguardo al Canone Unico Patrimoniale, dimostrando un uso critico e consapevole dello strumento.

2. **Produzione di deliverable concreti e operativamente utili.** Oltre all'analisi concettuale, il gruppo ha prodotto template di atti amministrativi realistici e dettagliati: una Determinazione Dirigenziale completa per autorizzazione pubblicitaria, una bozza di diniego, template per pareri CUP e sezione RICHIAMATI/PARERI. Questi documenti, pur con segnaposto, sono strutturalmente corretti, riportano i riferimenti normativi pertinenti (D.Lgs. 267/2000, D.Lgs. 42/2004, L. 160/2019) e dimostrano come l'IA possa supportare concretamente la standardizzazione degli atti tra uffici diversi. La simulazione multi-ufficio con 5 pareri (Urbanistica, Soprintendenza, Polizia Locale, Tributi, Patrimonio) e la distinzione tra pareri vincolanti e consultivi e particolarmente apprezzabile.

3. **Strategia di adozione realistica e ben articolata.** Il piano di adozione proposto (12 mesi, uffici pilota con personale aperto all'innovazione, "evangelisti" interni, formazione formale, report periodici di utilizzo per uffici e singoli dipendenti) denota una comprensione matura delle dinamiche organizzative della PA. L'approccio tecnologico scelto -- RAG open source integrato con LLM commerciale -- e appropriato e dimostra consapevolezza delle opzioni architetturali disponibili, inclusa l'esigenza di ridurre le allucinazioni attraverso il retrieval da una knowledge base normativa indicizzata.

---

## Aree di Miglioramento

1. **Formato e organizzazione dei deliverable.** I file prodotti sono prevalentemente in formato testo semplice (.txt) e la conversazione con l'IA e stata salvata in forma grezza senza una rielaborazione strutturata. Manca un documento di sintesi che organizzi in modo autonomo i risultati dell'analisi, separandoli dalla traccia della conversazione. Un report HTML o un documento strutturato con sezioni distinte (analisi AS-IS, requisiti, architettura proposta, piano di adozione, template prodotti) avrebbe reso il lavoro piu immediatamente fruibile e presentabile. Il file `analisi_caso_uso_IA.md` e in realta un export della conversazione, non un'analisi rielaborata dal gruppo.

2. **Assenza di una rappresentazione visiva dell'architettura e del flusso di processo.** Il progetto avrebbe beneficiato di un diagramma di flusso del processo di redazione assistita dall'IA, di uno schema architetturale (anche semplificato) che mostrasse l'interazione tra RAG, LLM, Sicraweb EVO e la knowledge base normativa, o di un mockup dell'interfaccia utente. Questi elementi grafici avrebbero reso piu tangibile la soluzione proposta e facilitato la comprensione da parte di stakeholder non tecnici.

3. **Approfondimento limitato su metriche di successo e analisi dei rischi.** Sebbene il gruppo menzioni i report periodici di utilizzo, non vengono definiti KPI specifici e misurabili (ad esempio: riduzione percentuale del tempo di redazione, tasso di errori normativi prima/dopo, percentuale di atti generati con template standard). Analogamente, l'analisi dei rischi (tecnici, organizzativi, normativi) potrebbe essere stata formalizzata in modo piu strutturato, identificando azioni di mitigazione concrete per ciascun rischio. Anche una stima dei costi, sia pure indicativa, avrebbe aggiunto solidita alla proposta.

---

## Suggerimenti per il Gruppo

Il lavoro svolto e di ottima qualita nel merito e dimostra una competenza di dominio non comune. Per elevare ulteriormente il progetto, si consiglia di:

- **Rielaborare i risultati in un documento autonomo e strutturato**, separando chiaramente l'analisi del gruppo dalla conversazione con l'IA. La conversazione con l'IA e un allegato prezioso come documentazione del processo, ma il deliverable principale dovrebbe essere un report sintetico scritto dal gruppo che presenti le conclusioni in modo organico.
- **Aggiungere elementi grafici**: un diagramma di architettura (anche a blocchi semplificati) che mostri come il sistema RAG si interfaccia con Sicraweb EVO tramite API, dove risiede la knowledge base normativa e come avviene il flusso di generazione dell'atto. Un semplice schema a blocchi basterebbe a rendere la soluzione molto piu concreta.
- **Definire 3-5 KPI misurabili** per valutare il successo del progetto pilota (es. tempo medio di redazione di una determina, numero di atti con errori normativi, percentuale di adozione dei template standard, indice di soddisfazione del personale).
- **Esplorare la possibilita di una demo funzionante**: data la scelta del RAG, sarebbe stato interessante mostrare un prototipo minimale (anche con un semplice prompt engineering su un LLM) che, dato un caso d'uso specifico, generasse la bozza di un atto. L'interazione con l'IA sulla simulazione dell'autorizzazione pubblicitaria va gia in questa direzione, ma una presentazione piu strutturata come demo avrebbe avuto maggiore impatto.

---

## Note del Valutatore

Il progetto del Gruppo 1 di Livorno rappresenta un caso d'uso con fortissima rilevanza pratica per la PA italiana. La scelta di focalizzarsi sulla redazione assistita degli atti amministrativi intercetta un bisogno reale e diffuso nei Comuni di ogni dimensione: la necessita di garantire coerenza, completezza e aggiornamento normativo degli atti prodotti da uffici diversi.

Il gruppo ha dimostrato tre qualita distintive: (a) una profonda conoscenza del dominio amministrativo, evidente nella correzione all'IA sul CUP e nella precisione dei template prodotti; (b) un uso intelligente dell'IA come strumento di analisi e co-progettazione, con un prompting iniziale ben strutturato (system prompt con ruolo, contesto e formato atteso); (c) una visione pragmatica dell'adozione tecnologica, con la scelta del RAG e il piano di introduzione graduale.

L'area principale di miglioramento riguarda la forma piuttosto che la sostanza: i contenuti sono solidi ma la loro presentazione e organizzazione non rende piena giustizia alla qualita del lavoro svolto. Un documento di sintesi ben strutturato, con diagrammi e KPI, avrebbe portato il progetto a un livello ancora superiore.

Il punteggio di 8.23/10 colloca il progetto nella fascia "molto buono", riflettendo l'eccellente qualita dell'analisi e la concretezza delle soluzioni proposte, bilanciata da margini di miglioramento nella presentazione e nella formalizzazione di metriche e rischi.

---

*Valutazione generata automaticamente - Progetto AI-PACT*
