"""cette exercice a pour but de verifier si le mot de user est trop court ou pas
 et verifer aussi s'il uniquement composer de nombre  l'operation redemarera lorsque les 
 conditions ne sont pas satisfait"""
# au cas l'operation passerai il y'aura une attente de 5 seconde 

from  time import sleep

root = True
while root:
    # recupper le mot de pass de user
    get_mdp = input("entrer votre mot de pass ")

    # verifier si le mdp est courte ou pas
    if len(get_mdp) >= 8:
    
        # verifier si le mdp est composer que de chiffre ou pas
        if not get_mdp.isdigit():
            root = False
            print("Traitement en cours...")
            sleep(5)

        else:
            print("Votre mot de pass est former que de chiffres".upper())
    else:
        print("Votre mot de pass est trop courte : 8 caracteres au moins".upper())
else:
    print("Operation effectuer avec succes".upper())