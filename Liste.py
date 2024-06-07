# invataire = ["Innocent"] * 10
# print(invataire)

"""
Liste[X] : affiche élé,ent d'indice X
Liste[-X] : affiche Xème élément en partant de la din
Liste [:] : affiche tous élément
Lise [:X] : affiche le X premier élémeent
liste[X:] : affichr le X dernier élément
Liste[A:B] : affiche de l'élément d'indice A à l'élément de l'indice B (exclus)

"""

invataire = ["Arc", "Epéé", "Arme", "Fusil", "portion", "Fusil", "Attache", "Fusil"]
print(invataire[:])

# Ajouter un element dans une liste
invataire.append("Machette")
print(invataire[:])

#Ajouter un element selon une indice
invataire.insert(0, "Mateau")
print(invataire[:])

# Pour retirer un element de la liste
invataire.remove("Machette")
print(invataire[:])

# ou bien
del invataire[1]
print(invataire[:])

# Pour chercher l'indice à supprimer
objet_supprimer = invataire.index("Epéé")
del invataire[objet_supprimer]
print(invataire[:])

# Poour trier selon l'ordre alphabetique ou par ordre croissant
invataire.sort()
print(invataire[:])

# Pour inverce les elements dans la liste
invataire.reverse()
print(invataire[:])

# Pour savoir le nombre d'element dans une liste
print("le nombre de l'element Fusil dans la liste est :", invataire.count("Fusil"))

# Pour vider la liste
invataire.clear()
print("la liste est vide",invataire[:])

# ou soit pour vider la liste
invataire[:] = []
print("la liste est vide",invataire[:])

# pour passer d'une liste à une chaine
chaine = "Bonjour tout le monde"
chaine = chaine.split()
print(chaine)

# Pour joindre ma chaine apres avoir splirter mais sur la chaine de caractre
invataire = "Bonjour tout le monde"
phrase = " ".join(invataire)
print(phrase)

# liste en deux
liste1 = ["Banana", "ananas", "avocat", "Pomme"]
liste2 = liste1

print("Liste 1", liste1[:])
print("Liste 1", liste2[:])

liste2.append("Tomate")

print("Liste 1", liste1[:])
print("Liste 1", liste2[:])

# Pour que un element ajouter en liste2 ne soit pas ajouter en liste1 il fautimporter copy

import  copy
liste1 = ["Banana", "ananas", "avocat", "Pomme"]
liste2 = copy.deepcopy(liste1)

print("Liste 1", liste1[:])
print("Liste 1", liste2[:])

liste2.append("Tomate")

print("Liste 1", liste1[:])
print("Liste 1", liste2[:])

# Pour ajouter une liste à ue autre
liste1 = ["Banana", "ananas", "avocat", "Pomme"]
liste2 = ["Fritte", "socis"]
print(liste2[:])

liste1.extend(liste2[:])
print(liste1)

# ou bient on fait
liste1 = ["Banana", "ananas", "avocat", "Pomme"]
liste2 = ["Fritte", "socis"]
print(liste2[:])

liste1 = liste1 + liste2
print(liste1)

# Pour simplifier 
liste1 = ["Banana", "ananas", "avocat", "Pomme"]
liste2 = ["Fritte", "socis"]
print(liste2[:])

liste1 += liste2
liste2.append("Arachide")
print(liste1)
print(liste2[:])

for objet_indice, valeur_objet, in enumerate(liste2, 1):
    print(f"L'element d'indice est {objet_indice} -> {valeur_objet}")


#verification d'un element dans une liste
if "Arme" in invataire:
    print("Oui j'ai l'Arme")
else:
    print("Essaye de verifier d'autre liste")

# Modification d'un element dans une liste
# invataire[2] = "Couteau"
# print(invataire)

# Avec la boucle for
"""for valeur in invataire:
    print(valeur)"""

#Avec la boucle while
"""i = 0
while i < len(invataire):
    print(invataire[i])
    i += 1"""
