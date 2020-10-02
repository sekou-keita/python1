def eleve_info():
    for i in range(3):
        fichier = open("eleve.txt","a")
        Nom = input("Taper votre Nom: ")
        Prenom = input("Taper votre Prenom: ")
        date = input("Taper votre date: ")
        classe = input("Taper votre classe: ")
        fichier.writelines(f"{Nom},{Prenom},{date},{classe} Annee\n")
        print(fichier)
        fichier.close
def lire_fichier():
    fichier = open("eleve.txt","r")
    contenue = fichier.readlines()
    for eleve in contenue:
        nom, prenom, date, classe, = eleve.split(",")
        mois = date.split("/")
        print(f"Nom et Prenom de l'eleve: {nom} {prenom}\nDate de naissance est:{date}\nmoi de naissance est:{mois[1]} mois\nclasse:{classe}")
lire_fichier() 
eleve_info()

                
