from Tests.all_tests import run_all_tests
from Tests.test_undo_redo import test_undo_redo_lab
from User_Interface.console import  run_ui

def main():
    run_all_tests()
    test_undo_redo_lab()
    run_ui()


if __name__ == '__main__':
    main()