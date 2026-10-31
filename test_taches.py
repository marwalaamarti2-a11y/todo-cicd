import pytest
from taches import GestionnaireTaches


def test_ajouter():
    g = GestionnaireTaches()
    g.ajouter("Réviser")
    assert g.lister() == [{"titre": "Réviser", "terminee": False}]


def test_ajouter_vide():
    g = GestionnaireTaches()
    with pytest.raises(ValueError):
        g.ajouter("   ")


def test_terminer():
    g = GestionnaireTaches()
    g.ajouter("Réviser")
    g.terminer(1)
    assert g.lister()[0]["terminee"] is True


def test_supprimer():
    g = GestionnaireTaches()
    g.ajouter("A")
    g.ajouter("B")
    g.supprimer(1)
    assert g.lister() == [{"titre": "B", "terminee": False}]


def test_numero_inexistant():
    g = GestionnaireTaches()
    with pytest.raises(IndexError):
        g.supprimer(5)


def test_liste_vide():
    assert GestionnaireTaches().lister() == []


def test_lister_en_cours():
    g = GestionnaireTaches()
    g.ajouter("A")
    g.ajouter("B")
    g.terminer(1)
    assert g.lister_en_cours() == [{"titre": "B", "terminee": False}]
