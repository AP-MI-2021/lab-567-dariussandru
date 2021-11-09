from Domain.cheltuieli import creeaza_cheltuiala, get_str
from Logic.adaugare_val_data import adaugare_val_data
from Logic.afisare_suma_lunara import get_suma_lunara
from Logic.cheltuiala_mare import cea_mai_mare_cheltuiala
from Logic.crud import adaugare, modif, stergere
from Logic.ordonarea_descrescator import ordonare
from Logic.stergere_cheltuieli import sterge_cheltuieli_nr_ap
from Logic.undo_and_redo import do_undo, do_redo


def menu():
    print("1.Adauga")
    print("2.Modifica")
    print("3.Sterge")
    print("4.Stergerea tuturor cheltuielilor pentru un apartament dat")
    print("5.Adunarea undei valori la toate cheltuielile dintr-o data citita")
    print("6.Determinati cea mai mare cheltuiala pentru fiecare tip de cheltuiala")
    print("7.Ordoneaza descrescator in functie de suma")
    print("8.Afișarea sumelor lunare pentru fiecare apartament.")
    print("u.Undo")
    print("r.Redo")
    print("a.Afiseaza cheltuieli")
    print("x.Iesire")

def user_interface_add(lst_cheltuieli, undo_list,redo_list):
    try:
        id_ap = int(input("Introduceti id-ul cheltuielii: "))
        nr_ap = int(input("Introduceti numarul apartamentului: "))
        suma = int(input("Introduceti suma cheltuielii: "))
        data = input("Introduceti data :")
        tip = input("Introduceti tipul cheltuielii:")
        lst_cheltuieli = adaugare(lst_cheltuieli, id_ap, nr_ap, suma, data, tip, undo_list, redo_list)
    except ValueError as ve:
        print("Eroare:",ve)
    return lst_cheltuieli


def user_interface_all(lst_cheltuieli):
    for x in lst_cheltuieli:
        print(get_str(x))


def user_interface_modif(lst_cheltuieli, undo_list, redo_list):
    try:
        id_ap = int(input("Introduceti id-ul cheltuielii care doriti sa se modifice:"))
        nr_ap = int(input("Dati nr apartamentului  "))
        suma = int(input("Dati noua suma a cheltuielii: "))
        data = input("Dati noua data a cheltuielii:")
        tip = input("Dati noul tip al cheltuielii:")
        cheltuiala_noua = creeaza_cheltuiala(id_ap, nr_ap, suma, data, tip)
        lst_cheltuieli = modif(lst_cheltuieli, cheltuiala_noua, undo_list, redo_list)
    except ValueError as ve:
        print("Eroare", ve)
    return lst_cheltuieli


def user_interface_delete(lst_cheltuieli, undo_list, redo_list):
    try:
        id_ap = int(input("Dati id-ul cheltuielii care sa se modifice: "))
        lst_cheltuieli = stergere(lst_cheltuieli, id_ap, undo_list, redo_list)
    except ValueError as ve:
        print("Eroare",ve)
    else:
        print("Cheltuiala s-a sters !")
    return lst_cheltuieli

def user_interface_sterge_cheltuieli_nr_ap(lst_cheltuieli, undo_list, redo_list):
    try:
        nr_ap = int(input("Indorduceti nr ap :"))
        lst_cheltuieli = sterge_cheltuieli_nr_ap(lst_cheltuieli, nr_ap, undo_list, redo_list)
    except ValueError as ve:
        print("Eroare",ve)
    else:
        print(f"Cheltuiala s-a sters cu succes!")
    return lst_cheltuieli

def user_interface_adaugare_val_dat(lst_cheltuieli, undo_list, redo_list):
    try:
        data = input("Dati o data dupa care se cauta cheltuiala :")
        val = int(input("Dati valoarea care se adauga"))
        lst_cheltuieli = adaugare_val_data(lst_cheltuieli,data,val,undo_list,redo_list)
    except ValueError as ve:
        print("Eroare",ve)
    else:
        print("Valoarea a fost schimbata cu succes")
    return lst_cheltuieli

def user_interface_cea_mai_mare_cheltuiala(lst_cheltuiala):
    rezultat = cea_mai_mare_cheltuiala(lst_cheltuiala)
    for tip in rezultat:
        print(f"Pentru tipul {tip} avem chltuiala:  {get_str(rezultat[tip])}")

def user_interface_ordonare_descrescatr(lst_cheltuiala,undo_list , redo_list):
    lst_cheltuiala = ordonare(lst_cheltuiala, undo_list,redo_list)
    print("Ordonarea s-a facut cu succes")
    return lst_cheltuiala

def user_interface_suma_lunara_fiecare_ap(lst_cheltuiala):
    rezultat= get_suma_lunara(lst_cheltuiala)
    for x in rezultat:
        print(f"Pentru luna {x}, avem lista de sume: {rezultat[x]}")

def user_interface_undo(lst_cheltuieli,undo_list, redo_list):
    undo_rezultat = do_undo(undo_list, redo_list, lst_cheltuieli)
    if undo_rezultat is not None:
        return undo_rezultat
    return lst_cheltuieli


def user_interface_redo(lst_cheltuieli, undo_list , redo_list):
    redo_result = do_redo(undo_list, redo_list, lst_cheltuieli)
    if redo_result is not None:
        return redo_result
    return lst_cheltuieli


def user_interface_crud(lst_cheltuieli,undo_list,redo_list):

    while True:
        menu()

        optiune = input("Dati o optiune: ")
        if optiune == "1":
            lst_cheltuieli = user_interface_add(lst_cheltuieli,undo_list,redo_list)
        elif optiune == "2":
            lst_cheltuieli = user_interface_modif(lst_cheltuieli,undo_list,redo_list)
        elif optiune == "3":
            lst_cheltuieli = user_interface_delete(lst_cheltuieli,undo_list,redo_list)
        elif optiune == "4":
            lst_cheltuieli = user_interface_sterge_cheltuieli_nr_ap(lst_cheltuieli,undo_list,redo_list)
        elif optiune == "5":
            lst_cheltuieli = user_interface_adaugare_val_dat(lst_cheltuieli,undo_list,redo_list)
        elif optiune == "6":
            lst_cheltuieli = user_interface_cea_mai_mare_cheltuiala(lst_cheltuieli)
        elif optiune == "7":
            lst_cheltuieli = user_interface_ordonare_descrescatr(lst_cheltuieli,undo_list,redo_list)
        elif optiune == "8":
            lst_cheltuieli = user_interface_suma_lunara_fiecare_ap(lst_cheltuieli)
        elif optiune == "u":
            lst_cheltuieli = user_interface_undo(lst_cheltuieli,undo_list,redo_list)
        elif optiune == "r":
            lst_cheltuieli =user_interface_redo(lst_cheltuieli,undo_list,redo_list)
        elif optiune == "a":
            user_interface_all(lst_cheltuieli)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita, reincercati")
    return lst_cheltuieli

