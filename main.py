from sqlDB import *
from ui import *

def main():
    with DB() as db:
        menu = Menu(["Поиск по ключевому слову","Поиск по жанру и году","Популярные запросы","История запросов","Выход"])
        while True:
            match menu.show():
                case 5:
                    print("До новых встреч")
                    break








if __name__ == '__main__':
    main()