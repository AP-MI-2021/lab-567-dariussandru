from Domain.cheltuieli import get_suma
from Logic.ordonarea_descrescator import ordonare
from Tests.test_Crud import get_cheltuieli


def test_ordonare_descrescator():
    list = get_cheltuieli()
    lista_noua = ordonare(list,[],[])
    assert len(list)== len(lista_noua)
    assert get_suma(lista_noua[0]) == 323
    assert get_suma(lista_noua[2]) == 175