from Tests.test_Crud import testAdaugaCheltuieli, testStergereCheltuieli
from Tests.test_Domain import testCheltuieli


def runAllTests():
    testCheltuieli()
    testAdaugaCheltuieli()
    testStergereCheltuieli()