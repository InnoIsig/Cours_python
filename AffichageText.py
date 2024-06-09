"""
Pour écrire :
<nom_variable> = <nom_widget>(<widget_parent>, <params>)
"""

import tkinter

app = tkinter.Tk()
app.title("ISIG-GOMA")
app.minsize(640, 480)
app.maxsize(900, 600)

# on peut aussi ecrire le texte de cette maniere
msg =  "Je suis ravi de vous voir" # et faire en suite l'appel de la variable
cree_label = tkinter.Label(app, text="Soyez les bienvenus (e)")
cree_message = tkinter.Message(app, text="Je suis ravi de vous voir")
cree_label.pack()
cree_message.pack()

# Methode de la saisi par l'utilisateur
entry_message = tkinter.Entry(app, show="*")
entry_message.pack()

# Attribut pour afficher helle dans le terminal
def helllo():
    print("Hello to everybody")

# pour creer un boutton quitter
butto_quitter = tkinter.Button(app, text="Quitter", width=25, height=5, justify="center", command=helllo)
butto_quitter.pack()



 # Pour modifier le texte
#cree_label.configure(text="Nouveau message")
app.mainloop()