from Domain.cheltuieli import creeaza_cheltuiala, get_str
from Logic.adaugare_val_data import adaugare_val_data
from Logic.cheltuiala_mare import cea_mai_mare_cheltuiala
from Logic.crud import adaugare, modif, stergere
from Logic.ordonarea_descrescator import ordonare
from Logic.stergere_cheltuieli import sterge_cheltuieli_nr_ap

def menu():
    print("1.Adauga")
    print("2.Modifica")
    print("3.Sterge")
    print("4.Stergerea tuturor cheltuielilor pentru un apartament dat")
    print("5.Adunarea undei valori la toate cheltuielile dintr-o data citita")
    print("6.Determinati cea mai mare cheltuiala pentru fiecare tip de cheltuiala")
    print("7.Ordoneaza descrescator in functie de suma")
    print("a.Afiseaza cheltuieli")
    print("x.Iesire")

def user_interface_add(lst_cheltuieli):
    try:
        id_ap = int(input("Introduceti id-ul cheltuielii: "))
        nr_ap = int(input("Introduceti numarul apartamentului: "))
        suma = int(input("Introduceti suma cheltuielii: "))
        data = input("Introduceti data :")
        tip = input("Introduceti tipul cheltuielii:")
        lst_cheltuieli = adaugare(lst_cheltuieli, id_ap, nr_ap, suma, data, tip)
    except ValueError as ve:
        print("Eroare:",ve)
    return lst_cheltuieli


def user_interface_all(lst_cheltuieli):
    for x in lst_cheltuieli:
        print(get_str(x))


def user_interface_modif(lst_cheltuieli):
    try:
        id_ap = int(input("Introduceti id-ul cheltuielii care doriti sa se modifice:"))
        nr_ap = int(input("Dati nr apartamentului  "))
        suma = int(input("Dati noua suma a cheltuielii: "))
        data = input("Dati noua data a cheltuielii:")
        tip = input("Dati noul tip al cheltuielii:")
        cheltuiala_noua = creeaza_cheltuiala(id_ap, nr_ap, suma, data, tip)
        lst_cheltuieli = modif(lst_cheltuieli, cheltuiala_noua)
    except ValueError as ve:
        print("Eroare", ve)
    return lst_cheltuieli


def user_interface_delete(lst_cheltuieli):
    try:
        id_ap = int(input("Dati id-ul cheltuielii care sa se modifice: "))
        lst_cheltuieli = stergere(lst_cheltuieli, id_ap)
    except ValueError as ve:
        print("Eroare",ve)
    else:
        print("Cheltuiala s-a sters !")
    return lst_cheltuieli

def user_interface_sterge_cheltuieli_nr_ap(lst_cheltuieli):
    try:
        nr_ap = int(input("Indorduceti nr ap :"))
        lst_cheltuieli = sterge_cheltuieli_nr_ap(lst_cheltuieli,nr_ap)
    except ValueError as ve:
        print("Eroare",ve)
    else:
        print(f"Cheltuiala s-a sters cu succes!")
    return lst_cheltuieli

def user_interface_adaugare_val_dat(lst_cheltuieli):
    try:
        data = input("Dati o data dupa care se cauta cheltuiala :")
        val = int(input("Dati valoarea care se adauga"))
        lst_cheltuieli = adaugare_val_data(lst_cheltuieli,data,val)
    except ValueError as ve:
        print("Eroare",ve)
    else:
        print("Valoarea a fost schimbata cu succes")
    return lst_cheltuieli

def user_interface_cea_mai_mare_cheltuiala(lst_cheltuiala):
    rezultat = cea_mai_mare_cheltuiala(lst_cheltuiala)
    for tip in rezultat:
        print(f"Pentru tipul {tip} avem chltuiala:  {get_str(rezultat[tip])}")

def user_interface_ordonare_descrescatr(lst_cheltuiala):
    lst_cheltuiala = ordonare(lst_cheltuiala)
    print("Ordonarea s-a facut cu succes")
    return lst_cheltuiala

def user_interface_crud(lst_cheltuieli):

    while True:
        menu()

        optiune = input("Dati o optiune: ")
        if optiune == "1":
            lst_cheltuieli = user_interface_add(lst_cheltuieli)
        elif optiune == "2":
            lst_cheltuieli = user_interface_modif(lst_cheltuieli)
        elif optiune == "3":
            lst_cheltuieli = user_interface_delete(lst_cheltuieli)
        elif optiune == "4":
            lst_cheltuieli = user_interface_sterge_cheltuieli_nr_ap(lst_cheltuieli)
        elif optiune == "5":
            lst_cheltuieli = user_interface_adaugare_val_dat(lst_cheltuieli)
        elif optiune == "6":
            lst_cheltuieli = user_interface_cea_mai_mare_cheltuiala(lst_cheltuieli)
        elif optiune == "7":
            lst_cheltuieli = user_interface_ordonare_descrescatr(lst_cheltuieli)
        elif optiune == "a":
            user_interface_all(lst_cheltuieli)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita, reincercati")
    return lst_cheltuieli


def menu_command():
    print("1. add, id , nr_ap, cheltuieli ,data, tip")
    print("2. stergere id")
    print("3. max_cheltuiala")
    print("4. show_all")

def user_interface_command(lst_cheltuieli):
    menu_command()
    optiune= input("alegeti o optiune:")
    comanda=optiune.split(";")
    for comanda in comanda:
        com = comanda.split(",")
        if com[0]== "add":
            try:
                lst_cheltuieli= adaugare(com[1],com[2],com[3],com[4],com[5],lst_cheltuieli)
            except ValueError as ve:
                print("Eroare",ve)
        elif com[0]=="sterge":
            lst_cheltuieli= stergere(com[1],lst_cheltuieli)
        elif com[0]=="max_mcheltuiala":
            print(cea_mai_mare_cheltuiala(lst_cheltuieli))
        elif com[0]=="show_all":
            print(user_interface_all(lst_cheltuieli))
        else:
            raise ValueError("Optiune invaida")


