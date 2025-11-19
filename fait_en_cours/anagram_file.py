def anagram(mot_1, mot_2):
    list_1 = list(mot_1)
    list_1.sort()
    list_2 = list(mot_2)
    list_2.sort()

    if list_1 == list_2:
        print("Les mots sont des anagrammes.")
    else:
        print("Les mots ne sont pas des anagrammes.")

mot_1 = input("Entrez le premier mot : ")
mot_2 = input("Entrez le deuxième mot : ")
anagram(mot_1, mot_2)