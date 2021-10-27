from Domain.cheltuieli import creeaza_cheltuiala, get_id
from Logic.crud import adaugare, stergere, modif
from Logic.crud import read


def get_cheltuieli():
    return [
        creeaza_cheltuiala(1, 1, 250, '12.10.2002', 'intretinere'),
        creeaza_cheltuiala(2, 2, 100, '12.10.2012', 'intretinere'),
        creeaza_cheltuiala(3, 3, 175, '10.10.2002', 'alte cheltuieli'),
        creeaza_cheltuiala(4, 4, 323.0, '07.07.2020', 'canal'),
        creeaza_cheltuiala(5, 5, 123.3, '08.12.2010', 'alte cheltuieli')
            ]


def test_adaugare():
    lst_cheltuieli = get_cheltuieli()
    cheltuiala_nou = (6, 6, 222, '12.10.2002', 'canal')
    cheltuiala_nou = creeaza_cheltuiala(*cheltuiala_nou)
    lst_cheltuieli_noi = adaugare(lst_cheltuieli, *cheltuiala_nou)
    assert len(lst_cheltuieli_noi) == len(lst_cheltuieli) + 1

    gasit = False
    for x in lst_cheltuieli:
        if x == cheltuiala_nou:
            gasit = True
    assert gasit == False

    gasit = False
    for x in lst_cheltuieli_noi:
        if x == cheltuiala_nou:
            gasit = True
    assert gasit == True


def test_modif():
    lst_cheltuieli = get_cheltuieli()
    schimbat_cheltuiala = (3, 3, 375, '12.10.2002', 'intretinere')
    cheltuiala_noua = creeaza_cheltuiala(*schimbat_cheltuiala)
    lst_cheltuieli_noi = modif(lst_cheltuieli, cheltuiala_noua)
    assert len(lst_cheltuieli_noi) == len(lst_cheltuieli)
    assert cheltuiala_noua not in lst_cheltuieli
    assert cheltuiala_noua in lst_cheltuieli_noi


def test_stergere():
    lst_cheltuieli = get_cheltuieli()
    id_ap = 3
    lst_cheltuieli_noi = stergere(lst_cheltuieli, id_ap)
    assert len(lst_cheltuieli_noi) == len(lst_cheltuieli)-1
    aparitie_cheltuiala = read(lst_cheltuieli, id_ap)
    assert aparitie_cheltuiala not in lst_cheltuieli_noi
    assert aparitie_cheltuiala in lst_cheltuieli

def test_read():
    lst_cheltuieli = get_cheltuieli()
    nr_apartament = lst_cheltuieli[2]
    caut_cheltuiala = read(lst_cheltuieli, get_id(nr_apartament))
    assert caut_cheltuiala in lst_cheltuieli
    assert read(lst_cheltuieli, None) == lst_cheltuieli


def test_crud():
    test_modif()
    test_adaugare()
    test_stergere()
    test_read()
