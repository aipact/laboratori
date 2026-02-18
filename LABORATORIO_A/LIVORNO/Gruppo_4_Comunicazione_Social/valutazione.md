# 📊 Valutazione Progetto: Dashboard Moderazione Social per la Comunicazione Istituzionale

**Gruppo:** 4
**Sede:** Livorno
**Data laboratorio:** 11 febbraio 2026
**Data valutazione:** 2026-02-16
**Tempo a disposizione:** ~1 ora

---

## 🎯 Punteggi per Criterio

| Criterio | Voto (1-10) | Peso | Punteggio |
|----------|-------------|------|-----------|
| Completezza dell'analisi | 6.5 | 25% | 1.63 |
| Qualità della soluzione | 7.5 | 30% | 2.25 |
| Innovatività e uso dell'IA | 7.0 | 20% | 1.40 |
| Presentabilità del report | 6.0 | 15% | 0.90 |
| Impatto potenziale sulla PA | 7.5 | 10% | 0.75 |
| **TOTALE** | | **100%** | **6.93/10** |

---

## ✅ Punti di Forza

1. **Problema reale e ben individuato.** Il tema della gestione della comunicazione social e della moderazione dei commenti critici nei Comuni e' una necessita' concreta e molto sentita nella PA. Il gruppo ha identificato con lucidita' le principali aree di conflitto (strade/buche, rifiuti/TARI, tasse, lavori pubblici, polemica politica) che corrispondono ai temi effettivamente piu' dibattuti sui canali social degli enti locali.

2. **Prototipo funzionante e tecnicamente solido.** La dashboard HTML e' completamente funzionante, con un buon livello di interattivita': gestione dinamica dei commenti, sistema di moderazione con risposte rapide differenziate per canale, statistiche in tempo reale, dark mode, persistenza dati via localStorage. L'uso di Tailwind CSS e Font Awesome garantisce un aspetto professionale e responsive.

3. **Concetto di "Voice Chart" ben sviluppato.** L'idea di differenziare il tono comunicativo per canale (Sito Istituzionale = formale e preciso, Facebook = empatico e rassicurante, Stories/Telegram = sintetico e visivo) dimostra una comprensione matura delle dinamiche della comunicazione multicanale nella PA. Questo e' un elemento di valore progettuale significativo.

---

## 🔧 Aree di Miglioramento

1. **Assenza di un documento di analisi separato.** Il file `soluzione_comunicazione.odt` contiene esclusivamente una copia del codice HTML della dashboard, senza alcuna analisi testuale del problema, descrizione del contesto, mappatura degli stakeholder, analisi AS-IS/TO-BE o descrizione della strategia proposta. Tutta l'analisi concettuale e' condensata nel solo README.md, che risulta sintetico. Anche considerando i vincoli temporali del laboratorio, un minimo di documento discorsivo avrebbe rafforzato notevolmente il progetto.

2. **Uso dell'IA non documentato.** Non vi e' alcuna traccia delle interazioni con strumenti di IA generativa nel processo di progettazione o sviluppo. Non sono presenti prompt utilizzati, esempi di output generati dall'IA, ne' riflessioni su come l'IA potrebbe essere integrata nel flusso operativo reale (ad esempio per la generazione automatica delle risposte, il sentiment analysis, o la classificazione dei commenti). Il README menziona funzionalita' come "Sentiment analysis commenti" e "Generazione risposte con tono appropriato", ma queste rimangono solo dichiarazioni senza implementazione o dimostrazione.

3. **Dashboard con dati statici e logica semplificata.** Pur essendo un prototipo, la dashboard lavora solo con dati di esempio hardcoded e commenti generati casualmente da un pool di tre esempi fissi. Le risposte standard sono template statici e identici indipendentemente dal commento ricevuto. Un passo avanti sarebbe stato mostrare almeno un esempio di come l'IA potrebbe generare risposte contestualizzate, anche solo simulandone il risultato nell'interfaccia.

---

## 💡 Suggerimenti per il Gruppo

Il progetto parte da un'intuizione corretta e rilevante: la gestione della comunicazione social nella PA e' un problema reale che richiede strumenti dedicati. La dashboard realizzata dimostra buone competenze tecniche nella prototipazione rapida.

Per migliorare il lavoro, si consiglia di:
- **Documentare il processo progettuale**, anche in forma sintetica: chi sono gli utenti, qual e' il flusso attuale, quali sono i pain point principali e come la soluzione li affronta.
- **Integrare concretamente l'IA nel prototipo**, ad esempio mostrando come un LLM potrebbe analizzare il sentiment di un commento e suggerire una risposta adeguata al tono del canale selezionato. Anche una simulazione statica di questo flusso avrebbe dimostrato maggiore consapevolezza.
- **Arricchire il Voice Chart** con piu' esempi e scenari, trasformandolo in una vera guida operativa per gli operatori della comunicazione.
- **Separare chiaramente codice e documentazione**: il file ODT avrebbe dovuto contenere l'analisi del problema e la descrizione della soluzione, non una copia del codice sorgente.

---

## 📝 Note del Valutatore

Il progetto del Gruppo 4 affronta il tema della comunicazione istituzionale sui social media con un approccio pragmatico, producendo un prototipo di dashboard funzionante e visivamente curato. Il problema individuato e' pertinente e il concetto di Voice Chart multicanale rappresenta un elemento di originalita'.

Tuttavia, il progetto presenta un significativo squilibrio tra la componente tecnica (il prototipo HTML, ben realizzato) e la componente analitico-documentale (quasi assente). Il file ODT, che avrebbe dovuto contenere la soluzione descrittiva, contiene solo il codice della dashboard copiato in un documento di testo. Questo lascia il README.md come unica fonte di contesto e analisi, risultando insufficiente per comprendere appieno la visione progettuale del gruppo.

L'uso dell'IA, pur essendo centrale nel tema del laboratorio, non e' documentato ne' dimostrato nel prototipo. Le funzionalita' avanzate menzionate nel README (chatbot FAQ, sentiment analysis, generazione risposte) rimangono a livello di elenco senza evidenza di esplorazione o implementazione.

Nel complesso, il lavoro e' sufficiente e mostra potenziale, ma avrebbe beneficiato di un migliore bilanciamento tra "fare" (il codice) e "spiegare" (l'analisi e la documentazione del processo).

---

*Valutazione generata automaticamente - Progetto AI-PACT*
