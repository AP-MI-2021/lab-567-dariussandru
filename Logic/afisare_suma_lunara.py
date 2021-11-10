from Domain.cheltuieli import get_data, get_suma


def get_suma_lunara(lst_cheltuieli):
    """
    Functia retunreaza un dictionar, cu cheia o luna ce se regaseste in data unei cel putin o chetuiala
    din lista iar valoarea o lista de sume ce apartin cheltuielilor ce sunt trecuta pe aceasta luna
    :param lst_cheltuieli: lst
    :return: un dict cu cheia "luna" si o valoare
    """
    rezultat = {}
    for x in lst_cheltuieli:
        data = get_data(x)
        luna = int(data.split(".")[1])
        if luna not in rezultat:
            rezultat[luna]=[]
            rezultat[luna].append(get_suma(x))
        else:
            rezultat[luna].append(get_suma(x))
    return rezultat