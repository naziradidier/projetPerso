class Etudiant:
    count = 0
    def __init__(self):

        self.nom = "nazirah"
        self.prenom = "didier"
        self.age = 10
        self.gender = "masculin"
    #methode de l'objet
    def inscrire(self, name, f_name, age, gender):
        self.nom = name
        self.prenom = f_name
        self.age = age
        self.gender = gender
    def visualiser_certificat_scolarite(self):
        return "nom : "+ self.nom + ", prenom :" + self.prenom + ",age : " + str(self.age) + " , genre : " + self.gender
    def compter_objet_creer(cls):
        Etudiant.count = Etudiant.count+1
        return  Etudiant.count

et1 = Etudiant()
etlist[]
nbEt = int(input("combien etudiant voulez vous faire une inscription"))
i=0
while i < nbEt:
    nomEt = input("Entrer le nom de cet etudiant : ")
    prenomEt = input("Entrer le prenom de cet etudiant : ")
    ageEt = int(input("Entrer le age de cet etudiant : "))
    genderEt = input("Entrer le genre de cet etudiant : ")
    etdict = {
        "nomEt": nomEt,
        "prenomEt": prenomEt,
        "ageEt" : ageEt,
        "genderEt": genderEt
    }

et1.inscrire(etdict["nomEt"], etdict["prenomEt"], etdict["etdict"], etdict["genderEt"])
print(et1.visualiser_certificat_scolarite())

et2 = Etudiant()
print("on a créer : ", et2.compter_objet_creer(), "etudiants")