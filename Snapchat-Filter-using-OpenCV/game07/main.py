from random import randint

fichier = open("data.txt")
data = fichier.readlines()
line = randint(0, len(data)-1)
word = data[line]
wordL = list(word)
wordL.pop()
# print(wordL)
f_star = randint(0, int(len(wordL)/2))
s_star = randint(int(len(wordL)/2)+1, int(len(wordL)-1))
# print(f_middle_word_len)
# print(s_middle_word_len)
wordL[f_star] = "*"
wordL[s_star] = "*"
wordLS = ''.join([item for item in wordL])
try:
    userInput = input("gess this word : {} \n ".format(wordLS))
    userInput= list(userInput)
    userInput = ''.join([item for item in userInput])

    if userInput + "\n" == word:
        print("good you found it!!!!")
        resp = input("""voulez-vous rejouer? OUI/NON
                >>> """)
        if resp == "OUI":
            i = 0
        else:
            exit(0)
    else:
        print("sorry, you failled!!!!")
    resp = input("""voulez-vous rejouer? OUI/NON
        >>> """)
    if resp == "OUI":
        i = 0
    else:
        exit(0)
except:
    print("there is error in this code")
finally:
    fichier.close()