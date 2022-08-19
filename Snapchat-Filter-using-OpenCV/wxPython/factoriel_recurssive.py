def factoriel_recursive(nbUser):
    fact = 1
    if nbUser == 0:
        return 1
    elif nbUser == 1:
        return 1
    else:
        return nbUser*factoriel_recursive(nbUser-1)
    #fonction recurssive le fonctio iany miantso ny tenany, ao anaty fonction iany miantso anle fonction

if __name__=="__main__":
    nbUser = int(input("entrer un nombre : "))
    fact = factoriel_recursive(nbUser)
    print(nbUser, "!=", fact)