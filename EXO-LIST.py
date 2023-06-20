# recuperer les nombres pairs d'une liste dans une autre liste avec list comprehention
print("----------les nombres pairs d'une liste dans une autre liste avec list comprehention----------")
liste = ["2", "5", "10", "7", "9", "8", "17", "16"]
liste_pair = [i for i in liste if int(i)%2 == 0]
print(liste_pair)


# recuperer les nombres positifs d'une liste dans une autre liste avec list comprehention
print("----------les nombres positif une liste avec list comprehention----------")
liste_postif = [i for i in range(-10, 11) if i>=0]
print(liste_postif)

# recuperer le double des nombres dans liste avec list comprehention
print("----------recuperer le double des nombre----------")
liste_double = [i*2 for i in range(5)]
print(liste_double)

# recuperer les nombres paires et l'inverse des nombres impaire dans une liste avec list comprehention
print("----------recuperer les nombres paires et l'inverse des nombres impaire----------")
nombre = range(10)
inverse_number = [i  if i%2 == 0 else -i for i in nombre]
print(inverse_number)
#Nb : lorsqu'on a un else dans la liste le for se trouve apres le else
