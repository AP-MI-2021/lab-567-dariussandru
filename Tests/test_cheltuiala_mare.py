from Logic.cheltuiala_mare import cea_mai_mare_cheltuiala
from Tests.test_Crud import get_cheltuieli


def test_cea_mai_mare_cheltuiala():
    lista_cheltuiala = get_cheltuieli()
    rezultat = cea_mai_mare_cheltuiala(lista_cheltuiala)
    assert len(rezultat) == 3