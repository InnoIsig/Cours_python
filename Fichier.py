import pickle

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