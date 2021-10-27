def creeaza_cheltuiala(id, nr_apartament, suma, data, tipul):
    """
    se formeaza o lista
    :param nr_apartament:int
    :param suma:float
    :param data:float
    :param tipul:str
    :return: creeaza cheltuiala cu datele introduse
    """
    """
    return {
        "id": id,
        "nr_ap": nr_apartament,
        "suma": suma,
        "data": data,
        "tip": tipul,
    } """
    return (id,nr_apartament,suma,data,tipul)


def get_id(cheltuiala):
    #return cheltuiala["id"]
    return cheltuiala[0]

def get_nr_ap(cheltuiala):
    #return cheltuiala["nr_ap"]
    return cheltuiala[1]

def get_suma(cheltuiala):
    #return cheltuiala["suma"]
    return cheltuiala[2]

def get_data(cheltuiala):
    #return cheltuiala["data"]
    return cheltuiala[3]

def get_tipul(cheltuiala):
    #return cheltuiala["tip"]
    return cheltuiala[4]

def get_str(cheltuiala):
    return "Id-ul cheltuielii este {} cu nr de apartament {},are suma {},la data {} pentru tipul {}}".format(
        get_id(cheltuiala),
        get_nr_ap(cheltuiala),
        get_suma(cheltuiala),
        get_data(cheltuiala),
        get_tipul(cheltuiala)
    )
