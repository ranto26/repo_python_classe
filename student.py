class Student:
    """Une classe pour représenter un(e) étudiant(e)."""
    def __init__(self, name : str = "Nouvel etudiant", notes : list[float] = []):
        """Cette fonction construit l'objet Student

        Args:
            name (str): nom de l'étudiant(e)
            notes (list[float]): liste des notes de l'étudiant(e). Par défaut, une liste vide.
        """
        self.name = name
        def verifier_notes(notes : list[float]) -> list[float]:
            """Cette fonction vérifie que les notes sont comprises entre 0 et 20.

            Args:
                notes (list[float]): liste des notes à vérifier

            Returns:
                list[float]: liste des notes valides
            """
            notes_valides = True
            for note in notes:
                if (note < 0) or (note > 20):
                    notes_valides = False
            if notes_valides:
                return notes
            else:
                print("Les notes doivent être comprises entre 0 et 20.")
                return []
        self.notes = verifier_notes(notes).copy()

    

    def present(self):
        """Cette fonction retourne une phrase de présentation.

        Returns:
            str: Phrase de présentation
        """
        phrase = f"Je m'appelle {self.name}."
        return phrase
    
    def add_new_note(self, new_note : float):
        """Cette fonction ajoute une nouvelle note à l'étudiant(e).

        Args:
            new_note (float): nouvelle note à ajouter
        """
        if (new_note >= 0) and (new_note <= 20):
            self.notes.append(new_note)
        else:
            print("La note doit être comprise entre 0 et 20.")
    def get_mean_notes(self):
        """Cette fonction retourne la moyenne générale de l'élève.
        Returns:
            float: Moyenne générale de l'élève
        """
        if len(self.notes) == 0:
            return 0
        moyenne = sum(self.notes)/len(self.notes)
        return moyenne