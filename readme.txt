Input per PMI.py sono 5 file txt:
	1_ con un text di un tweet per riga
	2_ con un token per ciascuna riga --> estratti precedentemente dal file 1 con il tokenizer
	3_ con una parola positiva per riga ("ottimo" /n "fantastico"....)
	4_ con parola negative per riga (come sopra)
	5_ file dove salvare il risultato: word, , frequenza_in_tweet, score_totale, pmi_positivo, pmi_negativo

I file 3 e 4 devono essere definiti scegliendo delle parole che si ritengono fortemente polarizzate a priori;
attualmente sono stati tradotti dei vocaboli polarizzati presi da SentiWorldNet
Queste parole sono usate per calcolare lo score pmi di ciascun termine che compare nel file 2 con i token.

Per la formula della PMI mi sono rifatto a questo esempio: 
http://stats.stackexchange.com/questions/80730/calculating-pointwise-mutual-information-between-two-strings

Per effettuare il calcolo su bigrammi o trigrammi è necessario modificare il file 2_token.txt;
mettendo in ciascuna riga del file i bigrammi (trigrammi ecc) la PMI viene calcolata su questi (questa opzione non è stata testata).

Operazioni da effettuare sul file tweet.txt per generare gli input:

tweet.txt --> splitter --> 1_text.txt
1_text.txt--> tokenizer --> 2_token.txt
