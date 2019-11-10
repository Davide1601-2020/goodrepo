import os
while True:
    print('''Benvenuto nell\'assistente virtuale per Linux.
    Creato da: Davide Visca.
    Versione 1.0
    Copyright 2019-2020
    *************************************************
    Scrivere "aiuto" per avere più informazioni''')
    dialogo = str(input("Cosa posso fare per te?:"))
    if dialogo == "Ciao" or dialogo == "ciao":
        print("Ciao!")
    elif dialogo == "Esegui un comando" or dialogo == "esegui un comando":
        comando = str(input("che comando vuoi eseguire?: "))
        os.system(comando)
    elif dialogo == "Come va?" or dialogo == "come va?":
        print("Tutto bene, te?")
        loop = input("Tutto bene?: ")
        if loop == "Si" or loop == "si":
            print("Ottimo!")
        elif loop == "No" or loop == "no":
            print("Mi dispiace")
    elif dialogo == "Apri un programma" or dialogo == "apri un programma":
        comando = str(input("Che programma vuoi eseguire?: "))
        os.system(comando)
    elif dialogo == "Aiuto" or dialogo == "aiuto":
        print('''Ecco i comandi disponibili attualmente:
        (si possono scrivere con o senza lettera maiuscola)
        -Ciao
        -Come va?
        -Esegui un comando
        -Apri un programma
        **************************************************************
        Presto arriveranno nuovi comandi.''')
        
    
    