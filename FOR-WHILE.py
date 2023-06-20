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