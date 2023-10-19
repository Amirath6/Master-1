#Écriture de la fonction naifZERO qui résout le problème ZERO en mettant en œuvre cette approche naîve.

def naifZERO(E):
    n=len(E)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if E[i]+E[j]+E[k]==0:
                    return True
    return False


# Écriture d'une fonction testZERO qui résout le problème ZERO.
def testZERO(E):
    E.sort()
    n=len(E)
    for i in range(0, n-3):
        deb = i+1
        fin = n-1
        while deb < fin:
            if E[i]+E[deb]+E[fin] > 0:
                fin -= 1
            elif E[i]+E[deb]+E[fin] < 0:
                deb += 1
            else:
                return True
    return False

# Ecriture de la fonction reduction qui, à partir d’une instance TRILISTE (trois
# listes d’entiers) construit l’instance ZERO correspondante (une liste d’entiers)
def reduction(X, Y, Z):
    liste = []
    for x in X:
        liste.append(10*x + 1)
    for y in Y:
        liste.append(10*y + 2)
    for z in Z:
        liste.append(10*z - 3)
    return liste

# Déduction de la fonction testTRILISTE et qui fait appel à la fonction reduction et à la fonction testZERO
def testTRILISTE(X, Y, Z):
    r = reduction(X, Y, Z)
    return testZERO(r)



####################################################################################################################################                                        Mon menu pour tester les fonctions
####################################################################################################################################    

# Exemple d'utilisation de la fonction naifZERO
E = [-4, 13, 2, -7, -5, -12, 5, 4]
# E =  [-10, 13, -7, -2, -4]
# E= [5, 2, -3, 8, 9]
res = naifZERO(E)
print("#----------------------------------------------------------")

print("\n TEST DE ZERO AVEC LA FONCTION naifZERO\n")

print(E," est elle une instance positive de ZERO ? ")
print("\n\tRéponse : ",res)

print("\n TEST DE ZERO AVEC LA FONCTION OPTIMAL testZERO\n")

res2 = testZERO(E)
print(E," est elle une instance positive de ZERO ? ")
print("\n\tRéponse : ",res2)

X = [2, -4, -7]
Y = [-5, 8, -6, -1]
Z = [-3, -10, 9]
# X = [2, 4, 7]
# Y = [5, 8, 6]
# Z = [3, 10, 9]
print("\n TEST DE TRILISTE \n")
t = testTRILISTE(X, Y, Z)

print("X = ",X,"\nY = ",Y,"\nZ = ",Z,"\n")

print("(X,Y,Z) est elle une instance positive de TRILISTE? ")

print("\n\tRéponse : ",t,"\n")