import tkinter


def show_about():
    show_about = tkinter.Toplevel()
    show_about.title("Nouvelle femetre")
    show_about.geometry("700x400")
    label = tkinter.Label(show_about, text="Bienveu sur une page")

# paramettrage de la fenetre
app = tkinter.Tk()
app.title("Création du menu")
app.geometry("700x400")


#Widget
mainmenu = tkinter.Menu(app)

first_menu = tkinter.Menu(mainmenu, tearoff=0)
first_menu.add_command(label="Option 1")
first_menu.add_separator()
first_menu.add_command(label="Option 2")
first_menu.add_command(label="Quitter", command=app.quit)

secondde_menu = tkinter.Menu(mainmenu, tearoff=0)
secondde_menu.add_command(label="commande 1")
secondde_menu.add_separator()
secondde_menu.add_command(label="A propos", command=show_about)

mainmenu.add_cascade(label="premier menu", menu=first_menu)
mainmenu.add_cascade(label="deuxieme menu", menu=secondde_menu)






# Boucle principale
app.config(menu=mainmenu)
app.mainloop()

