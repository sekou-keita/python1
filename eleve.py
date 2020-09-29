def eleve_info():
    for i in range(3):
        Nom = input("Taper votre Nom: ")
        Prenom = input("Taper votre Prenom: ")
        age = input("Taper votre age: ")
        classe = input("Taper votre classe: ")
        fichier = open("eleve.txt","a")
        fichier.writelines(f"{Nom} {Prenom} {age} an , classe:{classe} Annee \n")
        print(fichier)
        fichier.close
eleve_info()