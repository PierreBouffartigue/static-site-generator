#!/usr/bin/python3
# coding: utf-8

#Importation des librairies

import markdown
import argparse

md = markdown.Markdown()

#Préparation à l'écriture et la lisibilité des fichiers 

HTML = 'test.html'
MD = 'replace_me.md'
Fichier_HTML = open(HTML,'w')
Fichier_MD = open(MD,'r')

#Ecriture de la mise en page html dans le nouveau fichier html avec au milieu une conversion du markdown en html 

print("Conversion du Markdown en HTML ...")

Fichier_HTML.write("<!DOCTYPE html>\n<html>\n <head>\n\t<meta charset='utf-8'/>\n\t<title>Site-Statique</title>\n\t<link rel='stylesheet' href='style.css' />\n </head>\n <body>\n")
lecture = Fichier_MD.read()
Fichier_HTML.write(md.convert(lecture))
Fichier_HTML.write("\n </body>\n</html>")

print("Fin de la conversion !")

#Fermeture du fichier et fin du programme

parser = argparse.ArgumentParser
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Show this help message and exit.')

Fichier_HTML.close()

