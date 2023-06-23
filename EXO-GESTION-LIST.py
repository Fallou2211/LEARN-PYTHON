# GESTION DE LISTE MA LISTE
"""
OPTION: AFICHER TJRS L'OPTION CHOISIT PAR USER
    1-AJOUTER UN ELEMENT DE DANS LA LISTE
        IMPOSSIBLE D'AJOUTER UN ELEMENT DEJA EXISTANT
        SPECIFIER QUE L'ELEMENT X EST AJOUTER
    2-RETIER UN ELEMENT DANS LA LISTE
        IMPOSSIBLE DE RETIRER UN ELEMNT QUI EXISTE PAS
        SPECIFER QUE L'ELEMENT X EST BIEN SUPPRIMER
    3-AFFICHER LA LISTE
        AFFICHER CHAQUE ELEMENT AVEC LE NUMERO EN AVANT 
        DIRE QUE LA LISTE EST VIDE SI ELLE EST VIDE
    4-VIDER LA LISTE
        VIDER LA LISTE SI POSSIBLE
        IMPOSSIBLE DE VIDER LA LISTE SI ELLE EST DEJA VIDE
    5-QUITTER
        A BIENOT !
"""
import sys

liste = []
while True:
    affichage = """Choisissez parmis les options suivantes :
    1-AJOUTER UN ELEMENT DE DANS LA LISTE
    2-RETIER UN ELEMENT DANS LA LISTE
    3-AFFICHER LA LISTE
    4-VIDER LA LISTE
    5-QUITTER
    Votre choix -->  """

    option = input(affichage)

    if option == "1" or option == "2":

        element = input("entrer le nom de l'element : ")
        element = element.capitalize()

        if element in liste:
            if option == "1":
                print(f"l'element {element} exite deja ")

            else:
                liste.remove(element)
                print(f"l'element {element} a bien ete supprimer de la liste")
        else:
            if option == "1":
                liste.append(element)
                print(f"l'element {element} a bien ete ajouter")
            else:
                print(f"l'element {element} n'existe pas")


    elif option == "3" or option == "4":
        if len(liste) == 0:
            print("la liste est vide")
        else:
            if option == "3":
                for i, element in enumerate(liste, 1):
                    print(f"{i}. {element}")
            else:
                liste.clear()
                print("la liste a bien ete vider de son contenue")

    elif option == "5":
        print("A bientot !")
        sys.exit()

    else:
        print("VOTRE CHOIX N'EXISTE PAS RECHOISISSEZ !")
    print("-----------------------------------------------------------")
