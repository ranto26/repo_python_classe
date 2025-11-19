def palindrome_test(mot : str or int) -> bool:
    mot = str(mot)
    list_mot = list(mot)
    is_palindrome = True
    if len(list_mot)==1:
        return is_palindrome
    half = len(list_mot)//2
    for i in range(half):
        if list_mot[i] != list_mot[-(i+1)]:
            is_palindrome = False
    return is_palindrome

word = input("Entrez un mot ou un nombre :")
test_palindrome = palindrome_test(word)
if test_palindrome:
    print(f"{word} est un palindrome")
else:
    print(f"{word} n'est pas un palindrome")