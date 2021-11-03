from Domain.cheltuieli import get_nr_ap


def sterge_cheltuieli_nr_ap(lst_cheltuieli,nr_ap):
    """
    
    :param lst_cheltuieli: 
    :param nr_ap: 
    :return: 
    """
    lista_noua=[]
    for x in lst_cheltuieli:
        if get_nr_ap(x) != nr_ap:
            lista_noua.append(x)
    if len(lista_noua) == len(lst_cheltuieli):
            raise ValueError("Nu exista nici o cheltuiala la acest nr de apartament!")
    return lista_noua