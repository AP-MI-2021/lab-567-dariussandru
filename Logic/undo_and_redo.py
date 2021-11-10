def do_undo(undo_list, redo_list, current_list):
    """
    functia retine lista inaite de a fii apelata o functionalitate
    :param undo_list: lista de cheltuieli inaintea apelarii unei functionalitati
    :param redo_list: lista de cheltuieli dupa aplicarea unei functionalitati
    :param current_list: lista curenta
    :return: lista noua
    """
    if undo_list:
        top_undo = undo_list.pop()
        redo_list.append(current_list)
        return top_undo
    return None


def do_redo(undo_list, redo_list, current_list):
    """
    functia returneaza lista inaitea apelarii undo-ului
    :param undo_list: lista de cheltuieli inaintea apelarii unei functionalitati
    :param redo_list: lista de cheltuieli dupa aplicarea unei functionalitati
    :param current_list: lista curenta
    :return: lista noua
    """
    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(current_list)
        return top_redo
    return None