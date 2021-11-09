from Domain.cheltuieli import creeaza_cheltuiala
from Logic.crud import adaugare
from Logic.undo_and_redo import do_undo, do_redo
from Tests.test_Crud import get_cheltuieli


def test_undo_redo():
    lst_cheltuieli = get_cheltuieli()
    params = creeaza_cheltuiala(7, 3, 3, "11.11.1111", "canal")
    undo_list=[]
    redo_list=[]
    lst_cheltuieli_noua = adaugare(lst_cheltuieli,*params,undo_list,redo_list)
    lst_cheltuieli_noua = do_undo(undo_list,redo_list,lst_cheltuieli_noua)
    assert lst_cheltuieli_noua == lst_cheltuieli
    lst_cheltuieli_noua = do_redo(undo_list,redo_list,lst_cheltuieli_noua)
    assert len(lst_cheltuieli_noua) == len(lst_cheltuieli)+1