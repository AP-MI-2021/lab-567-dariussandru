from Domain.cheltuieli import get_nr_ap


def sterge_cheltuieli_nr_ap(lst_cheltuieli, nr_ap, undo_list , redo_list):
    """
    functia returneaza lista care se obtine in urma stergerii tututor cheltuielilor pentru un apartament dat
    :param lst_cheltuieli: lst
    :param nr_ap: int introdus de utilizator
    :return: lst noua 
    """
    lista_noua=[]
    for x in lst_cheltuieli:
        if get_nr_ap(x) != nr_ap:
            lista_noua.append(x)
    if len(lista_noua) == len(lst_cheltuieli):
            raise ValueError("Nu exista nici o cheltuiala la acest nr de apartament!")
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return lista_noua