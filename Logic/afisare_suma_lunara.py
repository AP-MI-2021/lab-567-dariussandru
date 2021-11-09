from Domain.cheltuieli import get_data, get_suma


def get_suma_lunara(lst_cheltuieli):
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