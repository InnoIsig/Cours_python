"""
Création du dictionnaire: dico = {} #vide
                          deco = {<cle>:<valeur>, <cle>:<valeur>}

Accès dans un dictionnaire :  print(deco[cle])
ajout et modification dans le dictionnaire : dico[<cle>] = "<valeur>"
suppression :
copie du dictionnaire       : dico1 = {1:464, 2:744}
                              dico2 = dico1.copy()
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

#pour retourner la cle d'une valeu
for key in dico.keys():
     print(key)

# Pour afficher les valeur
for value in dico.values():
    print(value)

# Verification de chaque valeur
for (k,v) in dico.items():
    print(f"Cle : {k} -valeur {v}")

dico2 =dico
print(dico)
print(dico2)

dico["ok"] = "ok"
print(dico)
print(dico2)

# paramettre nome
def maFoction(**paramettre):
   print(paramettre)

maFoction(p= 234, nom = "innocent")

