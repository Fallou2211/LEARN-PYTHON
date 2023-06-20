print("je suis Fallou Thiam") 


#manipulation des chaines de caracteres
#comment remplacer un element de la chaine de caractere
print("bonjour".replace("jour", "soir"))

#supprimer un element de la chaine de caractere
"""la methode strip supprimer en partant de la gauche puis de la droite , elle peut aussi supprimer les space a partit du debut et du fin"""
print("  bienvenue e".strip("  venue e ")) 
print("  bienvenue  ".strip())

#la methode split pour transforment une chaine de caractere en liste de caractere en indiquant le separateur
print("b i e n v e n u e".split(" "))

#la methode join permet de transformer une liste de chaine de caractere en une chaine de caractere brut raw string
print("".join(['b', 'i', 'e', 'n', 'v', 'e', 'n', 'u', 'e']))

#les casses
# Majuscule
print("hollow world".upper())
#Miniscule
print("HELLOW WORLD".lower())
#Majuscule en debut de phrase
print("HELLOW WORLD".capitalize())
#Majuste en debut de chaque mot
print("HELLOW WORLD".title())

# la methode zfil elle permet d'ajouter des zeros dans une chaine de caracteres avec chiffre
print("14".zfill(3))

# la methode count permet de counter le nombre de fois qu'un caractere est present dans une chaine
# elle prend en compte les espaces
print("Bonjour le jour".count("jour"))

#la methode find permet de trouver l'index d'une caractere et return -1 lors ce que n'est pas trouver
# la methode index fait la meme choise mais elle return une erreur a la place de -1
# rfind permet de compter a partir de la droite
print("bonjour".find("jour"))
print("bonjour".index("bon"))

#les methodes startswith et endswith permet de verifier si un mot commence ou termnine par
print("fallou.thiam".endswith("thiam"))

#la methode isdigit pert de vierifier si un caracteres est uniquement composer de chiffre
print("200000".isdigit())

#is et == sont different is verifie si des variables occupe les memes spaces memoires
a = 100
b = 200
print(a is b)

# la methode len permet de compter le nombre de caractere dans une chaine
print(len("je suis Fallou"))
