'''
items(infile, outfile) trova in ogni linea del file infile il nome di un
articolo (solamente caratteri alfabetici) e separati da spazi uno o piu'
numeri e deve scrivere nel file outfile per ogni articolo presente nel file
infile una linea che contiene l'articolo e separato da ':' la somma dei
numeri relativi ad esso. Ci possono essere piu' linee del file infile relative
allo stesso articolo. Il linee del file outfile devono essere ordinate rispetto
agli articoli tramite la funzione sorted(). Esempi
FILE infile
martello,12,1
bullone,13
vite,1,2
martello,1,23
vite,28

items(infile, outfile)  -->

FILE outfile
bullone:13
martello:37
vite:31

FILE infile
pasta,98,1,2,3,4
pomodori,2
patate,13,2,56
pomodori,67,8
pomodori,12
cicoria,2,3,4,1,6,8,45

items(infile, outfile)  -->

FILE outfile
cicoria:69
pasta:108
patate:71
pomodori:89

'''

def items(infile, outfile):
    diz=dict()
    out_list = []
    
    ingr = open(infile)
    articoli = ingr.readlines()
    l2=[]
    for x in articoli:
        v1= x.replace('\n','')
        v2= v1.split(',')
                  
        for i in range(1,len(v2)) :
            qt =  int(v2[i])
            l1 = [v2[0],qt]
            l2.append(l1)
 
    for l in l2:
            nome=l[0]
            val=l[1]
 
            if nome in diz:
                diz[nome]+=val
            else:
                diz[nome]=val

    for y in sorted(diz.keys()):
        out_file = open(outfile,'a')
        k = [y,':',diz[y]]
        out_string = str(k[0]) + str(k[1]) + str(k[2]) +"\n"
        out_file.write(out_string)
        out_file.close()
