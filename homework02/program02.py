'''
Ritorna un dizionario che combina il dizionario di input addr, che
contiene associazioni nome-indirizzo, e il dizionario phone, che contiene
associazioni nome-telefono. Il dizionario ritornato ad ogni nome N
in uno dei due dizionari associa un dizionario che contiene la chiave
'address' con valore l'indirizzo di N in addr (se presente in addr) e
la chiave 'phone' con valore il telefono di N in phone (se presente in
phone). La funzione non deve fare nessun controllo sui valori presenti
nei dizionari. Esempi

addr = {'Giorgio': 'via Verdi, 23', 'M. Bianchi': 'Piazza Milano, 1',
        'L. De La': 'via A. Einstein, 12', 'Ciro': 'via Pio'}
phone = {'Marco': '347 8987989', 'giorgio': '06 89786765',
         'Mauro B.': '3489878675', 'Ciro': '07897878', 'L. De La': '09877887'}

addr_phone(addr, phone) -->
    {'Giorgio':    {'address': 'via Verdi, 23'},
     'Marco':      {'phone': '347 8987989'},
     'giorgio':    {'phone': '06 89786765'},
     'L. De La':   {'phone': '09877887', 'address': 'via A. Einstein, 12'},
     'Ciro':       {'phone': '07897878', 'address': 'via Pio'},
     'Mauro B.':   {'phone': '3489878675'},
     'M. Bianchi': {'address': 'Piazza Milano, 1'}}


addr = {'blue': 'place', 'white': 'boh', 'BLACK': '1234', 'red': 'street'}
phone = {'blue': 'number', 'gray': 'Num', 'red': 'Phone', 'Red': 'TEL'}

addr_phone(addr, phone) -->
    {'blue':  {'phone': 'number', 'address': 'place'},
     'gray':  {'phone': 'Num'},
     'BLACK': {'address': '1234'},
     'red':   {'phone': 'Phone', 'address': 'street'},
     'white': {'address': 'boh'},
     'Red':   {'phone': 'TEL'}}
'''

def addr_phone(addr, phone):
        addr_phone = dict()
        d = dict()

        for nome, indirizzo in addr.items():
            d['address'] = indirizzo
            addr_phone[nome] = d
            d = {}
           
        for nome, numero in phone.items():
            if (nome in addr_phone):
                 addr_phone[nome] = {'phone': phone[nome],'address':addr[nome]}
            else:
                 d['phone'] = numero
                 addr_phone[nome] = d
                 d = {}
       
        return addr_phone
