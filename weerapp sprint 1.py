
# SMART APP SPRINT 1: WEERSTATION

# Celsius naar Fahrenheit

def Fahrenheit(temp_celcius):
    return 32 + 1.8 * temp_celcius




# Gevoelstemperatuurrrrr


def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return temp_celcius - (luchtvochtigheid / 100) * windsnelheid



# Weerrapport bepalen

def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):

    # de gevoelstemperatuur berekenenen
    gevoel = gevoelstemperatuur( temp_celcius,windsnelheid,luchtvochtigheid)


    if gevoel < 0 and windsnelheid > 10:
        return "Het is ijskoud en het stormt! Verwarming helemaal aan!"

    elif gevoel < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"

    elif gevoel >= 0 and gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait, verwarming aan en roosters dicht!"

    elif gevoel >= 0 and gevoel < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"

    elif gevoel >= 10 and gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm"

    # andere gevalen
    else:
        return "Kapot warm! Airco aan!"



# FUNCTIE   4

def weerstation():

    temperaturen = []

    for dag in range(1, 7):

        temp_input = input(
            f"Wat is op dag {dag} de temperatuur[C]: ")

        if temp_input == "":
            print("bye")

        if temperatuur < 0 or temperatuur > 50:
            print("Ongeldige vochtigheid. Voer een waarde van 0 t/m 100 in.")
            continue


        # temperatuur om te zetten naar een getal
        try:
            temperatuur = float(temp_input)

            # Windsnelheid vragen
            windsnelheid_input = input(
                f"Wat is op dag {dag} de windsnelheid[m/s]: ")

            # Als de gebruiker niets invult: stoppen
            if windsnelheid_input == "":
                print("bye")
                break

            windsnelheid = float(windsnelheid_input)

            # Luchtvochtigheid vragen
            luchtvochtigheid_input = input(
                f"Wat is op dag {dag} de vochtigheid[%]: ")

            # Als de gebruiker niets invult: stoppen
            if luchtvochtigheid_input == "":
                print("bye")
                break

            luchtvochtigheid = int(luchtvochtigheid_input)


            if luchtvochtigheid < 0 or luchtvochtigheid > 100:
                print("Ongeldige vochtigheid. Voer een waarde van 0 t/m 100 in.")
                continue

        # erroorororro bij foute invoer
        except ValueError:
            print("Ongeldige invoer. Voer een getal in.")
            continue


        temperaturen.append(temperatuur)
        fahrenheit = Fahrenheit(temperatuur)
        rapport = weerrapport( temperatuur, windsnelheid,luchtvochtigheid)



        # gemiddelde temperatuur
        gemiddelde = sum(temperaturen) / len(temperaturen)

        # Resultaat of the dayyy

        print(f"Het is {temperatuur}C ({fahrenheit}F)")
        print(rapport)
        print("Gemiddelde temp tot nu toe is:", gemiddelde)

        print("======================================")







weerstation()