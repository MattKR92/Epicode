import math

opzioni= ["1-Quadrato", "2-Cerchio", "3-Rettangolo"]

print("Ciao! Sono il tuo calcolatore di perimetri!")
print("Indicami con il numero corrispondente la figura di cui vuoi calcolare il perimetro")

while True:
    print("Ecco le opzioni a tua disposizione:")
    for opzione_disponibile in opzioni:
        print(opzione_disponibile)
    
    scelta_user= int(input())

    if scelta_user == 1:
        print("Ok, procediamo con il perimetro del quadrato")
        lato= float(input("Inserire la lunghezza del lato: "))
        perimetro_quadrato= float(lato*4)
        print("il perimetro del quadrato è di ", perimetro_quadrato," cm quadrati")
        continue
    elif scelta_user == 2:
        print("Ok, procediamo con la circonferenza del cerchio")
        raggio= float(input("Inserire il valore del raggio: "))
        pi_greco= 3.14
        perimetro_cerchio= float(2*(pi_greco*raggio))
        print("La circonferenza del cerchio è di ", perimetro_cerchio, " cm quadrati")
        continue
    elif scelta_user == 3:
        print("ok, procediamo con il perimetro del rettangolo")
        base= float(input("Inserire il valore della base: "))
        altezza= float(input("Inserire il valore dell'altezza: "))
        perimetro_rettangolo= float((base*2)+(altezza*2))
        print("Il perimetro del rettangolo è di ", perimetro_rettangolo, " cm quadrati")
        continue
    else:
        print("Opzione inesistente. Inserire una opione valida")
        continue



