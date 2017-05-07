'''
Implementare la funzione imagegrab che usa urllib2 per scaricare le 
immagini linkate in un documento HTML trovato all'URL dato come 
parametro alla funzione. 
Le immagini vanno salvate su disco con lo stesso
nome con cui sono definite nei link dati dalla pagina.

Ad esempio, se passiamo alla funzione l'url
http://dominio/pagina.html
e l'HTML contiene il tag
<img src="image.png">
Dovrete scaricare l'immagine all'indirizzo
http://dominio/image.png
e salvarla su disco col nome
image.png
e ripetere l'operazione per tutte i tag <img ...>.

Nei nostri test, useremo pagine del corso.

Suggerimento: Usate la classe HTML data nella lezioni, e copiata sotto,
e la funzione htnml.parse per trovare i tag img.
'''

import urllib2, html

class HTMLNode(object):
    def __init__(self,tag,attr,content,closed=True): 				      #costruttore
        self.tag = tag 					   #assegna tag all'oggetto in costruzione
        self.attr = attr				 #assegna attributi oggetto in costruzione
        self.content = content 				 #assegna il contenuto oggetto costruzione
        self.closed = closed 			       #assegna metodo verifica se il tag è chiuso

    def istext(self):					   #funzione verifica se contenuto è testo
        return self.tag == '_text_' 					#il tag del testo è _text_

    def tostring(self): 					   #permette di rendere testo html
        if self.istext(): 							   #se è gia testo
            return self.content 			        #ritorna direttamente il contenuto
        ret = '<'+self.tag 			    #assegna a ret il tag iniziale senza chiuderlo
        for k, v in self.attr.items():			        #scansiona ulteriori attributi tag
            ret += ' '+k+'="'+v+'"'			  #aggiunge al tag gli ulteriori attributi
        ret += '>' 								    #chiude il tag
        if self.closed: 						       #se il tag è chiuso
            for c in self.content: 					   #scansiona il contenuto
                ret += c.tostring() 		#tramite ricorsione rende testo ulteriori sottotag
            ret += '</'+self.tag+'>'		 #aggiunge a ret il tag di chiusura del tag aperto 
        return ret 						#ritorna testo html ricorsivamente
    
    def find_by_tag(self,tag): 				   #verifica contenuto appartiene a un tag
            ret = [] 				      #lista contenente contenuto presente nel tag
            if self.tag == tag: ret += [self] 		 #se appartiene al tag aggiungi alla lista
            if not self.istext(): 		 		      #se il contenuto non è testo
                for c in self.content: 					   #scansiona il contenuto
                    ret += c.find_by_tag(tag) #aggiungi a lista ricorsivamen il contenuto corretto
            return ret 					  #ritorna lista del contenuto nel tag tag

def imagegrab(url):
    '''Scrivere il codice qui.'''
    u = urllib2.urlopen(url) 		  #assegna a u l'url passato come parametro usando urllib2
    inpt = html.parse(u.read(), HTMLNode) 		  #carica in inpt l'html presente nell'url
    lstimg = [] 					       #inizializza la lista nome immagini
    for i in inpt.find_by_tag('img'):		   #scansiona il file nell'url cercando il tag img
        lstimg += i.attr.values() 	#aggiunge alla lista gli attributi src (i percorsi) di img
    lsturl = url.rsplit('/') #assegna a lsturl indirizzo immagine separandolo dal dominio iniziale 
								       #(ottengo /immagini/img.png
    lsturl.pop() 				    #rimuove e ritorna percorso immagine superiore
    for i in lstimg: 						 #scansiona la lista nome immagini
        lsturl.append(i) 					  #aggiungo a lsturl nome immagine
        strurl = '/'.join(lsturl)  #concatena la directory dell'immagine (nomesito.com/urlimg.png)
        s = urllib2.urlopen(strurl)		   #assegno ad s l'indirizzo immagine come stringa
        with open(str(lsturl.pop()),'wb') as outpt:    #apre il canale per il salvataggio immagine
            outpt.write(s.read()) 			 #salva effettivamente su disco immagine s
