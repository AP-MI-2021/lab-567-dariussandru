from Domain.cheltuieli import get_str
from Logic.crud import adaugare, stergere


def add(lst_cheltuieli, id_ap, nr_ap, suma, data, tip, undo_list, redo_list):
    try:
        id_ap = int(id_ap)
    except ValueError as ve:
        print('Eroare: ', ve)
    try:
        nr_ap = int(nr_ap)
    except ValueError as ve:
        print('Eroare: ', ve)
    try:
        suma = int(suma)
    except ValueError as ve:
        print('Eroare: ', ve)
    try:
        lst_cheltuieli = adaugare(lst_cheltuieli, id_ap, nr_ap, suma, data, tip, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare:', ve)
    print('Cheltuiala s-a aduagat cu succes!')
    return lst_cheltuieli


def delete(lst_cheltuieli, id_ap, undo_list, redo_list):
    try:
        id_ap = int(id_ap)
    except ValueError as ve:
        print('Eroare: ', ve)
        return lst_cheltuieli
    try:
        lst_cheltuieli = stergere(lst_cheltuieli, id_ap, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare:', ve)
    print('Cheltuiala s-a sters cu succes!')
    return lst_cheltuieli


def showall(lst_cheltuieli):
    for cheltuiela in lst_cheltuieli:
        print(get_str(cheltuiela))


def user_interface_command_console(lst_cheltuieli, undo_list, redo_list):
    while True:
        print('Puteti adauga cheltuieli in lista de cheltuieli, cu functia "add" ')
        print('Puteti afisa toate cheltuielile din lista de cheltuieli, cu functia "showall"')
        print('Puteti sterge cheltuieli, scriind "delete" si introducand un id al unei cheltuieli existente')
        print('Toate comenzile trebuie apelate pe o singura linie si separate prin ";" iar campurile prin ",", '
              'fara alti separatori!!!')
        print("x.Iesire din program")
        print('')

        optiune = input('Introduceti comenzile:')
        optiuni = optiune.split(';')

        for comenzi in optiuni:
            sir_optiune = comenzi.split(',')
            if sir_optiune[0] == 'add':
                id_ap = sir_optiune[1]
                nr_ap = sir_optiune[2]
                suma = sir_optiune[3]
                data = sir_optiune[4]
                tip = sir_optiune[5]
                lst_cheltuieli = add(lst_cheltuieli, id_ap, nr_ap, suma, data, tip, undo_list, redo_list)

            if sir_optiune[0] == 'delete':
                id_ap = sir_optiune[1]
                lst_cheltuieli = delete(lst_cheltuieli, id_ap, undo_list, redo_list)

            if sir_optiune[0] == 'showall':
                showall(lst_cheltuieli)
        if optiune == "x":
                break