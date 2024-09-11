# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math

speed = float(input("Vitesse initiale (en m/s): "))
angle = float(input("Angle de lancement (en degrés): "))

distance = ((speed**2)*math.sin(2*math.radians(angle)))/9.8
print(f"La distance maximale en x est de {round(distance, 2)}m")