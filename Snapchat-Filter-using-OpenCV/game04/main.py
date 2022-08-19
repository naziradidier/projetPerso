
# -*- coding: utf-8 -*-
from random import randint

fichier = open("data.txt", "r")
"""atao "r" raha lire, atao "w" rah anoratra, atao "a" rah anoratra am farany soratra ao am fichier"""
data = fichier.readlines()
resp = "oui"
level = 1
while resp == "oui":
    point = 0
    while level == 1:
        line = randint(0, len(data) - 31)
        niveau1 = []
        print("------------------------niveau 1------------------------")
        if line in niveau1:
            break
        else:
            print(data[line])
            """data = fichier.readline() --> rah 
            otra te amaky une line fotsiny readline() atao ,data = fichier.readlines() --> ataony 
            liste rah misy s am line"""
            userResp = input("Ta reponse : \n")
            if line == 0 and userResp.__eq__("lune") or line == 0 and userResp.__eq__("LUNE"):
                print("you are right")
                point += 1
                niveau1.append(line)
            elif line == 1 and userResp.__eq__("terre") or line == 1 and userResp.__eq__("TERRE"):
                print("you are right")
                point += 1
                niveau1.append(line)
            elif line == 2 and userResp.__eq__("pluton") or line == 2 and userResp.__eq__("PLUTON"):
                print("you are right")
                point += 1
                niveau1.append(line)
            elif line == 3 and userResp.__eq__("pense") or line == 3 and userResp.__eq__("PENSE"):
                print("you are right")
                point += 1
                niveau1.append(line)
            elif line == 4 and userResp.__eq__("C'est mon oncle") or line == 4 and userResp.__eq__("mon oncle"):
                print("you are right")
                point += 1
                niveau1.append(line)
            elif line == 5 and userResp.__eq__("La montagne") or line == 5 and userResp.__eq__("montagne"):
                print("you are right")
                point += 1
                niveau1.append(line)
            elif line == 6 and userResp.__eq__(
                    "Le e, en la retournant on obtient le 'u'") or line == 6 and userResp.__eq__("Le e"):
                print("you are right")
                point += 1
                niveau1.append(line)
            else:
                print("you are wrong")
            if point == 7:
                level = 2
                point = 0
    while level == 2:
        line = randint(7, len(data) - 24)
        print("------------------------niveau 2------------------------")
        print(data[line])
        userResp = input("Ta reponse : \n")

        if line == 7 and userResp.__eq__("Le nez") or line == 7 and userResp.__eq__("le futur"):
            print("you are right")
            point += 1
        elif line == 8 and userResp.__eq__("Ils pèsent les deux un kilo") or line == 8 and userResp.__eq__("un kilo"):
            print("you are right")
            point += 1
        elif line == 9 and userResp.__eq__("Jean est quatrième fils") or line == 9 and userResp.__eq__("Jean"):
            print("you are right")
            point += 1
        elif line == 10 and userResp.__eq__(
                "Les trains électriques ne projettent pas de fumée") or line == 10 and userResp.__eq__(
                "Les trains électriques n'a pas de fumée"):
            print("you are right")
            point += 1
        elif line == 11 and userResp.__eq__("Les escaliers") or line == 11 and userResp.__eq__("escaliers"):
            print("you are right")
            point += 1
        elif line == 12 and userResp.__eq__(
                "C'est vrai, car four commence par F et termine par T ") or line == 12 and userResp.__eq__(
            "C'est vrai"):
            print("you are right")
            point += 1
        elif line == 13 and userResp.__eq__(" Tous les mois ont 28 jours") or line == 13 and userResp.__eq__(
                "Tous les mois"):
            print("you are right")
            point += 1
        else:
            print("you are wrong")
        if point == 7:
            level = 3
            point = 0
    while level == 3:
        line = randint(14, len(data) - 17)
        print("------------------------niveau 3------------------------")
        print(data[line])
        userResp = input("Ta reponse : \n")

        if line == 14 and userResp.__eq__("Le n") or line == 14 and userResp.__eq__("n"):
            print("you are right")
            point += 1
        elif line == 15 and userResp.__eq__("Une heure") or line == 15 and userResp.__eq__("Une heure"):
            print("you are right")
            point += 1
        elif line == 16 and userResp.__eq__("pense") or line == 16 and userResp.__eq__("PENSE"):
            print("you are right")
            point += 1
        elif line == 17 and userResp.__eq__("Le feu") or line == 17 and userResp.__eq__("feu"):
            print("you are right")
            point += 1
        elif line == 18 and userResp.__eq__("Un œuf") or line == 18 and userResp.__eq__("œuf"):
            print("you are right")
            point += 1
        elif line == 19 and userResp.__eq__(
                "Il y avait le père, son fils, et le fils de son fils. Cela fait donc 2 pères et 2 fils pour un total de 3 personnes !"):
            print("you are right")
            point += 1
        elif line == 20 and userResp.__eq__("Une grippe") or line == 20 and userResp.__eq__("grippe"):
            print("you are right")
            point += 1
        else:
            print("you are wrong")
        if point == 7:
            level = 4
            point = 0
    while level == 4:
        line = randint(21, len(data) - 10)
        print("------------------------niveau 4------------------------")
        print(data[line])
        userResp = input("Ta reponse : \n")

        if line == 21 and userResp.__eq__("Ton prénom") or line == 21 and userResp.__eq__("prénom"):
            print("you are right")
            point += 1
        elif line == 22 and userResp.__eq__("Le mot MAL") or line == 22 and userResp.__eq__("MAL"):
            print("you are right")
            point += 1
        elif line == 23 and userResp.__eq__(
                "Tu termines la course à la 2ème place") or line == 23 and userResp.__eq__(
            "2ème place"):
            print("you are right")
            point += 1
        elif line == 24 and userResp.__eq__(
                "Son frère a 10 ans. La moitié de 8 est égale à 4, donc le frère de Jean a 4 ans de moins. Cela signifie que lorsque Jean aura 14 ans, son frère aura toujours 4 ans de moins, et qu'il aura donc 10 ans") or line == 24 and userResp.__eq__(
            "10"):
            print("you are right")
            point += 1
        elif line == 25 and userResp.__eq__("Une éponge") or line == 25 and userResp.__eq__("éponge"):
            print("you are right")
            point += 1
        elif line == 26 and userResp.__eq__("Es-tu endormi ?") or line == 26 and userResp.__eq__("tu dors?"):
            print("you are right")
            point += 1
        elif line == 27 and userResp.__eq__("Le futur") or line == 27 and userResp.__eq__("futur"):
            print("you are right")
            point += 1
        else:
            print("you are wrong")
        if point == 7:
            level = 4
            point = 0
    while level == 4:
        line = randint(28, len(data) - 3)
        print("------------------------niveau 5------------------------")
        print(data[line])
        userResp = input("Ta reponse : \n")

        if line == 28 and userResp.__eq__("Ton âge") or line == 28 and userResp.__eq__("âge"):
            print("you are right")
            point += 1
        elif line == 29 and userResp.__eq__("Il marchait, il ne conduisait pas"):
            print("you are right")
            point += 1
        elif line == 30 and userResp.__eq__("En ramenant une chaise"):
            print("you are right")
            point += 1
        elif line == 31 and userResp.__eq__(
                "Tu as 2 pommes. Tu as récupéré 2 pommes et en as laissé 1 dans le panier") or line == 31 and userResp.__eq__(
            "Tu as 2 pommes"):
            print("you are right")
            point += 1
        elif line == 32 and userResp.__eq__("Une serviette") or line == 32 and userResp.__eq__("serviette"):
            print("you are right")
            point += 1
        elif line == 33 and userResp.__eq__("David"):
            print("you are right")
            point += 1
        elif line == 34 and userResp.__eq__("La lettre R") or line == 34 and userResp.__eq__("R"):
            print("you are right")
            point += 1

    while level == 5:
        line = randint(35, len(data))
        print("niveau 5")
        print(data[line])
        userResp = input("Ta reponse : \n")

        if line == 35 and userResp.__eq__("Du popcorn") or line == 35 and userResp.__eq__("popcorn"):
            print("you are right")
            point += 1
        elif line == 36 and userResp.__eq__("La respiration") or line == 36 and userResp.__eq__("respiration"):
            print("you are right")
            point += 1
        elif line == 37 and userResp.__eq__("Une fenêtre") or line == 37 and userResp.__eq__("fenêtre"):
            print("you are right")
            point += 1
        else:
            print("you are wrong")
fichier.close()
