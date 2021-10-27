from Domain.cheltuieli import creeaza_cheltuiala, get_str
from Logic.crud import adaugare, modif, stergere


def user_interface_add(lst_cheltuieli):
    id_ap = int(input("Introduceti id-ul cheltuielii: "))
    nr_ap = int(input("Introduceti numarul apartamentului: "))
    suma = int(input("Introduceti suma cheltuielii: "))
    data = input("Introduceti data :")
    tip = input("Introduceti tipul cheltuielii:")
    lst_cheltuieli = adaugare(lst_cheltuieli, id_ap, nr_ap, suma, data, tip)
    return lst_cheltuieli


def user_interface_all(lst_cheltuieli):
    for cheltuiala in lst_cheltuieli:
        print(get_str(cheltuiala))


def user_interface_modif(lst_cheltuieli):
    id_ap = int(input("Introduceti id-ul cheltuielii care doriti sa se modifice:"))
    nr_ap = int(input("Dati nr apartamentului  "))
    suma = int(input("Dati noua suma a cheltuielii: "))
    data = input("Dati noua data a cheltuielii:")
    tip = input("Dati noul tip al cheltuielii:")
    new_cheltuiala = creeaza_cheltuiala(id_ap, nr_ap, suma, data, tip)
    return modif(lst_cheltuieli, new_cheltuiala)


def user_interface_delete(lst_cheltuieli):
    id_ap = int(input("Dati id-ul cheltuielii care sa se modifice: "))
    lst_cheltuieli = stergere(lst_cheltuieli, id_ap)
    return lst_cheltuieli


def user_interface_crud(lst_cheltuieli):

    while True:
        print("1.Adauga")
        print("2.Modifica")
        print("3.Sterge")
        print("a.Afiseaza cheltuieli")
        print("x.Iesire")
        optiune = input("Dati o optiune: ")
        if optiune == "1":
            lst_cheltuieli = user_interface_add(lst_cheltuieli)
        elif optiune == "2":
            lst_cheltuieli = user_interface_modif(lst_cheltuieli)
        elif optiune == "3":
            lst_cheltuieli = user_interface_delete(lst_cheltuieli)
        elif optiune == "a":
            user_interface_all(lst_cheltuieli)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita, reincercati")
    return lst_cheltuieli