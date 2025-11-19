import numpy as np

alea = np.random.randint(1000, size=1)[0]
guess = 1000

while guess != alea:
    guess = int(input("Devinez le nombre (entre 0 et 999) : "))
    if guess < alea:
        print("C'est plus !")
    elif guess > alea:
        print("C'est moins !")

print("Bravo ! Vous avez trouvé le nombre :", alea)