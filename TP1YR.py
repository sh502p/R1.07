#1
nom = "Rechal"
prenom = "Yanis"
maths = 20
anglais = 19
info = 21
promotion = 2023
moy = (maths+anglais+info)/3

print("L’étudiant {} {} de la promotion {} a une moyenne de {}".format(nom, prenom, promotion, moy))
#2
jour=23
heure=14
minutes=26

total=jour*24*60+heure*60+minutes

print ("Il s'est écoulé un total de", total, "minutes depuis le début du mois")

#3
print ("Quel jour est-il?")
jour=int(input())
print ("Quelle heure est-il?")
heure=int(input())
print ("Quelles minutes est-il?")
minute=int(input())

total=jour*24*60+heure*60+minute

print ("Il s'est écoulé un total de", total, "minutes depuis le début du mois")

#4

print("Combien de minutes se sont écoulés depuis le début du mois?")
minute=int(input())
heure = minute // 60
jour = heure // 24

print ("il s'est passé", jour, "jours depuis le début du mois")

# EX 5
from random import *
oui = randint(0,100)
print(oui)
