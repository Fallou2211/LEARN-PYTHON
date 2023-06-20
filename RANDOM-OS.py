import random
import os

# le module random
# generer un nombre entier dans une intervallle inclusive
nombre_1 = random.randint(0, 100)
# generer un nombre decimal dans une intervallle inclusive
nombre_2 = random.uniform(0, 100)
# generer un nombre entier dans une intervallle exclusive par pas de 10
nombre_3 = random.randrange(0, 101, 10)

print(f"nombre_1 {nombre_1}, nombre_2 {nombre_2}, nombre_3 {nombre_3}")

#le module os
#chemin du dossier
chemin = r"\Users\lenovo\Desktop\Mes_cours\APPRENDRE-PYTHON"
#concaternation du chemin
dossier = os.path.join(chemin, "nouveau_dossier")
# verifier si le chemin existe avec de creer le dossier
if not os.path.exists(dossier) :
    os.makedirs(dossier)
    print("creation avec succes")
else:
    print("le dossier existe deja")

# supprimer le dossier
if os.path.exists(dossier):
    os.removedirs(dossier)
    print("supprimer avec succes")
else:
    print("Ce dosssier n'exite pas encore")



