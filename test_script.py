from promo import Promo
from student import Student

def test_etudiant_valid():
    print("Test : création d'un étudiant valide...")
    etu = Student("Alice", [2, 4, 4, 19])
    assert etu.name == "Alice"
    assert etu.notes == [2, 4, 4, 19]
    print("Succes")


def test_notes_negatives():
    print("Test : notes négatives interdites...")
    etu = Student("Bob", [-1, 10, 15])
    assert etu.notes == []
    print("Succes")

def test_notes_sup_20():
    print("Test : notes > 20 interdites...")
    etu = Student("Carl", [10, 25, 5])
    assert etu.notes == []
    print("Succes")
    


def test_moyenne_correcte():
    print("Test : moyenne correcte...")
    etu = Student("Diane", [10, 10, 10])
    assert etu.get_mean_notes() == 10
    print("Succes")


def test_moyenne_vide():
    print("Test : moyenne d'une liste vide...")
    etu = Student("Eve", [])
    assert etu.get_mean_notes() == 0
    print("Succes")


def test_promo_ajout():
    print("Test : ajout d'étudiants dans la promo...")
    promo = Promo()
    promo.add_student(Student("Alice", [10, 12]))
    promo.add_student(Student("Bob", [15, 5]))
    assert len(promo.students) == 2.0
    print("Succes")


def test_promo_moyenne():
    print("Test : moyenne de promo...")
    promo = Promo()
    promo.add_student(Student("A", [10, 10]))  # moyenne 10
    promo.add_student(Student("C", [20, 0]))   # moyenne 10
    assert promo.get_mean_promo() == 10.0
    print("Succes")


def test_promo_vide():
    print("Test : moyenne d'une promo vide...")
    promo = Promo()
    assert promo.get_mean_promo() == 0
    print("Succes")


if __name__ == "__main__":
    print("\n=== Lancement des tests ===\n")

    test_etudiant_valid()
    test_notes_negatives()
    test_notes_sup_20()
    test_moyenne_correcte()
    test_moyenne_vide()
    test_promo_ajout()
    test_promo_moyenne()
    test_promo_vide()

    print("\n Les test sont passés")
