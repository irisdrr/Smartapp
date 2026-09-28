# Smartapp controler sprint 2

def maak_input_bestand():
    bestand = open('bestand.txt', "w")

    temperatuurverschil = setpoint - buitentemperatuur


#ketel
    if temperatuurverschil >= 20:
        cv_ketel = 100
    elif temperatuurverschil >= 10:
        cv_ketel = 50
    else:
        cv_ketel = 0
#ventilatie
ventilatie = aantal_personen + 1

if ventilatie > 4:
    ventilatie = 4

#bewatering
if neerslag < 3:
                bewatering = True
            else:
                bewatering = False

bestand.write
    (f"{datum};{cv_ketel};{ventilatie};{bewatering}\n")



def aantal_dagen(inputFile):


    with open(inputFile, "r") as bestand:
        regels = bestand.readlines()


def auto_bereken(inputFile, outputFile):
    with open(inputFile, "r") as bestand:
        regels = bestand.readlines()

    with open(outputFile, "w") as bestand:

def overwrite_settings(outputFile):


def smart_app_controller():
    print("1. Hoeveel dagen zijn er aanwezig?")
    print("2. Automatisch alle actuatoren berekenen")
    print("3. Een waarde overschrijven")
    print("4. Stoppen")

keuze = input("Maak een keuze: ")

