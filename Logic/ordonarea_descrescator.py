from Domain.cheltuieli import get_suma


def ordonare(lista,undo_list,redo_list):
    undo_list.append(lista)
    redo_list.clear()
    return sorted(lista , key=get_suma, reverse = True)