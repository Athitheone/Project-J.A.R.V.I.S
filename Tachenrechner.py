while True:
    try:
        zahl1 = float(input("Gib die erste Zahl ein: "))
        zahl2 = float(input("Gib die zweite Zahl ein: "))
    except ValueError:  # Falls der Benutzer Text eingibt statt einer Zahl
        print("Fehler: Bitte gib gültige Zahlen ein!")
        continue  # Springt zurück zum Start der Schleife

    operator = input("Wähle eine Rechenart (+, -, *, /) oder 'exit' zum Beenden: ")

    if operator == "exit":
        print("Taschenrechner wird beendet. Auf Wiedersehen!")
        break

    if operator == "+":
        ergebnis = zahl1 + zahl2
    elif operator == "-":
        ergebnis = zahl1 - zahl2
    elif operator == "*":
        ergebnis = zahl1 * zahl2
    elif operator == "/":
        if zahl2 != 0:
            ergebnis = zahl1 / zahl2
        else:
            ergebnis = "Fehler: Division durch Null ist nicht erlaubt!"
    else:
        ergebnis = "Ungültiger Operator!"

    print("Ergebnis:", ergebnis)

