# -*-coding:Latin-1 -*
import os
import pickle
from random import choice
from donnees import *

def recup_score():

	if os.path.exists(mon_fichier):
		fichier_score = open(mon_fichier, "rb")
		mon_depickler = pickle.Unpickler(fichier_score)
		scores = mon_depickler.load()

		fichier_score.close()
	else:
		scores = {}
	return scores


def enregistre_score(scores):
	fichier_score = open(mon_fichier, "wb")
	mon_pickler = pickle.Pickler(fichier_score)
	mon_pickler.dump(scores)
	fichier_score.close()




def recup_nom_utilisateur():

	nom_utilisateur = input("tapez votre nom")

	nom_utilisateur = nom_utilisateur.capitalize()

	if not nom_utilisateur.isalnum() or len(nom_utilisateur)<4:

		 print("Ce nom est invalide")

		 return recup_nom_utilisateur()
	else:
		return nom_utilisateur



def recup_lettre():
	lettre = input("tapez une lettre")

	lettre = lettre.lower()

	if len(lettre)>1 or not lettre.isalpha():
		print("vous n'avez pas saisi une lettre valide.")
		return recup_lettre
	else:
		return lettre


def choisir_mot():
	

	return choice(ma_list)


def recup_mot_masque(mot_complet, lettres_trouvees):
	mot_masque = ""

	for lettre in mot_complet:
		if lettre in lettres_trouvees:
			mot_masque += lettre
		else:
			mot_masque += "*"
	return mot_masque