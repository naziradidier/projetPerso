0from random import randint
nbMyster = randint(0, 100)
attempt = 2
i = 0


phrase = False
phrase2 = False
point_first_user = 0
point_second_user = 0

while i < attempt:
    # user1
    print("-------------- *** Au tours de user 1 de jouer *** ----------------\n")
    essaie = 10
    while essaie > 0:
        userNumber1_int = None
        while userNumber1_int is None:
            userNumber1_str = input("""Entrer un nombre
>>> """)
            try:
                userNumber1_int = int(userNumber1_str)
            except ValueError:
                print("Erreur !!! Veuillez entrer un nombre...!!!")

        if nbMyster < userNumber1_int:
            print("Diminuez votre nombre s'il vous plait!!!!")
            print("il vous reste ", essaie - 1, " essai!!!!")
        elif nbMyster > userNumber1_int:
            print("augmenter un tout petit peu!!!!")
            print("il vous reste ", essaie - 1, " essai!!!!")
        else:
            phrase = True
            point_first_user = point_first_user + 1
            break
        print()
        essaie -= 1
    if phrase:
        print("bravo, t'as gagné")
        print(f'Voici votre point {point_first_user}.')
    else:
        print("...Game over...")
        print(f'Voici votre point {point_first_user}.')

    print("\n------------------------------- *** -----------------------------------\n")

    # user2
    print("---------------- *** Au tours de user 2 de jouer *** ----------------\n")
    essaie2 = 10
    while essaie2 > 0:
        userNumber2_int = None
        while userNumber2_int is None:
            userNumber2_str = input("""Entrer un nombre
>>> """)
            try:
                userNumber2_int = int(userNumber2_str)
            except ValueError:
                print("Erreur !!! Veuillez entrer un nombre...!!!")
                print()
        if nbMyster < userNumber2_int:
            print("Diminuez votre nombre s'il vous plait!!!!")
            print("il vous reste ", essaie2 - 1, " essai!!!!")
        elif nbMyster > userNumber2_int:
            print("Augmenter un tout petit peu!!!!")
            print("il vous reste ", essaie2 - 1, " essai!!!!")
        else:
            phrase2 = True
            point_second_user = point_second_user + 1
            break
        essaie2 -= 1
        print()
    print()
    if phrase2:
        print("bravo, t'as gagné")
        print(f'Voici votre point {point_second_user}')
    else:
        print("...Game over...")
        print(f'Voici votre point {point_second_user}')

    i = i+1
    print()
    print("------- *** le score: user1 = ", point_first_user, "le score: user2 = ", point_second_user)

    print("\n\n-------------------------#########-----------------------\n\n")
    rejouer = input("""voulez-vous rejouer? OUI/NON
>>> """)
    if rejouer == "OUI":
        i = 0
    else:
        exit(0)
