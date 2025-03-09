
while True:
    eingabe = input("Du: ").lower()

    if "name" in eingabe:
        print("Meine Name ist J.A.R.V.I.S und ich bin dein persönlicher Assistent.")

    elif "hallo" in eingabe:
        print("Hallo sir, wie kann ich Sie heute helfen?")

    elif "was kannst du" in eingabe:
        print("Ich kann deine Fragen beantworten und dir helfen Sachen zu lernen.")

    elif "wetter" in eingabe:
        print("Ich bin noch nicht so weit entwickelt.")
        print("Ich wurde vorschlagen, dass du dein Wetter App in deinem Handy checkst!(:")

    elif "spät ist" in eingabe:
        print("Ich bin noch nicht so weit entwickelt.")
        print("Du kannst die Uhr in deinem Handy überprüfen!(:")

    elif "witz" in eingabe:
        import random

        witze = (
            "Warum können Skelette so schlecht lügen? Weil man durch sie hindurchsehen kann!",
            "Was macht eine Wolke mit Juckreiz? Sie geht zum Wolkenkratzer!",
            "Warum hat das Fahrrad eine gute Note bekommen? Weil es immer zwei Räder hatte!"
        )
        print("Gerne, Sir. ", random.choice(witze))

    elif "bye" in eingabe:
        print("Goodbye, Sir!")
        break

    else:
        print("ich habe das leider nicht verstanden", end=(str(".")))
        print("Ich bin noch nicht so weit entwickelt.")