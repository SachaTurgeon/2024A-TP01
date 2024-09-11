#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ? ")
code_medals = input("Chaine représentant les médailles ? ")
gold = 0
silver = 0
bronze = 0
i = 0
error = False

while i < len(code_medals):
    if code_medals[i] == "G":
        gold += 1
    elif code_medals[i] == "S":
        silver += 1
    elif code_medals[i] == "B":
        bronze += 1
    else:
        error = True
        break
    i += 1

if error == False:
    print(f"{country}:\n- Or: {gold}\n- Argent: {silver}\n- Bronze: {bronze}")
else:
    print("Erreur dans la chaine de médailles.")