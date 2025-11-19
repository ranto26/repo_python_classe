number = input("Entrer un nombre :")
number = int(number)

if number%15 == 0:
    print("tic toc")
elif number%3 == 0:
    print("tic")
elif number%5 == 0:
    print("toc")
else :
    print(number)