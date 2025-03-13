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
while weiter:
    op = input("Welche Operation möchtest du ausführen? (+, -, *, / ,** ,%) oder exit:")
    if op.lower() == 'exit':
        print('Code wird beendet!')
        break
    try:
        # Testen der Funktion
        zahl1 = float(input("Gib die erste Zahl ein: "))
        zahl2 = float(input("Gib die zweite Zahl ein: "))
    except ValueError:
        print("Erneut versuchen!")
        continue


    ergebnis = taschenrechner(zahl1, zahl2, op)
    print("Ergebnis:", ergebnis)
    frage = input("Willst du weiter machen?: ")
        
    if frage != "ja":
        weiter=False 
    
    mach = input('Mit dem gleichen Wert?')
while True:
    if mach == 'ja'.lower:
        ergebnis + op + zahl2