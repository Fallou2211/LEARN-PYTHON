##  les listes en python
# creer une liste : name = [value, value...]
favorite_language = ["Python", "flutter"]

# supprimer un element de la liste
favorite_language.remove("flutter")
print(favorite_language)

#ajouter un elemmnt dans la liste 
favorite_language.append("Java")

#ajouter pls elements dans la liste
# la methode extend ne prend qu'une seule argument
favorite_language.extend(["C", "C++"])



print(favorite_language)

#les slices : acceder a une partition de la liste par trances 
liste_users = ["user_2",
               "user_1",
               "user_3",
               "user_4",
               "user_5",
               "user_6",
               "user_7"]

print(liste_users)

# afficher les deux premiers element de la liste en u
#NB la derniere valeurs dans les slices est exclusive
user_1_2 = liste_users[0:2]
print(user_1_2)

#recupper un element sur deux en partant du debut a la fin
print(liste_users[::2])

# inverser l'odre d'une liste
print(liste_users[::-1])

# determiner la position d'un element dans la liste
print(liste_users.index("user_4"))


#compter le nombre de fois qu'un elemement est present dans ma liste
print(liste_users.count("user_1"))

#supprimer un element de la liste a l'aide de son index
supp = liste_users.pop(-1)
print("l'element supprimer est " + supp)
print(liste_users)

#trier une liste 
# avec la methode function sorted : la liste n'est pas directement trieer il faut la recupperer dans une variable

liste_users_triee = sorted(liste_users)
print(liste_users_triee)

# la la methode sort triee la liste directement 
liste_users.sort()
print(liste_users)

#inverser une liste
liste_users.reverse()
print(liste_users)

#les methode sum max et min
liste_num = [1, 2, 3]

print(min(liste_num))
print(max(liste_num))
print(sum(liste_num))

# la function round() arondie un nombre directement dans l'entier le plus pres
print(round(1.2))
print(round(1.9))
