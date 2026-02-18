# 📊 Valutazione Progetto: Piano di Raccolta Rifiuti Data-Driven per il Comune di Orbetello

**Gruppo:** 7
**Sede:** Livorno
**Data laboratorio:** 11 febbraio 2026
**Data valutazione:** 2026-02-16
**Tempo a disposizione:** ~1 ora

---

## 🎯 Punteggi per Criterio

| Criterio | Voto (1-10) | Peso | Punteggio |
|----------|-------------|------|-----------|
| Completezza dell'analisi | 8 | 25% | 2.00 |
| Qualità della soluzione | 8 | 30% | 2.40 |
| Innovatività e uso dell'IA | 7 | 20% | 1.40 |
| Presentabilità del report | 8 | 15% | 1.20 |
| Impatto potenziale sulla PA | 8 | 10% | 0.80 |
| **TOTALE** | | **100%** | **7.80/10** |

---

## ✅ Punti di Forza

1. **Doppio deliverable con approccio scalabile.** Il gruppo ha prodotto sia un template generico riutilizzabile da qualsiasi comune (`report_rifiuti.html`) sia una versione calata su un caso concreto -- il Comune di Orbetello (`piano_rifiuti_orbetello.html.html`). Questo approccio "dal generico allo specifico" dimostra una maturita progettuale notevole per il tempo a disposizione e offre un valore aggiunto reale per la PA: il template puo essere adottato e personalizzato da altri enti.

2. **Analisi contestuale approfondita e orientata al territorio.** Il piano per Orbetello non si limita a riempire i segnaposto del template, ma rielabora in profondita le specificita del territorio: la stagionalita turistica (da 14.500 a oltre 40.000 abitanti in estate), le criticita costiere e lagunari, la gestione delle seconde case, il settore ittico-agricolo, la pulizia delle spiagge e delle dune. Le frequenze di raccolta sono differenziate per zona (centro storico, frazioni costiere, aree periferiche) e per stagione (inverno/estate), dimostrando una comprensione operativa concreta.

3. **Struttura professionale e curata del documento finale.** Il piano per Orbetello presenta un header istituzionale con stemma del Comune, un disclaimer corretto sui dati preliminari, una struttura in due parti (Piano operativo + Piano di comunicazione), fasi temporali articolate (pre-lancio, lancio, mantenimento), responsive design con media query, e una grafica coerente con i colori istituzionali. Il livello di presentabilita e prossimo a quello di un documento ufficiale di una PA.

---

## 🔧 Aree di Miglioramento

1. **Uso dell'IA descritto in modo prevalentemente dichiarativo.** L'IA viene citata in molteplici contesti (chatbot multilingue, mappe interattive, sentiment analysis, video animati, dashboard KPI), ma rimane a livello di proposta senza una descrizione tecnica minima di come verrebbe implementata: non si indica quale tipo di modello per il chatbot, quale piattaforma per la sentiment analysis, quale strumento per la generazione dei video animati. Non emerge nemmeno una riflessione esplicita sul processo di prompting utilizzato durante il laboratorio stesso per generare i deliverable, che avrebbe dato concretezza all'uso dell'IA.

2. **Assenza di analisi AS-IS quantitativa e di indicatori di baseline.** Pur essendo comprensibile dato il vincolo temporale, il piano dichiara dati come "RD attuale stimata tra 60-65% (dati 2023 da verificare)" senza una fonte concreta. I target (75% RD entro 2027, -20% secco residuo, +30% decoro, -50% abbandoni) sono ambiziosi ma non ancorati a un punto di partenza verificato, rendendo difficile valutarne la fattibilita. Una tabella sintetica con i dati attuali reperibili online (ad esempio da ARRR Toscana o ISPRA) avrebbe rafforzato la credibilita.

3. **Refuso ricorrente "Rimostulazione" al posto di "Rimodulazione".** Compare sia nel template generico che nel piano di Orbetello (sezioni 2 e 3), suggerendo un errore nella generazione IA non intercettato in fase di revisione. Inoltre il nome del secondo file (`piano_rifiuti_orbetello.html.html`) presenta una doppia estensione. Questi dettagli, pur minori, riducono la percezione di accuratezza del prodotto finale.

---

## 💡 Suggerimenti per il Gruppo

Il progetto e solido e ben strutturato, e si posiziona tra i lavori piu completi per un laboratorio di un'ora. Per elevarlo ulteriormente:

- **Documentare il processo di prompting:** includere una breve sezione (anche in appendice) che mostri 2-3 prompt chiave utilizzati con l'IA durante il laboratorio, spiegando la logica iterativa (primo prompt generico, affinamento sul caso Orbetello, personalizzazione dei dati). Questo renderebbe il progetto anche un case study metodologico sull'uso dell'IA nella PA.

- **Aggiungere almeno una stima economica di massima:** anche una sola tabella con ordini di grandezza dei costi (isole ecologiche interrate, chatbot, personale stagionale) rispetto ai risparmi attesi (ottimizzazione rotte, tariffa puntuale) darebbe concretezza alla fattibilita del piano.

- **Integrare un mockup visivo:** un wireframe di bassa fedelta della dashboard KPI o della mappa interattiva, anche realizzato con l'IA, avrebbe reso tangibile la visione tecnologica proposta e avrebbe mostrato un uso piu avanzato degli strumenti di generazione.

- **Rileggere sempre l'output dell'IA:** una rapida revisione avrebbe permesso di correggere "Rimostulazione" e la doppia estensione del file, migliorando la qualita percepita complessiva.

---

## 📝 Note del Valutatore

Il Gruppo 7 ha affrontato una sfida particolarmente complessa: la gestione dei rifiuti in un comune con forte stagionalita turistica, che introduce variabili logistiche, comunicative e organizzative non banali. In circa un'ora, il gruppo ha prodotto due documenti HTML ben strutturati che coprono sia la dimensione operativa (raccolta e spazzamento) sia quella comunicativa (piano multicanale e multilingue con fasi temporali).

L'approccio template-generico + caso-specifico e intelligente e replicabile. La calata su Orbetello dimostra che il gruppo non si e limitato a generare un documento astratto, ma ha cercato dati reali (popolazione, frazioni, criticita costiere) per contestualizzare la proposta. Il piano di comunicazione e articolato e include elementi moderni (gamification, campagne "Turismo Consapevole", materiale multilingue).

Il principale limite risiede nella dimensione dell'innovazione IA, che resta a livello di visione futura piuttosto che di dimostrazione concreta. Non emerge chiaramente come l'IA sia stata utilizzata nel processo di lavoro del laboratorio, ne viene proposto un prototipo funzionante (anche minimale) delle soluzioni IA descritte.

Nel complesso, un lavoro di buona qualita che dimostra capacita di analisi territoriale, senso pratico nella progettazione del servizio, e attenzione alla comunicazione verso i cittadini. Il punteggio di 7.80/10 riflette un progetto solido, ben al di sopra della sufficienza, con margini di crescita nell'uso concreto e documentato dell'IA.

---

*Valutazione generata automaticamente - Progetto AI-PACT*
