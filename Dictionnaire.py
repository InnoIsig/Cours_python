"""
Création du dictionnaire: dico = {} #vide
                          deco = {<cle>:<valeur>, <cle>:<valeur>}

Accès dans un dictionnaire :  print(deco[cle])
ajout et modification dans le dictionnaire : dico[<cle>] = "<valeur>"
suppression :
"""

dico = {"nom":"Innocent", "ville":"Goma" }
print(dico["nom"])

#ajout de valeur dan un dictionnaire
dico["prenom"] = "toujours Innocent dans chaque circontance"
print(dico)

dico["autre nom"] = "Monsieur"
print(dico)

# Pour supprimer un element dans le dictionnaire
dico.pop("autre nom")
print(dico)


# valeur_supprime = dico.pop("ville")
# print(valeur_supprime)
# dico.pop("ville")
# print(dico)

# Pour recuperer une valeur supprimer
valeur_supprime = dico.pop("ville")
print(valeur_supprime)

if  "Innocent" in dico:
    print("oui je sui la")
else:
    print("Non suis pas en l'interieur")