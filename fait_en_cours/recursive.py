def sum_rec(n):
    if n < 0 :
        print("Erreur : n doit être un entier positif")
    elif n == 0:
        return 0
    else :
        return n + sum_rec(n-1)
    
def sum_for(n):
    
    sum = 0
    for i in range(n):
        sum = sum + i + 1
    return sum
    
def sum_one_line(n):
    return n * (n+1) / 2

nb = int(input("Entrez un nombre de valeurs à sommer :"))
print("La somme des", nb, "premiers entiers est :", sum_rec(nb))