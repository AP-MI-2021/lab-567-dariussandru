from Tests.test_Crud import test_crud
from Tests.test_adaugare_val_data import test_adaugare_val_data
from Tests.test_afisare_suma_lunara import test_get_suma_lunara
from Tests.test_cheltuiala_mare import test_cea_mai_mare_cheltuiala
from Tests.test_ordonare_descrescator import test_ordonare_descrescator
from Tests.test_stergere_cheltuieli import test_stergere_cheltuieli
from Tests.test_undo_redo import test_undo_redo


def run_all_tests():
    test_get_suma_lunara()
    test_adaugare_val_data()
    test_crud()
    test_ordonare_descrescator()
    test_stergere_cheltuieli()
    test_undo_redo()
    test_cea_mai_mare_cheltuiala()