# #exercice1
# liste1 = [19, 4, 13, 18, 24, 39, 6, 1, 79, 100]
# j = 1
# i = 0
# min = liste1[0]
# minpos = 0
# if liste1[i] < min:
#         min = liste1[i]
#         minpos = i
#         tamp = liste1[0]
#         liste1[0] = liste1[i]
#         liste1[i] = tamp
# while i < len(liste1):
#     while j < len(liste1):
#         if liste1[i] > liste1[j]:
#             tamp2 = liste1[j]
#             liste1[j] = liste1[i]
#             liste1[i] = tamp2
#             print(liste1)
#     j = i + 1
#     i = i+1
#
# print(liste1)

import numpy.random


def tri_insertion(l):
    n = len(l)
    ndec = 0
    for n in range(1, n):
        cle = l[n]
        j = n-1
        while j >= 0 and l[j] > cle:
            l[j + 1] = l[j]
            ndec += 1
            j = j-1
        l[j + 1] = cle
    return ndec


def nombre_decalages(n):
    ndec_moy = 0
    p = 100
    for i in range(p):
        liste = numpy.random.randint(0, 3 * n, n)
        ndec_moy += tri_insertion(liste)
    ndec_moy /= p
    return (ndec_moy)


liste_N = [10, 100, 1000, 1000, 2000]
for N in liste_N:
    print(nombre_decalages(N)/N**2)
