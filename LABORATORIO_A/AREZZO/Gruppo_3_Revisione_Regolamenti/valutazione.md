# Valutazione Progetto: Revisione Regolamenti Comunali

**Gruppo:** 3
**Sede:** Arezzo
**Data laboratorio:** 20 gennaio 2026
**Data valutazione:** 2026-02-16
**Tempo a disposizione:** ~1 ora

---

## Punteggi per Criterio

| Criterio | Voto (1-10) | Peso | Punteggio |
|----------|-------------|------|-----------|
| Completezza dell'analisi | 8.5 | 25% | 2.13 |
| Qualita della soluzione | 7.5 | 30% | 2.25 |
| Innovativita e uso dell'IA | 6 | 20% | 1.20 |
| Presentabilita del report | 8.5 | 15% | 1.28 |
| Impatto potenziale sulla PA | 8.5 | 10% | 0.85 |
| **TOTALE** | | **100%** | **7.70/10** |

---

## Punti di Forza

1. **Analisi economica di livello professionale.** Il progetto si distingue nettamente per la qualita dell'analisi costi, che presenta due scenari alternativi completi (gestione interna a 65-155K EUR vs. appalto esterno a 130-280K EUR), con voci di spesa dettagliate e itemizzate -- dalle licenze OCR alle consulenze NLP, dalla formazione del personale all'infrastruttura hardware. Sono esplicitati vantaggi e svantaggi di ciascuno scenario e viene formulata una raccomandazione motivata (Scenario B). Questo livello di dettaglio, prodotto in circa un'ora, e' notevole e rende la proposta direttamente utilizzabile da un decisore pubblico.

2. **Architettura di sistema modulare e coerente.** Il sistema e' articolato in cinque moduli funzionali chiaramente definiti (Ingestione OCR, Strutturazione dati, Analisi NLP/AI, Workflow e versioning, Consultazione e ricerca), ognuno con un perimetro ben delimitato e funzioni specifiche. L'approccio modulare dimostra maturita progettuale: consente un'implementazione incrementale, facilita la manutenzione e permette di sostituire o aggiornare singoli componenti. La scelta di includere il modulo di Workflow con versioning e ciclo di approvazione mostra consapevolezza dei processi amministrativi reali.

3. **Deliverable HTML di qualita professionale.** Il documento HTML con foglio di stile CSS dedicato presenta un layout responsive, una palette cromatica istituzionale (blu #0056b3), card modulari per la presentazione dei componenti del sistema, e media queries per l'adattamento a dispositivi mobili. Il tono e il formato sono quelli di una proposta dirigenziale autentica, indirizzata a Sindaco, Assessori e Segretario Generale. Il documento e' immediatamente presentabile in un contesto istituzionale senza modifiche.

---

## Aree di Miglioramento

1. **Assenza di utilizzo dimostrativo dell'IA durante il laboratorio.** Questo e' il limite principale del progetto nel contesto di un laboratorio AI-PACT. L'intelligenza artificiale appare esclusivamente come oggetto della proposta (un sistema che "utilizzerebbe" NLP e AI), ma non vi e' alcuna evidenza che strumenti di IA siano stati impiegati come metodo di lavoro durante il laboratorio. Mancano completamente: prompt utilizzati, output generati da modelli linguistici, esempi di analisi AI applicate a un regolamento reale, o qualsiasi forma di prototipazione. Anche un singolo esempio -- un articolo di regolamento sottoposto a un LLM con il prompt e la risposta risultante -- avrebbe trasformato la proposta da teorica a dimostrativa.

2. **Mancanza di un caso d'uso concreto su un regolamento reale.** La proposta resta interamente sul piano dell'astrazione progettuale. Non viene preso in esame nessun regolamento specifico di un comune toscano, non vengono identificate criticita normative concrete (articoli obsoleti, riferimenti abrogati, incoerenze tra regolamenti), e non viene mostrato un "prima e dopo" che illustri il funzionamento del sistema proposto. L'inclusione di un esempio reale avrebbe reso la proposta molto piu convincente e avrebbe dimostrato la fattibilita dell'approccio.

3. **Assenza di analisi dei rischi e delle resistenze al cambiamento.** Sebbene le risorse umane necessarie siano ben identificate (CED, funzionari giuridici, coordinatore), manca un'analisi strutturata dei rischi di progetto -- in particolare quelli legati alla qualita dell'OCR su documenti datati, alla resistenza organizzativa del personale, alla dipendenza da fornitori esterni, e alla gestione di eventuali dati sensibili nei regolamenti. Le "Considerazioni Finali" accennano alla criticita dell'ingestione documentale, ma senza un piano di mitigazione.

---

## Suggerimenti per il Gruppo

Il lavoro svolto dimostra competenze solide nella progettazione di soluzioni per la PA e una notevole capacita di strutturare una proposta istituzionale credibile in tempi molto ristretti. Per valorizzare ulteriormente il progetto:

- **Aggiungere una dimostrazione pratica di utilizzo dell'IA.** Selezionare un articolo di un regolamento comunale reale (ad esempio dal regolamento edilizio o di polizia urbana di un comune della zona), sottoporlo a un LLM con un prompt mirato (es. "Analizza questo articolo, identifica riferimenti normativi potenzialmente obsoleti, evidenzia problemi di chiarezza linguistica e suggerisci riformulazioni") e includere nel documento sia il prompt che la risposta ottenuta. Questo singolo esempio varrebbe piu di molte pagine di descrizione teorica.

- **Costruire una sezione di risk assessment.** Una tabella con i rischi principali (qualita OCR insufficiente, resistenza al cambiamento, lock-in con il fornitore, costi imprevisti, tutela dei dati) corredati di probabilita, impatto e strategie di mitigazione renderebbe la proposta piu robusta.

- **Inserire una timeline di implementazione.** Anche una semplice tabella con fasi, milestone e tempistiche stimate (piuttosto che la generica indicazione "2-3 anni") darebbe alla proposta una dimensione operativa che attualmente manca.

- **Citare strumenti e piattaforme gia esistenti nella PA.** Fare riferimento a Normattiva, al Piano Triennale per l'Informatica nella PA, o ad altre soluzioni gia adottate in ambito pubblico rafforzerebbe la credibilita e mostrerebbe consapevolezza dell'ecosistema digitale della PA italiana.

---

## Note del Valutatore

Il Gruppo 3 ha affrontato un tema di grande rilevanza e concretezza per la PA locale italiana. La gestione e la revisione dei regolamenti comunali e' un problema reale e diffuso, particolarmente sentito nei comuni medio-piccoli dove le risorse dedicate all'aggiornamento normativo sono limitate. Il tema e' stato scelto con intelligenza e la soluzione proposta e' plausibile e potenzialmente replicabile in molti contesti.

La qualita della proposta come documento istituzionale e' elevata: il formato, il tono, la struttura e il livello di dettaglio dell'analisi costi sono quelli di un documento che potrebbe essere effettivamente presentato in una giunta comunale. Il deliverable HTML con CSS dedicato, comprensivo di layout responsive, e' curato e professionale.

Il limite principale, tuttavia, risiede nella natura esclusivamente teorico-progettuale del lavoro. In un laboratorio dedicato all'uso dell'IA nella PA, il progetto descrive un sistema basato sull'IA senza mai dimostrare l'IA in azione. Si tratta di una proposta che potrebbe essere stata redatta interamente senza l'ausilio di strumenti di intelligenza artificiale, il che la colloca in una posizione ambigua rispetto agli obiettivi formativi del laboratorio. L'IA e' trattata come una promessa futura piuttosto che come uno strumento gia sperimentabile oggi.

Nonostante questo limite, il punteggio complessivo di 7.70/10 riflette il buon livello generale del lavoro svolto nel tempo a disposizione: il problema e' reale, la proposta e' strutturata, il deliverable e' professionale, e l'impatto potenziale e' significativo. Con l'aggiunta di una componente dimostrativa dell'IA, questo progetto avrebbe potuto raggiungere punteggi sensibilmente superiori.

---

*Valutazione generata automaticamente - Progetto AI-PACT*
