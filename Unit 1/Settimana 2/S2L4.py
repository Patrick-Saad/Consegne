import math #per poter fare il calcolo preciso del p greco

#Faccio inserire all'utente quale perimetro vuole calcolare facendo si che il risultato
forma = input ("Inserisci quale perimetro vuoi calcolare ( rettangolo, quadrato, cerchio): ")

# ora usando 'if' e 'elif' faccio si che in base alla scelta del utente il programma 
# richieda il neccessario per calcolare il perimetro della forma geometrica scelta
if forma == "rettangolo":
        base = float(input("Inserisci la base del rettangolo: "))
        altezza = float(input("Inserisci l'altezza del rettangolo: "))
        perimetro_rettangolo = 2 * (base + altezza)
        print("Il perimetro del rettangolo è: ", perimetro_rettangolo)
       
elif forma == "quadrato":
        base = float(input("Inserisci il lato del quadrato: "))
        perimetro_quadrato = 4*(base)
        print("Il perimetro del quadrato è: ",perimetro_quadrato)
        
elif forma == "cerchio":
        raggio = float(input("Inserisci il raggio del cerchio: "))
        perimetro_cerchio = 2 * (math.pi * raggio)
        print("Il perimetro del cerchio è: ",perimetro_cerchio)
       
elif forma != "rettangolo" :
        print("Inserire la richiesta corretta")

# Se il risultato non è nessuno di quelli richiesti stampa "Inserire in minuscolo"
# altrimenti stampa il calcolo del perimetro





