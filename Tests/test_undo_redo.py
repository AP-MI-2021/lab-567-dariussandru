from Domain.cheltuieli import creeaza_cheltuiala
from Logic.crud import adaugare, read
from Logic.undo_and_redo import do_undo, do_redo
from Tests.test_Crud import get_cheltuieli


def test_undo_redo():
    lst_cheltuieli = get_cheltuieli()
    undo_list = []
    redo_list = []
    lst_cheltuieli_noua = adaugare(lst_cheltuieli, *creeaza_cheltuiala(7, 3, 3, "11.11.1111", "canal"), undo_list, redo_list)
    lst_cheltuieli_noua = do_undo(undo_list, redo_list, lst_cheltuieli_noua)
    assert lst_cheltuieli_noua == lst_cheltuieli
    lst_cheltuieli_noua = do_redo(undo_list, redo_list, lst_cheltuieli_noua)
    assert len(lst_cheltuieli_noua) == len(lst_cheltuieli)+1

def test_undo_redo_lab():
    lst_cheltuieli = []
    undo_list = []
    redo_list = []
    lst_cheltuieli = adaugare(lst_cheltuieli, 1, 1, 100, "10.10.2010", "canal", undo_list, redo_list)
    lst_cheltuieli = adaugare(lst_cheltuieli, 2, 2, 200, "10.10.2010", "canal", undo_list, redo_list)
    lst_cheltuieli = adaugare(lst_cheltuieli, 3, 3, 300, "10.10.2010", "canal", undo_list, redo_list)
    assert lst_cheltuieli == [[1, 1, 100, "10.10.2010", "canal"],
                              [2, 2, 200, "10.10.2010", "canal"],
                              [3, 3, 300, "10.10.2010", "canal"]]
    lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert lst_cheltuieli == [[1, 1, 100, "10.10.2010", "canal"],
                              [2, 2, 200, "10.10.2010", "canal"],]
    lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert lst_cheltuieli == [[1, 1, 100, "10.10.2010", "canal"]]
    lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert read(lst_cheltuieli, 1) is None
    assert read(lst_cheltuieli, 2) is None
    assert read(lst_cheltuieli, 3) is None
    lst_cheltuieli = adaugare(lst_cheltuieli, 1, 1, 100, "10.10.2010", "canal", undo_list, redo_list)
    lst_cheltuieli = adaugare(lst_cheltuieli, 2, 2, 200, "10.10.2010", "canal", undo_list, redo_list)
    lst_cheltuieli = adaugare(lst_cheltuieli, 3, 3, 300, "10.10.2010", "canal", undo_list, redo_list)
    assert lst_cheltuieli == [[1, 1, 100, "10.10.2010", "canal"],
                              [2, 2, 200, "10.10.2010", "canal"],
                              [3, 3, 300, "10.10.2010", "canal"]]
    if len(redo_list) > 0:
        lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert lst_cheltuieli == [[1, 1, 100, "10.10.2010", "canal"],
                              [2, 2, 200, "10.10.2010", "canal"],
                              [3, 3, 300, "10.10.2010", "canal"]]
    if len(undo_list) > 0:
        lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert lst_cheltuieli == [[1, 1, 100, "10.10.2010", "canal"],
                              [2, 2, 200, "10.10.2010", "canal"]]
    if len(undo_list) > 0:
        lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert lst_cheltuieli == [[1, 1, 100, "10.10.2010", "canal"]]
    if len(redo_list) > 0:
        lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert lst_cheltuieli == [[1, 1, 100, "10.10.2010", "canal"],
                              [2, 2, 200, "10.10.2010", "canal"]]
    if len(redo_list) > 0:
        lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert lst_cheltuieli == [[1, 1, 100, "10.10.2010", "canal"],
                              [2, 2, 200, "10.10.2010", "canal"],
                              [3, 3, 300, "10.10.2010", "canal"]]
    if len(undo_list) > 0:
        lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert lst_cheltuieli == [[1, 1, 100, "10.10.2010", "canal"],
                              [2, 2, 200, "10.10.2010", "canal"]]
    if len(undo_list) > 0:
        lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert lst_cheltuieli == [[1, 1, 100, "10.10.2010", "canal"]]
    lst_cheltuieli = adaugare(lst_cheltuieli, 4, 4, 400, "10.10.2010", "canal", undo_list, redo_list)
    assert len(lst_cheltuieli) == 2
    assert lst_cheltuieli == [[1, 1, 100, "10.10.2010", "canal"],
                              [4, 4, 400, "10.10.2010", "canal"]]
    if len(redo_list) > 0:
        lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 2
    assert lst_cheltuieli == [[1, 1, 100, "10.10.2010", "canal"],
                              [4, 4, 400, "10.10.2010", "canal"]]
    if len(undo_list) > 0:
        lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 1
    assert lst_cheltuieli == [[1, 1, 100, "10.10.2010", "canal"]]
    if len(undo_list) > 0:
        lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 0
    assert lst_cheltuieli == []
    if len(redo_list) > 0:
        lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 1
    assert lst_cheltuieli == [[1, 1, 100, "10.10.2010", "canal"]]
    if len(redo_list) > 0:
        lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 2
    assert lst_cheltuieli == [[1, 1, 100, "10.10.2010", "canal"],
                              [4, 4, 400, "10.10.2010", "canal"]]
    if len(redo_list) > 0:
        lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 2
    assert lst_cheltuieli == [[1, 1, 100, "10.10.2010", "canal"],
                              [4, 4, 400, "10.10.2010", "canal"]]

