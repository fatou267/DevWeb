#-*-coding:Latin-1 -*
from tkinter import *

fenetre = Tk()

champ_label = Label(fenetre, text="Dictionnaire français")

champ_label.pack()

var= StringVar()

var_text= Entry(fenetre, text=var, width=30)
var_text.pack()

dictionnaire = {"manger": "Absorber un aliment",
				"aller": "Se mouvoir d'un lieu vers un autre",
				"dormir": "être plonger dans le sommeil",
				"affecter": "Destiner quelque chose à  un usage particulier",
				"responsable": "Qui est l'auteur ou le coupable de quelque chose",
				"armoire":"Meuble de rangement",
				"dictionnaire": "Meuble de rangement",
				"flexible":"Qui se plie, se courbe aisément",
				"garant": "Qui est caution d'une autre personne",
				"bloc": "Masse compacte de quelque chose"
}
def getMot():
	value = var_text.get()
	for cle, valeur in dictionnaire.items():
		if cle == value:
			ligne = cle + " : "+dictionnaire[cle]
			champ = Label(fenetre, text=ligne)
			return champ.pack()
	
	champ = Label(fenetre, text="ce mot n'existe pas")
	return champ.pack()
			

btn = Button(fenetre, text="Rechercher", command=getMot)
btn.pack()



bouton_quitter = Button(fenetre, text="QUITTER", command=fenetre.quit)
bouton_quitter.pack()

fenetre.mainloop()
