from datetime import datetime, date


def calcul_age(date_naissance : datetime) -> int :
    today = date.today()
    birth_date_now = date(today.year, date_naissance.month, date_naissance.day)
    age = today.year - date_naissance.year
    if today < birth_date_now:
        age = age - 1
    return age
    
date_naissance = datetime.strptime(input("Entrez votre date de naissance (jj/mm/aaaa) : "), "%d/%m/%Y")
age = calcul_age(date_naissance)
print(f"Vous avez {age} ans.")
