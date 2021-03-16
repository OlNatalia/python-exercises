def eingabe(message, datatyp="String"):
    a=0
    if(datatyp=="String"):
        a=input(message)
    elif(datatyp=="Int"):
        a=int(input(message))
    elif(datatyp=="Float"):
        a=float(input(message))
    return a


# fahrkarte
def zielort():
    try:     
       ziel = eingabe("Wohin wollen Sie fahren? ")
    except ValueError:     
        print("Falsche Eingabe") 
    return ziel


def hin_und_rueck(preis):
    hinzu = eingabe("Hin und Zurück? (J/N) ")
    if hinzu.upper() == "J":
        print("hnzu preis: ", preis * 2)
        return preis * 2
    print("hnzu preis: ", preis)
    return preis


def bahnkarte(preis):
    baka = eingabe("Haben Sie eine Bahncard 50 oder 25? ","Int")
    if baka == 25:
        preis = preis - (preis * 0.25)
    elif baka == 50:
        preis /= 2
    print("baka preis: ", preis)
    return preis


def ges_preis_berechnen():
    preis = 0
    ziel = zielort().lower()

    if ziel == "berlin":
        preis = 20
    elif ziel == "dresden":
        preis = 15
    elif ziel == "münchen":
        preis = 45

    hinzu_preis = hin_und_rueck(preis)
    baka = bahnkarte(hinzu_preis)
    ges_preis = baka

    print("Ges.Preis beträgt: " + str(ges_preis) + "€")
    return "Ges.Preis beträgt: " + str(ges_preis) + "€"
    # return ges_preis


def bezahlen():
    ges_preis_berechnen()
    is_zahlen = eingabe("Möchten Sie Fahrkarte jetzt bezahlen? (J/N) ")
    if is_zahlen.upper() == "J":
        print("Vielen Dank, bitte entnehmen Sie Ihre Fahrkarte")
    else:
        print("Bis zum nächsten mal")


def main():
    print("Fahrkarten Automat")
    ziel = ""
    baka = 0
    hinzu = 0
    preis = bezahlen()

main()
