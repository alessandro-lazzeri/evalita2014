Input sono 5 file txt:
	1_ con un text di un tweet per riga
	2_ con un token per ciascuna riga --> estratti precedentemente dal file 1 con il tokenizer
	3_ con una parola positiva per riga ("ottimo" /n "fantastico"....)
	4_ con parola negative per riga (come sopra)
	5_ file dove salvare il risultato: word, , frequenza_in_tweet, score_totale, pmi_positivo, pmi_negativo

I file 3 e 4 devono essere definiti scegliendo delle parole che si ritengono fortemente polarizzate a priori;
queste parole sono usate per calcolare lo score pmi di ciascun termine che compare nel file 2 con i token.

Per la formula mi sono rifatto a questo esempio: 
http://stats.stackexchange.com/questions/80730/calculating-pointwise-mutual-information-between-two-strings

Per effettuare il calcolo su bigrammi o trigrammi � necessario modificare il file 2_token.txt;
mettendo in ciascuna riga del file i bigrammi (trigrammi ecc) la PMI viene calcolata su questi (questa opzione non � stata testata).