from student import Student

class Promo:
    """Une classe pour représenter une promotion d'étudiants."""
    def __init__(self, name_promo : str = "Nouveau promo", list_students : list[Student] = []):
        """Cette fonction construit l'objet Promo

        Args:
            name_promo (str): nom de la promo
            students (list[Student]): liste des étudiants de la promo. Par défaut, une liste vide.
        """
        self.name_promo = name_promo

        def verifier_nb_notes(list_etudiants : list[Student]) -> bool:
            """Cette fonction vérifie si tous les étudiants ont le même nombre de notes."""
            if len(list_etudiants) == 0:
                return True
            else :
                nb_notes = len(list_etudiants[0].notes)
                for etudiant in list_etudiants:
                    if len(etudiant.notes) != nb_notes:
                        return False
                return True
        if verifier_nb_notes(list_students):
            self.students = list_students.copy()
        else:
            print("Tous les étudiants doivent avoir le même nombre de notes.")
            self.students = []


    def add_student(self, new_student : Student):
        """Cette fonction ajoute un étudiant à la promo.

        Args:
            new_student (Student): nouvel étudiant à ajouter
        """
        if len(self.students) == 0:
            self.students.append(new_student)
        else:
            nb_notes = len(self.students[0].notes)
            if len(new_student.notes) != nb_notes:
                print("L'étudiant doit avoir le même nombre de notes que les autres étudiants de la promo.")
            else:
                self.students.append(new_student)
    def get_mean_promo(self):
        """Cette fonction retourne la moyenne générale de la promo.
        """
        if len(self.students) == 0:
            return 0
        total = 0
        for student in self.students:
            total += student.get_mean_notes()
        moyenne_promo = total / len(self.students)
        return moyenne_promo
    
    def present_promo(self):
        """Cette fonction retourne la liste des étudiants de la promo.

        Returns:
            list: Liste des étudiants de la promo
        """
        if len(self.students) == 0:
            return "La promo est vide."
        else :
            list_etudiants = [etudiant.name for etudiant in self.students]
            return list_etudiants