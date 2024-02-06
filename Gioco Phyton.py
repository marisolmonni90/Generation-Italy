# prima creiamo le funzioni principali, perchè il codice, viene letto dall'alto verso il basso
# il menu che verrà visualizzato nel terminale è scritto il fondo al sorgente perchè
# richiama le funzione definite in partenza

import datetime #importa la libreria (o moduli/tanti moduli = libreria) python datatime che mi consente di scrivere le date 

# Lista per salvare le attività a cui non assegno nessun valore su cui posso scrivere dentro come un foglio bianco
attivita_list = []

# Funzione per inserire una nuova attività
def inserisci_attivita(): # 0 parametri perchè si utilizzano gli imput 
    titolo = input("Inserisci il titolo dell'attività: ") # variabile stringa 
    descrizione = input("Inserisci una descrizione dell'attività: ")
    data_creazione = datetime.datetime.now() # funzione che mette come data di creazione, oggi
    data_fine = input("Inserisci la data di fine (YYYY-MM-DD): ")
    nuova_attivita = { # variabile di tipo dizionario che ha al suo interno ha una serie di coppie chiave:valore
        'titolo': titolo,# titolo è la variabile che viene assegnata tramite l'input della riga 8 e viene usata come valore della chiave "titolo"
        'descrizione': descrizione, # la descrizione è l'imput della riga 9 etc..
        'data_creazione': data_creazione,
        'data_fine': data_fine,
        'completata': False #false perchè non hai completato le attività
    }
    attivita_list.append(nuova_attivita) #aggiunge alla lista vuota della riga 4 il dizionario nuova attività della riga 12
    print("Attività inserita con successo!")

# Funzione per modificare un'attività, la chiave andrà a sovrascrivere quello che l'utente vuole modificare         
def modifica_attivita(): # 0 parametri perchè si utilizzano gli imput 
    titolo_modifica = input("Inserisci il titolo dell'attività da modificare: ")
    for attivita in attivita_list: # ranged for, è una stuttura che si può utilizzare nelle sequenze, cioè negli oggetti iterabili 
        #per ogni elemento di attivita list che abbiamo riempito precedentemente
        if attivita['titolo'] == titolo_modifica: #se la chiave 'titolo' è ugale alla chiave che ha scritto l'utente
            #attività= è una variabile temporanea che serve per accedere all'elemento della lista
            attivita['titolo'] = input("Nuovo titolo: ") # per indicizzare gli elementi viene utilizzata la chiave 
            attivita['descrizione'] = input("Nuova descrizione: ")
            attivita['data_fine'] = input("Nuova data di fine (YYYY-MM-DD): ")
            print("Attività modificata con successo!")
            return
    print("Attività non trovata.")

# Funzione per cancellare un'attività
def cancella_attivita():
    titolo_cancella = input("Inserisci il titolo dell'attività da cancellare: ")
    for attivita in attivita_list:
        if attivita['titolo'] == titolo_cancella:
            attivita_list.remove(attivita)
            print("Attività cancellata con successo!")
            return
    print("Attività non trovata.")

# Funzione per visualizzare attività (concluse o non concluse)
def visualizza_attivita(concluse=False):
    for attivita in attivita_list:
        if attivita['completata'] == concluse:
            print(f"Titolo: {attivita['titolo']}")
            print(f"Descrizione: {attivita['descrizione']}")
            print(f"Data di creazione: {attivita['data_creazione']}")
            print(f"Data di fine: {attivita['data_fine']}")
            print(f"Completata: {'Sì' if attivita['completata'] else 'No'}")
            print("-------------------------")

# Funzione per contrassegnare un'attività come completata
def segna_attivita_completata():
    titolo_completata = input("Inserisci il titolo dell'attività completata: ")
    for attivita in attivita_list:
        if attivita['titolo'] == titolo_completata:
            attivita['completata'] = True
            print("Attività contrassegnata come completata!")
            return
    print("Attività non trovata.")

# Funzione per cercare attività per titolo o descrizione
def cerca_attivita():
    chiave_ricerca = input("Inserisci il titolo o la descrizione da cercare: ")
    for attivita in attivita_list:
        if chiave_ricerca in attivita['titolo'] or chiave_ricerca in attivita['descrizione']:
            print(f"Titolo: {attivita['titolo']}")
            print(f"Descrizione: {attivita['descrizione']}")
            print(f"Data di creazione: {attivita['data_creazione']}")
            print(f"Data di fine: {attivita['data_fine']}")
            print(f"Completata: {'Sì' if attivita['completata'] else 'No'}")
            print("-------------------------")

# Loop principale dell'applicazione
while True:# è vero e quindi va sempre 
    print("\nMenu:")
    print("1. Inserisci nuova attività")
    print("2. Modifica attività")
    print("3. Cancella attività")
    print("4. Visualizza attività non concluse")
    print("5. Visualizza attività concluse")
    print("6. Contrassegna attività come completate")
    print("7. Cerca attività per titolo o descrizione")
    print("8. Esci")
    
    scelta = input("Seleziona un'opzione: ") #l'input è sempre una stringa

    if scelta == '1': #1 mettiamo come str e non come numero perchè la prende dall'input
        inserisci_attivita()# se la scelta è == 1 allora chiama la funzione inserisci attività
    elif scelta == '2':
        modifica_attivita()
    elif scelta == '3':
        cancella_attivita()
    elif scelta == '4':
        visualizza_attivita(False)
    elif scelta == '5':
        visualizza_attivita(True)
    elif scelta == '6':
        segna_attivita_completata()
    elif scelta == '7':
        cerca_attivita()
    elif scelta == '8':
        break  #mettiamo break perchè altrimenti continueremmo a ciclare 
    else: # se tu schiacci qualsiasi altra cosa diversa dalle possibili scelte il terminale stampa
        print("Scelta non valida. Riprova.")# scelta non valida..
