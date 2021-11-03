from Logic.crud import read
from Logic.stergere_cheltuieli import sterge_cheltuieli_nr_ap
from Tests.test_Crud import get_cheltuieli


def test_stergere_cheltuieli():
    lst_cheltuieli = get_cheltuieli()
    nr_ap = 3
    lista_noua = sterge_cheltuieli_nr_ap(lst_cheltuieli, nr_ap)
    assert len(lista_noua) == len(lst_cheltuieli)-1
    assert read(lst_cheltuieli,3) is not None

