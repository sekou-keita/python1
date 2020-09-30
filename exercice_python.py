def eleve_info():
    for i in range(3):
        fichier = open("elev.txt","a")
        Nom = input("Taper votre Nom: ")
        Prenom = input("Taper votre Prenom: ")
        age = input("Taper votre age: ")
        classe = input("Taper votre classe: ")
        fichier.writelines(f"{Nom} {Prenom} {age} an , classe_eleve:{classe} Annee \n")
        print(fichier)
        fichier.close
def lire_fichier():
    fichier = open("elev.txt","r")
    contenue = fichier.readlines()
    for eleve in contenue:
        code = eleve.split(" ")
        print(f"Nom_l'evele: {code[1]}\nPrenom_l'eleve: {code[0]}\nage de l'eleve: {code[2]} {code[3]}\n{code[5]} {code[6]}")
       
    fichier.close()    
    
lire_fichier()
eleve_info()   
                
