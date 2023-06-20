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
liste = []
while True :
    print("Choisissez parmis les options suivantes : ")
    print("1-AJOUTER UN ELEMENT DE DANS LA LISTE")
    print("2-RETIER UN ELEMENT DANS LA LISTE")
    print("3-AFFICHER LA LISTE")
    print("4-VIDER LA LISTE")
    print("5-QUITTER")

    option = input("Votre choix --> ")

    if option == "1" or option == "2":

        element = input("entrer le nom de l'element : ")
        element = element.capitalize()

        if element in liste :
            if  option =="1":
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
        else :
            if option == "3":
                i = 1
                for element in liste :
                    print(f"{i}. {element}")
                    i+= 1
            else:
                liste.clear()
                print("la liste a bien ete vider de son contenue")

    elif option == "5":
        print("A bientot !")
        break

    else:
        print("VOTRE CHOIX N'EXISTE PAS RECHOISISSEZ !")
    print("-----------------------------------------------------------")