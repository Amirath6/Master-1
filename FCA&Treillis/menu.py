import csv

# Path: menu.py
def menu(path: str):
    #Lire le fichier csv
    file = open(path, "r")
    reader = csv.reader(file)
    relation = {}
    for row in reader:
        relation[row[0]] = [ing.strip() for ing in row[1:]]
    
    G = relation.keys()
    
    M = []
    for _, ingredients in relation.items():
        for ingredient in ingredients:
            if (ingredient not in M):
                M.append(ingredient)

    # Créer la matrice avec des 0 et 1 pour indiquer les relation
    matrice = [[0 for _ in M] for _ in G]

    for i, g in enumerate(G):
        for j, m in enumerate(M):
            if m in relation[g]:
                matrice[i][j] = 1

    # Afficher la matrice
    for row in matrice:
        print(row)

    return matrice, G, M

def write_menu(path: str):
    matrice, G, M = menu(path)
    file = open("menu.rcf", "w")
    file.write("[Relational Context]\nMenu Pizzas\n[Binary Relation]\nmenupiza.csv\n")
    for pizza in G:
        file.write(pizza + " | ")
    file.write("\n")
    for _, ingredient in enumerate(M):
        file.write(ingredient + " | ")
    file.write("\n")
    for row in matrice:
        for value in row:
            file.write(str(value) + " ")
        file.write("\n")    
    file.write("\n")
    file.write("[END Relational Context]")
    # file.close()

write_menu("menupizza.csv")
