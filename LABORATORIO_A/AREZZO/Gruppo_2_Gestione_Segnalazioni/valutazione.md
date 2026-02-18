# Valutazione Progetto: Gestione Segnalazioni Cittadini

**Gruppo:** 2
**Sede:** Arezzo
**Data laboratorio:** 20 gennaio 2026
**Data valutazione:** 2026-02-16
**Tempo a disposizione:** ~1 ora

---

## Punteggi per Criterio

| Criterio | Voto (1-10) | Peso | Punteggio |
|----------|-------------|------|-----------|
| Completezza dell'analisi | 8 | 25% | 2.00 |
| Qualita della soluzione | 9 | 30% | 2.70 |
| Innovativita e uso dell'IA | 8.5 | 20% | 1.70 |
| Presentabilita del report | 9 | 15% | 1.35 |
| Impatto potenziale sulla PA | 9 | 10% | 0.90 |
| **TOTALE** | | **100%** | **8.65/10** |

---

## Punti di Forza

1. **Deliverable interattivo di qualita eccezionale per il tempo a disposizione.** Il prototipo HTML non e un semplice documento statico: include un diagramma di flusso Mermaid.js ben strutturato in 4 fasi, un mockup di dashboard split-screen con pannello input e pannello risposta, e soprattutto due scenari simulabili tramite pulsanti (scenario normale e scenario con conflitto). Questo tipo di artefatto e immediatamente presentabile a un dirigente comunale per ottenere il consenso al progetto. La cura del CSS (variabili, responsivita, stili di stampa) denota attenzione al dettaglio professionale.

2. **Architettura del processo matura e consapevole dei vincoli della PA.** Il flusso a 4 fasi (Ingestion/Normalizzazione, Smistamento AI, Lavorazione multi-ufficio, Output con Human-in-the-loop) dimostra una comprensione profonda di come funziona realmente la gestione delle segnalazioni in un Comune. La scelta progettuale di mantenere l'operatore umano come validatore finale -- l'AI propone, l'uomo approva -- non e scontata e rivela consapevolezza delle responsabilita giuridiche e amministrative che impediscono una piena automazione nella PA.

3. **Funzionalita anti-contraddizione genuinamente innovativa.** Il requisito FR-012 (Logic Check Anti-Contraddizione) rappresenta un elemento originale che va oltre la semplice automazione. L'idea che l'AI confronti le risposte provenienti da uffici diversi prima di comporre la bozza, bloccando l'automazione e generando un alert quando rileva incoerenze, affronta un problema reale e frequente nella PA. Lo scenario di conflitto nel mockup -- Ufficio Manutenzione che programma lavori con mezzi pesanti vs. Polizia Locale che segnala chiusura strada per fiera -- e un esempio concreto e credibile che dimostra l'utilita pratica di questa funzionalita.

---

## Aree di Miglioramento

1. **Mancanza di una sezione AS-IS, anche sintetica.** Pur comprendendo il vincolo temporale, anche 3-4 righe che descrivessero il processo attuale ("Oggi le segnalazioni arrivano via email e vengono smistate manualmente dall'operatore URP, con tempi medi di risposta di X giorni") avrebbero dato un punto di partenza rispetto al quale misurare il miglioramento proposto. Un confronto prima/dopo, anche qualitativo, avrebbe rafforzato la proposta.

2. **Requisiti funzionali solo parzialmente documentati.** Vengono presentati 3 requisiti funzionali (FR-002, FR-012, FR-014) su una numerazione che suggerisce un elenco piu ampio. Non e chiaro se il gruppo avesse in mente ulteriori requisiti che non ha avuto tempo di documentare. Aggiungere anche solo una lista puntata dei titoli dei requisiti mancanti (FR-001, FR-003, ecc.) avrebbe dato un quadro piu completo dell'ampiezza della soluzione pensata.

3. **Assenza di indicazioni concrete sull'uso dell'IA durante il laboratorio.** Il progetto fa ampio uso concettuale dell'IA come componente della soluzione (Normalizzatore, Classifier, Composer, Logic Check), ma non documenta come l'IA sia stata utilizzata durante il laboratorio stesso per costruire il deliverable. Anche un breve paragrafo ("Abbiamo usato l'IA per generare il CSS, per raffinare il diagramma Mermaid, per simulare le risposte degli uffici") avrebbe dimostrato in modo piu esplicito la competenza d'uso dello strumento.

---

## Suggerimenti per il Gruppo

Il progetto e uno dei piu completi e comunicativi che si possano realizzare in un'ora di laboratorio. Il deliverable HTML interattivo e il punto di forza principale: e un artefatto che puo essere mostrato immediatamente a stakeholder non tecnici per far comprendere la proposta.

Per evolvere il progetto verso una proposta operativa, si consiglia di:

- **Aggiungere una breve analisi AS-IS**: bastano poche righe con dati stimati (numero segnalazioni/mese, tempo medio di risposta attuale, numero di operatori coinvolti) per dare una baseline quantitativa.
- **Completare la lista dei requisiti funzionali**: anche solo come elenco titolato, per mostrare la visione complessiva della soluzione.
- **Inserire 1-2 esempi di prompt AI**: ad esempio il prompt per il Normalizzatore ("Dato il seguente messaggio WhatsApp, estrai: soggetto segnalante, localizzazione, tipologia problema, urgenza...") renderebbe la proposta piu concreta e implementabile.
- **Definire 3-4 KPI di successo**: percentuale di smistamento corretto, tempo medio di risposta, tasso di approvazione bozze AI senza modifiche, riduzione carico operatore.

---

## Note del Valutatore

Il Gruppo 2 ha prodotto uno dei deliverable piu efficaci del laboratorio, dimostrando capacita di sintesi, visione architetturale e attenzione alla comunicazione. In circa un'ora hanno realizzato un prototipo HTML interattivo con diagrammi, mockup funzionante e scenari simulabili -- un risultato che supera ampiamente le aspettative per il tempo concesso.

Il tema scelto (gestione segnalazioni multicanale) e universale nella PA italiana e la soluzione proposta e realistica, con un corretto bilanciamento tra automazione AI e controllo umano. La funzionalita anti-contraddizione e un elemento differenziante che denota pensiero critico: non si sono limitati a proporre "l'AI fa tutto", ma hanno ragionato su cosa puo andare storto e su come gestirlo.

Il punteggio di 8.65/10 riflette un lavoro molto buono, con un deliverable di qualita elevata e un'architettura ben pensata. I margini di miglioramento riguardano principalmente la profondita documentale (AS-IS, requisiti completi, strategia di prompting), aspetti che nel contesto di un'ora di laboratorio sono comprensibilmente sacrificati a favore della realizzazione del prototipo funzionante -- scelta che si rivela vincente dal punto di vista comunicativo.

---

*Valutazione generata automaticamente - Progetto AI-PACT*
