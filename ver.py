# identifiant= "sekou"
# mot_de_passe = "sekou3807"

# print("interface de Connnexion")
# user_id = input("Taper votre identifient: ")
# user_pass = input("Entrer votre mot de passe: ")
# if user_id==identifiant and user_pass==mot_de_passe:
#     print("vous etes connecter, Bienvenue: ",user_id, user_pass)
# else:
#     print("pas connecter")
# jeu_lance =True

# while jeu_lance:
#     choixMenu=input("> ")
#     if choixMenu=="again":
#         continue
#     elif choixMenu=="quit":
#         jeu_lance=False
#     elif choixMenu=="helo":
#          print("bienvenue")
#     else:
#         print("comande introuvable")   
# print("A bientot")
a, b, c = 3, 2, 1
while c < 15:
    print(c, ": ", b)
    a, b, c = b, a*b, c+1
        