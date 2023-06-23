# LE JEU DU NOMVRE MISTERE
# AFFICHER : LE JEUX DU NOMBRE MISTERE
"""
GENERER UN NOMBRE MISTERE ENRTRE 0, ET 100
LE NOMBRE D'ESSAI = 5 :
    AFFICHER LE NOMBRE D'ESSAI RESTE AVANT CHAQUE PARTIE
    DEMANDER A USER DE DEVINER LE NOBRE MISTERE
        VERIFIER SI USER A BIEN ENTRER UN NOMBRE
            SINON AFFICHER VEILLER ENTRER UN NOMBRE VALIDE
        DIRE SI LE NOMBRE ET PLUS GRAND OU PLUS PETIT QUE LE NOMBRE MISTERE
        SI USER TROUVE LE NOMBRE AFFICHER :
            BRAVO LE NOMBRE MISTERE ETAIT BIEN X 
            TU AS TROUVER LE NOMBRE EN Y ESSAI
        SINNON AFFICHER : DOMMAGE VOUS AVEZ PERDU 
            NOMBRE MISTERE ETAIT Y

"""
import random

print("Bienvenue dans le jeux du nombre mistere.")
nombre_mistere = random.randint(0, 100)
nombre_de_essai = 5
while nombre_de_essai > 0 :
    print(nombre_mistere)
    print(f"Il te reste {nombre_de_essai} essai{'s' if nombre_de_essai > 1 else ''}")
    user_choice = input("Deviner le nombre : ")

    if not user_choice.isdigit():
        print("Veiller entrer un choix valide")
        continue

    user_choice = int(user_choice)

    if user_choice < nombre_mistere:
        print(f"le nombre mistere est plus grand")
    elif user_choice > nombre_mistere:
        print("le nombre mistere est plus petit")
    else:
        print(f"bravo le nombre mistere etait bien {nombre_mistere}")
        break
    nombre_de_essai -= 1
      
    print("_"*50)
if nombre_de_essai == 0:
    print(f"Dommage le nombre mistere etait {nombre_mistere}")  
else :
    nombre_de_essai = 6-nombre_de_essai
    print(f"vous avez gagner en {nombre_de_essai} essai{'s'if nombre_de_essai > 1 else ''}")

print("fin du jeux")
