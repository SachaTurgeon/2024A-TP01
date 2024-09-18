# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = float(input("Pourcentage de batterie ? "))

if (battery_level > 50):
    distance = (battery_level - 50) * 2 + 25 * 0.5 + 15 + 5 * 2.5 + 5 * 6
elif (battery_level > 25):
    distance = (battery_level - 25) * 0.5 + 15 + 5 * 2.5 + 5 * 6
elif (battery_level > 10):
    distance = (battery_level - 10) + 5 * 2.5 + 5 * 6
elif (battery_level > 5):
    distance = (battery_level - 5) * 2.5 + 5 * 6
else:
    distance = battery_level * 6

if distance > 0:
    print(f"{distance} km")
else:
    print("La batterie est vide")