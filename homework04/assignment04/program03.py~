'''
Implementare la funzione text(htmlfile, outfile) che preso in input il percorso htmlfile di
un file in HTML scrive nel file outfile la concatenazione dei testi nei nodi con tag '_text_'
che si trovano direttamente contenuti in nodi con tag 'p'. L'ordine con cui sono concatenati e'
lo stesso di quello con cui si trovano nel file. Quindi la funzione scrive nel file di output
la concatenazione di tutti i paragrafi del file di input.
Esempi
text('wpHTML_in.html', 'wpHTML_out.txt') il file di output 'wpHTML_out.txt' deve essere uguale
a 'wpHTML_check.txt'
text('wpTimBernersLee_in.html', 'wpTimBernersLee_out.txt') il file di output 'wpTimBernersLee_out.txt'
deve essere uguale a 'wpTimBernersLee_check.txt'.

Usare il modulo html e definire un'opportuna classe...
'''

import html

            
class HTMLNode(object):
    def __init__(self,tag,attr,content,closed=True): 	   			     #costruttore
        self.tag = tag 			                  #assegna tag all'oggetto in costruzione
        self.attr = attr 	   			#assegna attributi oggetto in costruzione
        self.content = content 				#assegna il contenuto oggetto costruzione
        self.closed = closed 			      #assegna metodo verifica se il tag è chiuso
        
    def istext(self): 					  #funzione verifica se contenuto è testo
        return self.tag == '_text_' 				       #il tag del testo è _text_

    def find_by_tag(self,tag): 	 			  #verifica contenuto appartiene a un tag
        ret = [] 				     #lista contenente contenuto presente nel tag
        if (self.tag == tag) : ret += [self]            #se appartiene al tag aggiungi alla lista  
        if not self.istext(): 					     #se il contenuto non è testo
            for c in self.content: 				 	  #scansiona il contenuto
                ret += c.find_by_tag(tag)  #aggiungi a lista ricorsivamente il contenuto corretto
        return ret 					 #ritorna lista del contenuto nel tag tag

def text(htmlfile, outfile):  				#da input concatena output testo in tag p
	with open(htmlfile,'rU') as f:  		      #apre file input in lettura unicode
		doc = html.parse(f.read(),HTMLNode)    			#carica in doc file input
	with open(outfile,'a') as g: 		  		   #apre in append il file output
		for i in doc.find_by_tag('p'): 	 		  #scansiona input cercando tag p
			for j in i.content: 	  	       #scansiona contenuto dei paragrafi
				if j.istext(): 			    #se il contenuto di p è testo
					outputs=(j.content)         #assegna quel testo a outputs
					g.write(outputs) 	  #scrive outputs sul file output
