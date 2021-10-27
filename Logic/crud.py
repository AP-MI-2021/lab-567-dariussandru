from Domain.cheltuieli import creeaza_cheltuiala, get_id


def adaugare(lst_cheltuieli, id, nr_ap, suma, data, tip):
    """
    se formeaza lista
    :param lst_cheltuieli: O lista de cheltuieli
    :param id: int
    :param nr_ap: int
    :param suma: int
    :param data: int
    :param tip: str
    :return: O noua lista
    """
    cheltuiala_noua = creeaza_cheltuiala(id, nr_ap, suma, data, tip)
    return lst_cheltuieli + [cheltuiala_noua]


def stergere(lst_cheltuieli, id):
    """
    se sterge din lista cheltuiala cu id = cu id-ul citit de la tastatura
    :param lst_cheltuieli: lista de cheltuieli
    :param id: id-ul unei cheltuieli
    :return: lista dupa elimiminearea unei cheltuieli
    """
    lista_noua_cheltuieli = []
    for x in lst_cheltuieli:
        if get_id(x) != id:
            lista_noua_cheltuieli.append(x)
    return lista_noua_cheltuieli


def modif(lst_cheltuiali, cheltuiala_noua):
    """
    se modifica lista in functie de un id citit de la tastatura
    :param lst_cheltuiali: lista de cheltuieli
    :param cheltuiala_noua: lista noua
    :return: lista dupa modificare
    """
    lista_noua_cheltuieli = []
    for x in lst_cheltuiali:
        if get_id(x) != get_id(cheltuiala_noua):
            lista_noua_cheltuieli.append(x)
        else:
            lista_noua_cheltuieli.append(cheltuiala_noua)
    return lista_noua_cheltuieli


def read(lst_cheltuieli, ap_id):
    """
    Functia verifica daca apare in lista de cheltuieli o anumita cheltuiala, cu id dat
    :param lst_cheltuieli:O lista de cheltueieli
    :param ap_id:Numarul apartamentului a cheltuielii
    :return:Returneaza cheltuiala cautata (daca exista in lista) sau toata lista daca nr_ap_cheltuiala = None
    """
    nr_ap_cheltuiala = 0
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) == ap_id:
            nr_ap_cheltuiala = cheltuiala
    if nr_ap_cheltuiala:
        return nr_ap_cheltuiala
    return lst_cheltuieli