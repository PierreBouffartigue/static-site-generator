#!/usr/bin/python3
# coding: utf-8

#Importation des librairies
import markdown
md = markdown.Markdown()

#Préparation à l'écriture et la lisibilité des fichiers 
HTML = 'test.html'
MD = 'replace_me.md'
Fichier_HTML = open(HTML,'w')
Fichier_MD = open(MD,'r')

#Ecriture de la mise en page html dans le nouveau fichier html avec au milieu conversion du markdown en html 

Fichier_HTML.write("<!DOCTYPE html>\n<html>\n <head>\n\t<meta charset='utf-8'/>\n\t<title>Site-Statique</title>\n\t<link rel='stylesheet' href='style.css' />\n </head>\n <body>\n")
lecture = Fichier_MD.read()
Fichier_HTML.write(md.convert(lecture))
Fichier_HTML.write("\n </body>\n</html>")

#Fermeture du fichier et fin du programme

Fichier_HTML.close()

