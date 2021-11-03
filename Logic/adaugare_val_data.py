from Domain.cheltuieli import get_suma, get_id, get_nr_ap, get_tipul, creeaza_cheltuiala, get_data
from Logic.crud import format_data


def adaugare_val_data(lst_cheltuieli , data:str, val:int):
    format_data(data)
    lst_cheltuieli_noua =[]
    minim_o_cheltuiala = False
    for x in lst_cheltuieli:
        if get_data(x) == data:
            minim_o_cheltuiala = True
            suma_noua = get_suma(x) + val
            id = get_id(x)
            nr_ap = get_nr_ap(x)
            tip = get_tipul(x)
            lst_cheltuieli_noua.append(creeaza_cheltuiala(id,nr_ap,suma_noua,data,tip))
        else:
            lst_cheltuieli_noua.append(x)
    if minim_o_cheltuiala == False :
        raise ValueError(f'Nu exista nici o cheltuiala pe data {data}')
    return lst_cheltuieli_noua