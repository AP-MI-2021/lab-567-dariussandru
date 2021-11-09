from Logic.afisare_suma_lunara import get_suma_lunara
from Tests.test_Crud import get_cheltuieli


def test_get_suma_lunara():
    lst_cheltuieli = get_cheltuieli()
    rezultat_sume = get_suma_lunara(lst_cheltuieli)
    rezultat = {}
    rezultat[10] = [250, 100, 175]
    rezultat[7] = [323]
    rezultat[12] = [123.3, 275]
    assert len(rezultat) == len(rezultat_sume)
    assert (rezultat_sume == rezultat) is False
