import tkinter

#paramettrage de la fenetre
app = tkinter.Tk()
app.title("Comment positionner un Widget")
app.geometry("700x400")

#Widget
# mainFrame = tkinter.LabelFrame(app, width=300, height=200, borderwidth=1)
# mainFrame.pack()
label = tkinter.Label(app, text="label")
entry = tkinter.Entry(app)
btn = tkinter.Button(app, text="BIENVENU")
btn.place(x=500, y=10)

label.grid(row=0, column=0, columnspan=2, rowspan=3)
entry.grid(row=0, column=2)
btn.grid(row=0, column=3,)



#Boucle principale
app.mainloop()