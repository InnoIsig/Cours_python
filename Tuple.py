"""
    creation du tuple: mon_tuple = () #vide
                       mon_tuple = 17, #une seul valeur
                       mon_tuple = (17,) #Idem qu'on dessus
                       mon_tuple = (3, 4, 5,) plusieurs valeurs

    Accès aux valeurs : mon_tuple[X] # valeur d'indice X
    (!) Tuple : conteneur immuable (dont on peut modifier la valeur)

"""

mon_tuple = (45, 56, 67)

try:
    print((mon_tuple[2]))
except:
    print("Dépassement du tuple")

#affectation multiple avec le tuple
nombre1, nombre2 = 64, 32
print(nombre1)
print(nombre1)

def get_position_player():
    Posx = 167
    Posy = 67

    return (Posx, Posy)

cosx = 0 
cosy = 0

print(f"la position du joueuer est {cosx}/{cosy}")

cosx, cosy = get_position_player()

print(f"la position du joueuer est {cosx}/{cosy}")
