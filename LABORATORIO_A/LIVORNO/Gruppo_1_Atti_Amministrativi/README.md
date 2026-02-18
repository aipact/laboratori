# Gruppo 1 - Assistente alla Redazione Atti Amministrativi

## Tema
Sistema AI per assistenza nella redazione di determine, delibere, verbali di gara.

## Obiettivo
- Garantire coerenza e omogeneita degli atti tra i vari uffici
- Aggiornamento automatico riferimenti normativi
- Standardizzazione della composizione degli atti

## Contesto
Comuni toscani che utilizzano Sicraweb EVO (Maggioli)

## Output Prodotti
- `conversazione_concessioni.txt`: Simulazione rilascio autorizzazione pubblicitaria con pareri multi-ufficio
- `analisi_caso_uso_IA.md`: Analisi requisiti per assistente AI redazione atti

### Template Estratti
- `template_determina_autorizzazione.txt`: Template Determinazione Dirigenziale completa
- `template_determina_diniego.txt`: Template diniego autorizzazione
- `template_pareri_cup.txt`: Template pareri Canone Unico Patrimoniale
- `template_richiamati_pareri.txt`: Template sezione RICHIAMATI e PARERI

## Contenuti Analisi Caso d'Uso

### Requisiti Funzionali Identificati
1. Aggiornamento continuo normative (nazionali e locali)
2. Template corretto per tipologia atto
3. Integrazione Sicraweb EVO tramite API
4. Conformita GDPR e linee guida AGID

### Approccio Tecnologico Proposto
- **RAG (Retrieval Augmented Generation)** open source
- Integrazione con LLM commerciale
- Knowledge base normativa indicizzata

### Piano di Adozione
- Introduzione graduale (12 mesi)
- Uffici pilota con personale aperto all'innovazione
- Formazione formale + "evangelisti" interni
- Report periodici di utilizzo

## Simulazione Autorizzazione Pubblicitaria

### Uffici Coinvolti
| Ufficio | Natura Parere |
|---------|---------------|
| Urbanistica/Edilizia | Vincolante |
| Soprintendenza BB.AA. | Vincolante |
| Traffico/Polizia Locale | Vincolante (sicurezza) |
| Tributi (CUP) | Vincolante |
| Patrimonio/Demanio | Vincolante |

### Documenti Generati
- Bozza Determinazione Dirigenziale (autorizzazione)
- Bozza Diniego (scenario negativo)

## Competenze Coinvolte
- CED
- Ufficio Contratti
- Ufficio Gare

## Valutazione Laboratorio
| Criterio | Punteggio |
|----------|-----------|
| Realizzabilita (40%) | 10/10 |
| Impatto (35%) | 10/10 |
| Valore Didattico (25%) | 9/10 |
| **Totale** | **9.75/10** |

**Nota**: Caso d'uso con punteggio piu alto - rappresenta la quintessenza dell'efficientamento PA.
