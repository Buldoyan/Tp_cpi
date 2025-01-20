import tkinter as tk
from tkinter import simpledialog

     # Fonction pour récupérer les titres et sous-titres
def recuperer_titres():
    root = tk.Tk()
    root.withdraw()  # Cacher la fenêtre principale

    titre = simpledialog.askstring("Titre", "Entrez le titre du cours:")
    sous_titre = simpledialog.askstring("Sous-titre", "Entrez le sous-titre du cours:")

    with open("Cahier_de_texte.txt", "a") as fichier:
        fichier.write(f"Titre: {titre}\nSous-titre: {sous_titre}\n")
             # Appel de la fonction
recuperer_titres()

