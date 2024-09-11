# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity = int(input("Quantité d'eau à assainir (en L):"))
filtres = water_quantity / 5
lampes = water_quantity * 3 / 5
chlore = water_quantity / 10

print(f"Voici les matériaux requis pour l'assainissement de {water_quantity}L d'eau:\n- {filtres} filtres\n- {lampes} lampes UV\n- {chlore}kg de chlore")