# 📊 Valutazione Progetto: Istruttoria Automatica Tributi e Allegati

**Gruppo:** 3
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

1. **Doppio caso d'uso concreto e complementare.** Il gruppo ha prodotto due deliverable HTML distinti che coprono due scenari reali e diversi della PA locale: la gestione di un bando contributi TARI per famiglie in disagio economico e l'autorizzazione per esposizione pubblicitaria in centro storico vincolato. Questa scelta dimostra ampiezza di visione e capacità di affrontare problematiche eterogenee (tributi e procedimenti autorizzativi) nell'arco del tempo limitato disponibile.

2. **Report TARI interattivo e funzionalmente ricco.** Il file `report_bando_tari.html` non si limita a un documento statico: include input parametrici modificabili dall'operatore (nome comune, anno, date, numero domande ammesse/escluse), calcoli automatici in JavaScript per la distribuzione del budget, e un riepilogo dinamico della graduatoria. Questo approccio trasforma il report in uno strumento operativo realmente utilizzabile da un funzionario comunale, con validazione dei dati e aggiornamento in tempo reale.

3. **Analisi approfondita degli aspetti normativi e privacy.** Entrambi i report dimostrano una conoscenza solida del contesto normativo. Il report TARI affronta esplicitamente la problematica GDPR (anonimizzazione graduatorie, registro di controllo, base giuridica ex Art. 6 GDPR). Il report sull'autorizzazione pubblicitaria dettaglia con precisione i pareri degli uffici coinvolti (Urbanistica, Soprintendenza, Polizia Locale, Tributi, Patrimonio), la natura vincolante di ciascuno e il corretto inquadramento del Canone Unico Patrimoniale.

---

## 🔧 Aree di Miglioramento

1. **Collegamento esplicito con l'IA insufficientemente documentato.** Sebbene il README menzioni l'estrazione dati da documenti non strutturati come funzione "killer" dell'AI per la PA, i due report HTML non mostrano concretamente dove e come l'IA interverrebbe nel flusso di lavoro. Il report TARI descrive un processo interamente manuale assistito da JavaScript, mentre il report sull'autorizzazione pubblicitaria accenna genericamente alla capacità di un "Agente AI" di analizzare progetti tecnici, senza specificare quale modello, quale tipo di prompt engineering o quale architettura di integrazione si utilizzerebbe. Sarebbe stato utile includere almeno un esempio di prompt utilizzato, un mock-up di output dell'IA sul controllo documentale, o un diagramma del flusso che evidenzi i punti di intervento dell'intelligenza artificiale.

2. **Assenza di analisi AS-IS e quantificazione del problema.** I report partono direttamente dalla soluzione senza descrivere lo stato attuale del processo e i suoi punti di dolore misurabili. Non vengono forniti dati sui tempi medi attuali di istruttoria, sul tasso di errore nel controllo manuale degli allegati, o sul costo-opportunita del lavoro manuale. Anche una stima approssimativa avrebbe rafforzato la giustificazione dell'intervento e permesso di valutare il ROI potenziale.

3. **Il report sull'autorizzazione pubblicitaria manca di interattivita e operativita.** A differenza del report TARI, il documento sull'autorizzazione pubblicitaria e essenzialmente un testo statico con una funzione di export PDF. Non include alcun elemento interattivo, nessuna checklist operativa per l'operatore, nessuna tabella di stato dei pareri da compilare. Questo crea un disequilibrio qualitativo tra i due deliverable e riduce l'utilita pratica del secondo report come strumento di lavoro.

---

## 💡 Suggerimenti per il Gruppo

Il progetto dimostra una buona comprensione dei processi amministrativi e una capacita apprezzabile di produrre deliverable tecnici in tempi ristretti. Per portare il lavoro a un livello superiore, si consiglia di:

- **Rendere esplicito il ruolo dell'IA nel flusso operativo**: creare un diagramma di flusso che mostri i punti esatti in cui l'IA interviene (ad esempio: "L'IA legge l'attestazione ISEE in PDF, ne estrae il valore numerico, lo confronta con la soglia di 8.000 EUR e produce un esito Conforme/Non conforme/Warning"). Questo renderebbe il progetto immediatamente comprensibile anche a decisori non tecnici.

- **Aggiungere un prototipo di prompt e output**: anche un singolo esempio concreto (input: documento ISEE simulato; prompt: "Estrai il valore ISEE e verifica che sia inferiore a 8.000 EUR"; output: tabella Si/No/Warning) avrebbe dato sostanza alla proposta e dimostrato la fattibilita dell'approccio.

- **Uniformare la qualita dei due report**: portare il report sull'autorizzazione pubblicitaria allo stesso livello di interattivita del report TARI, ad esempio aggiungendo una checklist dinamica dei pareri da acquisire con stati (Richiesto/Ricevuto/Favorevole/Negativo/Con prescrizioni) e campi data.

- **Quantificare l'impatto atteso**: stimare il risparmio di tempo per pratica (es. da 45 minuti a 10 minuti per il controllo allegati), il numero di pratiche annue gestibili in piu, e il potenziale di riduzione degli errori.

---

## 📝 Note del Valutatore

Il Gruppo 3 ha affrontato un tema di grande rilevanza pratica per la PA locale: il controllo documentale automatizzato negli iter tributari e autorizzativi. Il README e ben strutturato e identifica con chiarezza le domande chiave del laboratorio. I due report HTML sono tecnicamente solidi: il report TARI in particolare si distingue per la logica JavaScript che simula l'intero ciclo di vita del bando, dalla ricezione delle domande alla liquidazione, con calcoli parametrici coerenti e gestione dei vincoli di budget.

Tuttavia, il progetto soffre di un gap tra la promessa (automazione tramite IA dell'estrazione dati da documenti non strutturati) e la dimostrazione concreta. I deliverable documentano bene *cosa* farebbe il sistema, ma non mostrano *come* l'IA lo farebbe. In un contesto laboratoriale con tempo limitato questa lacuna e comprensibile, ma rappresenta il principale margine di crescita.

L'aspetto privacy nel report TARI e trattato con competenza e va oltre il minimo sindacale, il che denota sensibilita verso un tema cruciale per la PA. L'analisi dei pareri nel report autorizzativo e giuridicamente accurata e dimostra conoscenza diretta dei procedimenti amministrativi.

Il punteggio complessivo di 7.80/10 colloca il progetto nella fascia "buono", con elementi che toccano il "molto buono" sulla qualita della soluzione e sulla completezza dell'analisi, bilanciati da un uso dell'IA piu dichiarato che dimostrato.

---

*Valutazione generata automaticamente - Progetto AI-PACT*
