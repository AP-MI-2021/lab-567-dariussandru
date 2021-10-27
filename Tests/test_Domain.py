from Domain.cheltuieli import getId, creeazaCheltuieli, getNrApartament, getSuma, getData, getTip


def testCheltuieli():
    cheltuieli = creeazaCheltuieli("1", 8, 150, 12 / 23 / 2021, "gaz")

    assert getId(cheltuieli) == "1"

    assert getSuma(cheltuieli) == 150
    assert getData(cheltuieli) == 12/23/2021
    assert getTip(cheltuieli) == "gaz"