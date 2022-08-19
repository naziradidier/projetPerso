def factoriel_non_recursive(n):
    fact = 1
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        while n > 0:
            fact = fact * n
            n -= 1
        return fact

if __name__=="__main__":
    nbUser = int(input("entrer un nombre : "))
    fact = factoriel_non_recursive(nbUser)
    print(nbUser, "!=", fact)