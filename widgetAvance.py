import tkinter

# biblithèque pour estimer unee condition pendant un evenement dans l'interface
from tkinter import messagebox
import tkinter.messagebox

# app = tkinter.Tk()
# app.minsize(640, 480)
# app.maxsize(900, 600)

# check_widget = tkinter.Checkbutton(app,text="Publier", offvalue=2, onvalue=5)
# radion_widget = tkinter.Radiobutton(app,text="Femme", value=1)
# radion_widget2 = tkinter.Radiobutton(app,text="Homme", value=0)
# spin_widget = tkinter.Spinbox(app, from_=1, to=100)

# # Creation d'une liste
# lb = tkinter.Listbox(app)
# lb.insert(1,"Windows")
# lb.insert(2,"MacOs")
# lb.insert(3,"Linux")
# lb.insert(4,"Et autre...")

#cursseur de 0 à 100%
# scale_widget = tkinter.Scale(app, from_=10, to=100, tickinterval=25)

# check_widget.pack()
# radion_widget.pack()
# radion_widget2.pack()
# scale_widget.pack()
# spin_widget.pack()
# lb.pack()


# app.mainloop()

app = tkinter.Tk()
def show_error():
    messagebox.askquestion("ERREUR", "Une erreur est survenu")

btn = tkinter.Button(app, text="Déclacher cette erreur avant de continuer", command=show_error)

btn.pack()


app.mainloop()