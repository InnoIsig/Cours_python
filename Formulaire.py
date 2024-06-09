import tkinter

# Creation d'une fenetre
mainapp = tkinter.Tk()
mainapp.title("Mon première fénetre")

#redimensionnement de taille
#mainapp.minsize(640, 480)
#mainapp.maxsize(900, 600)
#mainapp.sizefrom("user")
#mainapp.positionfrom("user")
#empache la redimensionnement de la taille d'une fenetre ou vice-versa
#mainapp.resizable(width=False, height=False)

screen_x = int(mainapp.winfo_width())
screen_y = int(mainapp.winfo_height())
windo_x = 800
windo_y = 600

pos_X = (screen_x // 2) - (windo_x // 2)
pos_Y = (screen_y // 2) - (windo_y // 2)


geo = "{}x{}+{}+{}".format(windo_x, windo_y, pos_X, pos_Y)
mainapp.geometry(geo)


"""
pour centrer la fenetre
position_X = (largeur_ecran // 2) - (largeur_fenetre // 2)
position_Y = (hauteur_ecran // 2) - (largeur_fenetre // 2)
"""

#Utilisation de geometry
#geomety(XxY+0+0)
mainapp.geometry("800x600+50+100")



#boucle qui facilte l'utilisateur de fermer la fenettre
mainapp.mainloop()