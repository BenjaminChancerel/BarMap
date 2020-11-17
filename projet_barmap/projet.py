import folium
import os
import json
import webbrowser
import tkinter as tk
from PIL import ImageTk, Image

#Définition de la premiere fonction liée au premier bouton tkinter
def map():
    #liaison au fichier JSON correspondant
    def loadfromjson(filename):
        with open(filename, 'r', encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data

    userDictionnayFile = "data/point.json"
    loadjsondata = loadfromjson(userDictionnayFile)

    # Création de la Map et de sa position
    m = folium.Map(location=[44.837789, -0.57918], zoom_start=13)
    
    # Création des marqueurs à partir d'un fichier JSON 
    for point in loadjsondata:
        html = f'<h4 style="color: #1E4579; font-family: Georgia, serif; font-weight: bold;">{point["name"]}</h4><br>\n<h5 style="color: #5F6164; font-family: Georgia, serif;">{point["adresse"]}</h5><br>\n<h6 style="font-family: Georgia, serif;">{point["note"]}</h6><br>'
        folium.Marker(
            location=point['coordinates'],   
            popup=html,
            tooltip= point['popup'] ,
            icon=folium.Icon(color= point['marker-color'], icon=point['marker-symbol'])
        ).add_to(m)

    # Generation de la map dans notre navigateur
    m.save('map.html')
    chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open('map.html')

#Définition de la deuxieme fonction liée au deuxieme bouton tkinter
def cinq():
    #liaison au fichier JSON correspondant
    def loadfromjson(filename):
        with open(filename, 'r', encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data

    userDictionnayFile = "data/5étoiles.json"
    loadjsondata = loadfromjson(userDictionnayFile)

    # Création de la Map
    m = folium.Map(location=[44.837789, -0.57918], zoom_start=13)

     
    # Création des marqueurs à partir d'un fichier JSON 
    for point in loadjsondata:
        html = f'<h4 style="color: #1E4579; font-family: Georgia, serif; font-weight: bold;">{point["name"]}</h4><br>\n<h5 style="color: #5F6164; font-family: Georgia, serif;">{point["adresse"]}</h5><br>\n<h6 style="font-family: Georgia, serif;">{point["note"]}</h6><br>'
        folium.Marker(
            location=point['coordinates'],
            popup=html,
            tooltip= 'Bar ☆☆☆☆☆' ,
            icon=folium.Icon(color= point['marker-color'], icon=point['marker-symbol'])
        ).add_to(m)

    # Generation de la map dans notre navigateur
    m.save('map.html')
    chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open('map.html')

#Définition de la troisieme fonction liée au troisieme bouton tkinter
def quatre():
    #liaison au fichier JSON correspondant
    def loadfromjson(filename):
        with open(filename, 'r', encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data

    userDictionnayFile = "data/4étoiles.json"
    loadjsondata = loadfromjson(userDictionnayFile)

    # Création de la Map
    m = folium.Map(location=[44.837789, -0.57918], zoom_start=13)
     
    # Création des marqueurs à partir d'un fichier JSON 
    for point in loadjsondata:
        html = f'<h4 style="color: #1E4579; font-family: Georgia, serif; font-weight: bold;">{point["name"]}</h4><br>\n<h5 style="color: #5F6164; font-family: Georgia, serif;">{point["adresse"]}</h5><br>\n<h6 style="font-family: Georgia, serif;">{point["note"]}</h6><br>'
        folium.Marker(
            location=point['coordinates'],
            popup=html,
            tooltip= 'Bar ☆☆☆☆' ,
            icon=folium.Icon(color= point['marker-color'], icon=point['marker-symbol'])
        ).add_to(m)

    # Generation de la map dans notre navigateur
    m.save('map.html')
    chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open('map.html')


#Définition de la quatrieme fonction liée au quatrieme bouton tkinter
def trois():
    #liaison au fichier JSON correspondant
    def loadfromjson(filename):
        with open(filename, 'r', encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data

    userDictionnayFile = "data/3étoiles.json"
    loadjsondata = loadfromjson(userDictionnayFile)

    # Création de la Map
    m = folium.Map(location=[44.837789, -0.57918], zoom_start=13)
 
    # Création des marqueurs à partir d'un fichier JSON 
    for point in loadjsondata:
        html = f'<h4 style="color: #1E4579; font-family: Georgia, serif; font-weight: bold;">{point["name"]}</h4><br>\n<h5 style="color: #5F6164; font-family: Georgia, serif;">{point["adresse"]}</h5><br>\n<h6 style="font-family: Georgia, serif;">{point["note"]}</h6><br>'
        folium.Marker(
            location=point['coordinates'],
            popup=html,
            tooltip= 'Bar ☆☆☆' ,
            icon=folium.Icon(color= point['marker-color'], icon=point['marker-symbol'])
        ).add_to(m)

    # Generation de la map dans notre navigateur
    m.save('map.html')
    chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open('map.html')

def quais():

    def loadfromjson(filename):
        with open(filename, 'r', encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data

    userDictionnayFile = "data/quais.json"
    loadjsondata = loadfromjson(userDictionnayFile)

    # Création de la Map 
    # Création des marqueurs à partir d'un fichier JSON 
    m = folium.Map(location=[44.837789, -0.57918], zoom_start=13)

    for point in loadjsondata:
        html = f'<h4 style="color: #1E4579; font-family: Georgia, serif; font-weight: bold;">{point["name"]}</h4><br>\n<h5 style="color: #5F6164; font-family: Georgia, serif;">{point["adresse"]}</h5><br>\n<h6 style="font-family: Georgia, serif;">{point["note"]}</h6><br>'
        folium.Marker(
            location=point['coordinates'],   
            popup=html,
            tooltip= point['popup'] ,
            icon=folium.Icon(color= point['marker-color'], icon=point['marker-symbol'])
        ).add_to(m)

    # Generation de la map
    m.save('map.html')
    chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open('map.html')
    

def centre():

    def loadfromjson(filename):
        with open(filename, 'r', encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data

    userDictionnayFile = "data/centre.json"
    loadjsondata = loadfromjson(userDictionnayFile)

    # Création de la Map 
    # Création des marqueurs à partir d'un fichier JSON 
    m = folium.Map(location=[44.837789, -0.57918], zoom_start=13)

    for point in loadjsondata:
        html = f'<h4 style="color: #1E4579; font-family: Georgia, serif; font-weight: bold;">{point["name"]}</h4><br>\n<h5 style="color: #5F6164; font-family: Georgia, serif;">{point["adresse"]}</h5><br>\n<h6 style="font-family: Georgia, serif;">{point["note"]}</h6><br>'
        folium.Marker(
            location=point['coordinates'],   
            popup=html,
            tooltip= point['popup'] ,
            icon=folium.Icon(color= point['marker-color'], icon=point['marker-symbol'])
        ).add_to(m)

    # Generation de la map
    m.save('map.html')
    chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open('map.html')

#Création de la fenetre d'accueil avec Tkinter
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.creer_widegets()
    #Création du texte de présentation et d'accueil
    def creer_widegets(self):
        self.beerimage = Image.open("1.jpeg")
        self.beerimages = ImageTk.PhotoImage(self.beerimage)

        self.can1 = tk.Canvas(self, bg="#128D75", height=720, width=720)
        self.introText = self.can1.create_text(
            360, 20, text="Bonjour,", font="Arial 17", anchor="center", fill="White"
        )
        self.presText = self.can1.create_text(
            360, 60, text="Nous sommes deux élèves de Ynov Informatique actuellement en B1.", font="Arial 17", anchor="center", fill="White"
        )
        self.sujetText = self.can1.create_text(
            360, 100, text="Nous avons fait une selection de bars sur Bordeaux pour vous !", font="Arial 17", anchor="center", fill="White" 
        )
        self.can1.create_image(
            360, 400, image=self.beerimages
        )

        #Creation des boutons téléportateurs vers les maps
        self.can1.pack(side="left")
        self.boutonMap = tk.Button(self, text="Tous les bars", font="Arial 12", bg="#557AFA", fg="white", command=map)
        self.bouton3 = tk.Button(self, text="Bars ☆☆☆", font="Arial 12",bg="#0B69B8", fg="white", command=trois)
        self.bouton4 = tk.Button(self, text="Bars ☆☆☆☆",font="Arial 12",bg="#0B69B8", fg="white", command=quatre)
        self.bouton5 = tk.Button(self, text="Bars ☆☆☆☆☆",font="Arial 12",bg="#0B69B8", fg="white", command=cinq)
        self.boutonQuai = tk.Button(self, text="Bars des quais", font="Arial 12", bg="#153668", fg="white", command=quais)
        self.boutonCenter = tk.Button(self, text="Bars du centre", font="Arial 12", bg="#153668", fg="white", command=centre)
        self.boutonquit = tk.Button(self, text="Quitter",font="Arial 11", fg="red", command=quit)
        self.boutonMap.pack()
        self.bouton3.pack()
        self.bouton4.pack()
        self.bouton5.pack()
        self.boutonQuai.pack()
        self.boutonCenter.pack()
        self.boutonquit.pack(side="bottom")

if __name__ == "__main__":
    app = Application()
    app.title("BarMap")
    app.mainloop()