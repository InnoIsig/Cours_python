import tkinter

def updade_label(*args):
    var_label.set(var_entry.get())
    if var_label.get():
        var_info_label.set("T'es bien un Homme")
        print("C'est l'homme") 
    else:
        var_info_label.set("T'es bien une Femme")
        print("C'est une femme")

app = tkinter.Tk()
app.title("Ma page")
app.geometry("700x400")

var_info_label = tkinter.StringVar()
info_label = tkinter.Label(app, textvariable=var_info_label)

var_entry = tkinter.StringVar()
var_entry.trace("w", updade_label)
entry = tkinter.Entry(app, textvariable=var_entry)

var_label = tkinter.StringVar()
label = tkinter.Label(app, textvariable=var_label)

var_label_gender = tkinter.IntVar()
var_label_gender.trace("w", updade_label)
radion_button1 = tkinter.Radiobutton(app, text="Homme", value=1, variable=var_label_gender)
radion_button2 = tkinter.Radiobutton(app, text="Femme", value=0, variable=var_label_gender)

var_label.set("Saisie...")
print("label :", var_label.get())

label.pack()
entry.pack()
radion_button1.pack()
radion_button2.pack()
info_label.pack()


app.mainloop()