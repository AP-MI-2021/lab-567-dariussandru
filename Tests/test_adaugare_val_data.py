from Logic.adaugare_val_data import adaugare_val_data
from Tests.test_Crud import get_cheltuieli


def test_adaugare_val_data():
    lista_cheltuieli = get_cheltuieli()
    data = '12.10.2002'
    val = 100
    lista_cheltuieli_noua = adaugare_val_data(lista_cheltuieli,data,val)
    assert len(lista_cheltuieli_noua) == len(lista_cheltuieli)
    try:
        alta_data = '01.11.2002'
        lista_cheltuieli_noua = adaugare_val_data(lista_cheltuieli_noua,alta_data,val)
        assert False
    except ValueError:
        assert True