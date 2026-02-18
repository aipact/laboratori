# Gruppo 3 - Istruttoria Automatica Tributi e Allegati

## Tema
Estrazione dati da documenti non strutturati per screening conformita tributi.

## Obiettivo
- Automatizzare controllo allegati a domande/istanze
- Verificare completezza documentazione
- Generare report sintesi per operatore

## Contesto
Comuni con gestione bandi contributi e agevolazioni

## Domande Chiave Affrontate
1. Quali sono i 3 allegati piu "faticosi" da controllare manualmente?
2. Quali criteri di conformita deve verificare l'IA (validita documento, corrispondenza importi)?
3. Come strutturare l'output per l'operatore (Tabella "Si/No/Warning")?
4. Quali rischi in caso di errore e come prevedere supervisione umana?

## Output Prodotti
- `report_bando_tari.html`: Report interattivo gestione Bando Contributi TARI
- `report_autorizzazione_pubblicitaria.html`: Report procedura autorizzativa

## Report Bando TARI

### Parametri Simulati
- Budget: 6.000 EUR
- Domande ricevute: 100
- Soglia ISEE: 8.000 EUR
- Contributo max per famiglia: 250 EUR

### Fasi Processo Gestite
1. Ricezione e Protocollo Domande
2. Fascicolazione e Pre-Controllo Documentale
3. Analisi Ammissibilita e Verifiche
4. Stesura Graduatoria Provvisoria
5. Redazione Graduatoria Definitiva
6. Assegnazione e Comunicazione Contributi
7. Liquidazione

### Aspetti Privacy (GDPR)
- Registro di Controllo delle Domande
- Pubblicazione con codici anonimi
- Comunicazioni tramite canali sicuri (PEC/A/R)
- Base giuridica: Art. 6 par. 1 lett. c ed e

### Caratteristiche Tecniche
- Calcoli automatici JavaScript
- Input parametri modificabili
- Riepilogo economico dinamico

## Competenze Coinvolte
- Area Tributi
- Area Finanziaria
- Area Sociale

## Valutazione Laboratorio
| Criterio | Punteggio |
|----------|-----------|
| Realizzabilita (40%) | 9/10 |
| Impatto (35%) | 9/10 |
| Valore Didattico (25%) | 7/10 |
| **Totale** | **8.50/10** |

**Nota**: L'estrazione dati da documenti non strutturati e una funzione "killer" dell'AI per la PA.
