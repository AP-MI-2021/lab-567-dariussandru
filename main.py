from Tests.test_Crud import test_crud
from Tests.test_adaugare_val_data import test_adaugare_val_data
from Tests.test_cheltuiala_mare import test_cea_mai_mare_cheltuiala
from Tests.test_ordonare_descrescator import test_ordonare_descrescator
from Tests.test_stergere_cheltuieli import test_stergere_cheltuieli
from User_Interface.console import user_interface_crud


def main():
    lst_cheltuieli = []
    user_interface_crud(lst_cheltuieli)


if __name__ == '__main__':
    test_crud()
    test_stergere_cheltuieli()
    test_adaugare_val_data()
    test_cea_mai_mare_cheltuiala()
    test_ordonare_descrescator()
    main()