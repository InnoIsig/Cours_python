import tkinter

"""
    Stringvar  : chaine de caractere (str)
    intvar     : nombre entier (int)
    DoubleVar  : nombre flottant (flottant)
    BooleanVar : nombre boolean
"""
# observateur pour modifier en temps reel la saisi de l'utilisateu
def update_label(*args):
    var_label.set(var_entry.get())

    if var_gender.get():
        var_label_geder.set("ES-tu bien un Homme ?")
        print("C'est un Homme")
    else:
        var_label_geder.set("ES-tu bien une Fememe ?")
        print("C'est une femme")

# création et parametrage de la fenetre
app = tkinter.Tk()
app.title("Introduction aux varibales tkinter")
app.geometry("400x300")

# Wedget
# Affichage à l'ecran pour identifier si c'est une Femme ou un Homme
var_label_geder = tkinter.StringVar()
label_geder = tkinter.Label(app, textvariable=var_label_geder)

# creation de checkbox lorque l'utilisateur selectionne une de genre entre Homme ou Femme
var_gender = tkinter.IntVar()
var_gender.trace("w", update_label)
radio_buttun1 = tkinter.Radiobutton(app, text="Homme", value=1, variable=var_gender)
radio_buttun2 = tkinter.Radiobutton(app, text="Femme", value=0, variable=var_gender)

# Modification de la valeur par le label
var_entry = tkinter.StringVar()
var_entry.trace("w", update_label)
entry = tkinter.Entry(textvariable=var_entry)

#creation d'une variable et le set pour modifier la valeur
var_label = tkinter.StringVar()
label = tkinter.Label(app, textvariable=var_label)

var_label.set("")
print("Label :", var_label.get())

# pour supprimer par exemple
#trace_vedelete("u", update_label())


entry.pack()
label.pack()
radio_buttun1.pack()
radio_buttun2.pack()
label_geder.pack()



#boucle principale
app.mainloop()