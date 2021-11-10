from Domain.cheltuieli import get_suma


def ordonare(lista,undo_list,redo_list):
    """
    functia returneaza lista de cheltuieli ordonata descrescator in functie de suma
    :param lista: lst
    :param undo_list:Lista de cheltuieli, ce se modifica in urma apelarii fiecarei functionalitati
    :param redo_list:Lista ce se modifica in urma apelarii fiecarei Undo
    :return: lst de cheltuieli
    """
    undo_list.append(lista)
    redo_list.clear()
    return sorted(lista , key=get_suma, reverse = True)