from Domain.cheltuieli import creeaza_cheltuiala, get_id

def cifre(sir):
    """

    :param sir:
    :return:
    """
    lst_cifre = ["0","1","2","3","4","5","6","7","8","9"]
    for litera in sir:
        if litera not in lst_cifre:
            return False
    return True

def format_data(data):
    """

    :param data:
    :return:
    """
    data_split = data.split(".")
    if len(data_split[0]) != 2 or len(data_split[1]) !=2 or len(data_split[2])!=4:
        raise ValueError(f'Data cheltuielii nu este corecta')
    if cifre(data_split[0])==False or cifre(data_split[1]) == False or cifre(data_split[2])== False:
        raise ValueError(f'Data cheltuielii nu este corecta')
    zi= int(data_split[0])
    luna = int(data_split[1])
    if(luna%2==0 and zi >30) or (luna%2 == 1 and zi>31) or (luna == 2 and zi >28):
        raise ValueError(f'Data cheltuielii nu este corecta')

def adaugare(lst_cheltuieli, id, nr_ap, suma, data, tip, undo_list, redo_list):
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
    if id < 0:
        raise ValueError(f"Id-ul {id} introdus nu este valabil")
    if read(lst_cheltuieli,id) is None:
        raise ValueError(f"Exista o cheltuiala cu id {id} introdus")
    if nr_ap < 0:
        raise ValueError(f"Numarul apartamentului nu este valid")
    format_data(data)
    if tip != "canal" and tip != "intretinere" and tip !="alte cheltuieli":
        raise ValueError(f'Tipul cheltuielii este gresit')
    cheltuiala_noua = creeaza_cheltuiala(id, nr_ap, suma, data, tip)
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return lst_cheltuieli + [cheltuiala_noua]


def stergere(lst_cheltuieli, id , undo_list , redo_list ):
    """
    se sterge din lista cheltuiala cu id = cu id-ul citit de la tastatura
    :param lst_cheltuieli: lista de cheltuieli
    :param id: id-ul unei cheltuieli
    :return: lista dupa elimiminearea unei cheltuieli
    """
    if read(lst_cheltuieli,id) is None:
        raise ValueError(f"Nu exista o cheltuiala cu id-ul {id}")
    lista_noua_cheltuieli = []
    for x in lst_cheltuieli:
        if get_id(x) != id:
            lista_noua_cheltuieli.append(x)
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return lista_noua_cheltuieli


def modif(lst_cheltuieli, cheltuiala_noua, undo_list, redo_list):
    """
    se modifica lista in functie de un id citit de la tastatura
    :param lst_cheltuieli: lista de cheltuieli
    :param cheltuiala_noua: lista noua
    :return: lista dupa modificare
    """
    if read(lst_cheltuieli,get_id(cheltuiala_noua)) is None:
        raise ValueError(f"Nu exhista cheltuiala cu id-ul {id}")
    lista_noua_cheltuieli = []

    for x in lst_cheltuieli:
        if get_id(x) != get_id(cheltuiala_noua):
            lista_noua_cheltuieli.append(x)
        else:
            lista_noua_cheltuieli.append(cheltuiala_noua)
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return lista_noua_cheltuieli


def read(lst_cheltuieli, ap_id = None):
    """
    Functia verifica daca apare in lista de cheltuieli o anumita cheltuiala, cu id dat
    :param lst_cheltuieli:O lista de cheltueieli
    :param ap_id:Numarul apartamentului a cheltuielii
    :return:Returneaza cheltuiala cautata (daca exista in lista) sau toata lista daca nr_ap_cheltuiala = None
    """
    if ap_id is None:
        return lst_cheltuieli

    nr_ap_cheltuiala = 0
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) == ap_id:
            nr_ap_cheltuiala = cheltuiala
    if nr_ap_cheltuiala:
        return nr_ap_cheltuiala
    return lst_cheltuieli