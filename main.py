from Tests.test_Crud import test_crud
from User_Interface.console import user_interface_crud


def main():
    lst_cheltuieli = []
    user_interface_crud(lst_cheltuieli)


if __name__ == '__main__':
    test_crud()
    main()