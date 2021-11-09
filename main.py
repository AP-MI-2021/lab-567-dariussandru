from Logic.crud import adaugare
from Tests.all_tests import run_all_tests
from User_Interface.console import user_interface_crud
from User_Interface.console_command import user_interface_command_console


def main():
    lst_cheltuieli = []
    undo_list=[]
    redo_list=[]
    lst_cheltuieli = adaugare(lst_cheltuieli, 1, 3, 234.5, '28.11.2004', 'alte cheltuieli', undo_list, redo_list)
    lst_cheltuieli = adaugare(lst_cheltuieli, 2, 1, 300, '27.11.2004', 'canal', undo_list, redo_list)
    print("1. Pentru a accesa meniul basic")
    print("2. Pentru a accesa meniu command")
    menu = int(input("Dati tipul de meniu dorit:"))
    if menu == 1:
        user_interface_crud(lst_cheltuieli, undo_list, redo_list)
    elif menu == 2:
        user_interface_command_console(lst_cheltuieli, undo_list, redo_list)



if __name__ == '__main__':
    run_all_tests()
    main()