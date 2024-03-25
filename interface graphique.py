import tkinter as tk
import csv

def chercher_telephone():
    telephone = entry.get()
    with open(r"C:\Users\PC\Downloads\scrapiingfinal.csv", newline='') as fichier_csv:
        lecteur_csv = csv.DictReader(fichier_csv)
        for ligne in lecteur_csv:
            if telephone in ligne.values():
                attribut_trouve = ligne
                break
        else:
            attribut_trouve = None

    if attribut_trouve:
        print(f"Prix JUMIA: {attribut_trouve['price1']}, Prix BESTMARKET: {attribut_trouve['price2']}")
    else:
        print("Téléphone non trouvé")

fenetre = tk.Tk()
fenetre.geometry('400x400')
fenetre.title('le prix minimal')
fenetre['bg'] = 'white'
fenetre.resizable(height=True, width=True)

entry = tk.Entry(fenetre)
entry.grid(row=0, column=0, padx=230, pady=130)
label = tk.Label(fenetre , text="choissisez le téléphone que vous désirez", font=("verdana", 16), fg='pink' , bg='white')
label.place(x='90',y='30')

bouton = tk.Button(fenetre , text='rechercher', bg='pink', fg='white', command=chercher_telephone)
bouton.place(x='260', y='80')


fenetre.mainloop()