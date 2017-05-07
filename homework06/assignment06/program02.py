'''Scrivere una funzione tw_stats(twfile) che prende in input un file
in formato json che contiene una lista di tweets e ritorna un dizionario
che contiene i seguenti dati statistici:
- 'tweets': numero di tweets
- 'retweeted': un dizionario contenente:
               'count': numero retweets. Si riconoscono perche' contengono
                        la chiave 'retweeted_status' il cui valore e' un dizionario.
               'max': massimo numero di volte che un tweet e' stato retweeted.
                      Il numero di volte che un tweet e' stato retweeted e' il valore
                      della chiave 'retweet_count' nel dizionario di 'retweeted_status'
               'name': il nome dell'utente che ha scritto il tweet piu' retweeted.
                       Il nome dell'utente che ha originato un retweeet e' il valore
                       della chiave 'screen_name' nel dizionario della chiave 'user'
                       nel dizionario 'retweeted_status'.
               'text': il testo del tweet piu' retweeted. Il testo di un retweet e' il
                       valore della chiave 'text' nel dizionario di 'retweeted_status'.
- 'users': un dizionario contenente:
           'max_followers': il numero massimo di followers tra tutti gli utenti dei
                            tweets del file. Il numero di followers e' il valore della
                            chiave 'followers_count' nel dizionario della chiave 'user'
                            di un tweet.
           'name': il nome dell'utente con il massimo numero di followers. Il nome
                   dell'utente di un tweet e' il valore della chiave 'screen_name'
                   nel dizionario 'user'.
- 'words': un dizionario contenente dati statistici circa le parole nei tweets. 
           Per parola si intende una sequenza di caratteri alfabetici (minuscoli o 
           maiuscoli) delimitata da o whitespaces o l'inizio o la fine del testo.
           Convertite le parole in lowercase per fare i conteggi.
           'count': numero parole distinte.
           'most_freq': lista ordinata delle parole di lunghezza almeno 5 che occorrono
                        almeno n/100 volte (divisione intera), dove n e' il valore di 'count'.

Suggerimento 1: Il formato json e' un formato ASCII per salvare su file liste, dizionari, numeri e stringhe. In Python, basta usare la funzione load() del modulo json per caricare il contenuto dei files json in memoria. Per "vedere" i dati, semplicemente aprite il file json in un editor di testo.

Suggerimento 2: Per determinare le parole, potete usare ascii_letters nel modulo string.

Esempi:
tw_stats('file02_01_in.json') --->
{'tweets': 1000,
 'retweeted': {'count': 273,
               'max': 58402,
               'name': u'NiallOfficial',
               'text': u"#privacy ! Doesn't exist"},
 'users': {'max_followers': 331310, 'name': u'stinsonsays'},
 'words': {'count': 2167, 'most_freq': [u'about', u'christmas', u'people']}}
 
tw_stats('file02_02_in.json') --->
{'tweets': 1500,
 'retweeted': {'count': 368,
               'max': 57057,
               'name': u'Louis_Tomlinson',
               'text': u"It's my birthday tomorrow ahhhhhh !! How is everyone?"},
 'users': {'max_followers': 105293, 'name': u'Kuwaiti1DLover'},
 'words': {'count': 2926,
           'most_freq': [u'about', u'christmas', u'follow', u'people']}}
'''

import json
import string

def tw_stats(twfile):
    '''Scrivere il codice qui.'''
        
