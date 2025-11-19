from datetime import datetime, date

def age_now(birth_year : int, birth_month : int, birth_day : int) :
   birth = datetime(birth_year, birth_month, birth_day)
   today = date.today()
   
   birth_date_now = date(today.year, birth.month, birth.day)
   age = today.year - birth.year
   if today < birth_date_now:
       age = age - 1
   return age

annee = 1998
mois = 12
jour = 20

age_actuel = age_now(annee, mois, jour)
print(f"Vous avez {age_actuel} ans.")
# Vous avez 26 ans.