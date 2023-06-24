# jeux comporte deux joueurs: un user et un ennemi
# il commemce avec 50 points de vie
# user dispose de 3 potions qui donne entre 15 et 50 point de vie de plus
# l'attaque de user inflige des degats compris entre 5 et 10
# l'attaque de l'ennemi inflige des degats compris entre 5 et 15
# passer au prochain tour si user utilise une potion
# deroulement
"""
    DEMANDER A USER : Souhaitez-vous attaquer(1) ou utiliser une potion (2):
        si user choisit 1:
            afficher: vous avez infliger x point de degats a l'ennemi
        si user choiait 2:
            verifier si il reste des potions a user si oui
                afficher: vous avez recuperer x point de vie (x potion restant)
                passer a la toure suivante:
                afficher: vous passez votre tour
            sinon:
                afficher: vous n'avez plus de potion et redemandera user de rechoisir
        afficher: l'ennemi vous a infliger x point de degat
        afficher: le nombre de point de vie qui reste pour chaque joueur
    afficher qui a gagner et fin du jeux
"""
from random import randint
user_life = 50
bot_life = 50
potion = 3

while True:

    user_choice = ""
    if user_choice not in ["1", "2"]:
        user_choice = input("Souhaitez-vous attaquer(1) ou utiliser une potion (2): ")

    skip_turn = False
    if user_choice == "1":
        user_dammage = randint(5, 10)
        bot_life -= user_dammage
        print(f"vous avez infliger {user_dammage} points de degat a l'ennemi")
    else:
        if potion > 0:
            get_life = randint(15, 50)
            user_life += get_life
            potion -= 1
            print(f"vous avez recuperer {get_life} points de vie ({potion} restant)")
            skip_turn = True
        else:
            print("vous n'avez plus de potion")

    if skip_turn:
        print("vous passez le tour")
        bot_dammage = randint(5, 15)
        user_life -= bot_dammage
        print(f"l'ennemi vous a infliger {bot_dammage} point de degat")
        print(f"il vous reste {user_life} point de vie")

    bot_dammage = randint(5, 15)
    user_life -= bot_dammage
    print(f"l'ennemi vous a infliger {bot_dammage} point de vie")

    if user_life <= 0:
        print("vous avez perdu")
        break
    elif bot_life <= 0:
        print("vous avez gagne")
        break
    else:
        print(f"il vous reste {user_life} point de vie\nil reste {bot_life} point de vie a l'ennemi")

print("fin du jeux")




