from Domain.cheltuieli import get_suma


def ordonare(lista):
    return sorted(lista , key=get_suma, reverse = True)