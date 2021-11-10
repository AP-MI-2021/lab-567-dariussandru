from Domain.cheltuieli import get_tipul, get_suma


def cea_mai_mare_cheltuiala(lst_cheltuiala):
    rezultat = {}
    for x in lst_cheltuiala:
        tip = get_tipul(x)
        cost = get_suma(x)
        if tip not in rezultat:
            rezultat[tip] = x
        else:
            if cost > get_suma(rezultat[tip]):
                rezultat[tip] = x
    return rezultat
