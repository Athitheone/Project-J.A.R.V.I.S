def taschenrechner(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Fehler: Division durch 0!"
        return a / b
    elif operation == "**":
        return a ** b
    elif operation == "%":
        return a % b
    else:
        return "Ungültige Operation!"
weiter= True
ergebnis = 0
while weiter:
    op = input("Welche Operation möchtest du ausführen? (+, -, *, / ,** ,%) oder exit:")
    if op.lower() == 'exit':
        print('Code wird beendet!')
        break
    try:
        if ergebnis == 0:
                    zahl1 = float(input("Gib die erste Zahl ein: "))
                    zahl2 = float(input("Gib die zweite Zahl ein: "))
        else:
            zahl1 = ergebnis
            zahl2 = float(input("Gib die zweite Zahl ein: "))
    except ValueError:
        print("Erneut versuchen!")
        continue


    ergebnis = taschenrechner(zahl1, zahl2, op)
    print("Ergebnis:", ergebnis)
    frage = input("Willst du weiter machen? (ja/nein): ").lower()
    
    if frage != 'ja'.lower():
        weiter = False  
    else:
        frage2 = input('Mit demselben Wert? (ja/nein): ')
    if frage2 != 'ja'.lower():
        ergebnis = 0