def eleve_info():
    for i in range(3):
        fichier = open("eleve.txt","a")
        Nom = input("Taper votre Nom: ")
        Prenom = input("Taper votre Prenom: ")
        age = input("Taper votre age: ")
        classe = input("Taper votre classe: ")
        fichier.writelines(f"{Nom},{Prenom},{age} an,{classe}Annee\n")
        print(fichier)
        fichier.close
def lire_fichier():
    fichier = open("eleve.txt","r")
    contenue = fichier.readlines()
    for eleve in contenue:
        code = eleve.split(",")
        print(f"Nom de l'eleve: {code[0]}\nprenom:{code[1]}\nage de l'eleve: {code[2]}\nclasse: {code[3]}\n")
    fichier.close()    
    
lire_fichier()
eleve_info()   
                
