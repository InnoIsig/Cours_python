"""
Lesture             : read(), readline(), readlins()
"""
import pickle

# Pour ouvrir un fichier
fic = open("docs/donees.txt.txt", "r")

# Pour recupérer tous les élément du fichier et lecture seule
print(fic.read())
content = fic.read()
print(content)

#pour recupérer qu'une ligne dans un fichie
line = fic.readline()
print(line)

line = fic.readline()
print(line)

line = fic.readline()
print(line)


# fermer un fichier
fic.close()

# Pour ouvrir un fichier autrement
with open ("docs/donees.txt.txt", "r") as fic:
    content = fic.read()
    print(content)

#verifier si le ficheir est fermé
if fic.closed:
    print("C'est ouvrir")
else:
    print("C'est fermé")

# pas besoin de close()

# Pour donner accès à l'écriture 
with open ("docs/donees.txt.txt", "r") as fic:
    nombre = 14
    fic.write(str(nombre))  
    fic.write("Bonjour tout le monde")

# Creation d'une classe pour specifier un mode binaire
class Player:
    def __init__(self, nom, level):
        self.nom = nom
        self.level = level

    def Qui_t_es(self):
        print(f"{self.nom} {self.level}")

p1 = Player("Innocent", 6)
p1.Qui_t_es()

with open("Player.data", "wb") as nom_variable:
    record = pickle.Pickler(nom_variable)
    # Je fais la copie de mon objet p1 = Player("Innocent". 6)
    record.dump(p1)

