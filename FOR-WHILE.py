# la boucle for permet de faire une iteration
print("---------------bouble for-------------------")
liste = [1, 2, 3]
for i in liste:
    print(i)

#oubien
print("---------------boucle for oubien-------------------")
for i in range(4):
    print(i)

# la boucle while permet de repeter un action une certaine nombre de fois
print("---------------bouble while-------------------")
i = 0
while i < 4:
    print(i)
    i += 1

# l'instruction  continu passe directement a prochaine iteration sans executer le code qui suit
# afficher seulement les nom
print("----------------l'instruction  continu------------------")
liste = ["1", "2", "3", "Toto", "Tata", "4", "Paul"]
for element in liste:
    if element.isdigit():
        # l'iteration continue  si element.isdigit() sans executer le reste du code 
        # sinon elle affiche le element avec le print
        continue

    print(element)

# l'instruction  break arrete directement l'execution de la boucle 
print("----------------l'instruction break------------------")

for element in liste:
    if element.isdigit():
        print("arret du boucle")
        break
    print(element)

# les comprehensions de listes : list comprehension
"""
liste = ["1", "2", "3", "Toto", "Tata", "4", "Paul"]
for i in liste:
    if not i.isdigit():
        liste_name = liste.append(i)
        """
#code ci dessus equivaut a:
print("--------------------list comprehension------------------")
liste = ["1", "2", "3", "Toto", "Tata", "4", "Paul"]
# on ajoute i a la liste_name pour i venant de liste si i.isdigit()
liste_name = [i for i in liste if not i.isdigit()]
print(liste_name)

# afficher les mot d'une chaine de caractere a l'envers
#la fonction reverse permet d'inverser une chaine de carctere
mot = "python"
for i in reversed(mot):
    print(i)

# sortir d'une boucle while si user le souhaite

continuer = "o"
while continuer == "o":
    continuer = input("voulez-vous continuer (o/n)")
    if not continuer == "o":
        continue
    print("on continue")


#addition de deux nombres
#premiere methode 
"""
while True:
    nombre_1 = input("entrer le 1er nombre ")
    nombre_2 = input("entrer le 2em nombre ")
    try:
        nombre_1 = int(nombre_1)
        nombre_2 = int(nombre_2)
    except:
        print("veillez entrer deux nombres valides")
    else :
        print(f"La somme de {nombre_1} et de {nombre_2} est {nombre_1+nombre_2}")
        break
"""
#methode recommander
while True:
    a = input("entrer le 1er nombre ")
    b = input("entrer le 2em nombre ")
    if a.isdigit() and b.isdigit():
        print(f"la somme de {a} et de {b} est: {int(a)+int(b)}")
        break
    print("Veiller entrer deux nombres valides")
else:
    print("FIN")
