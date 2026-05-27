class Menu:
    def __init__(self, items: list):
        self.items = items

    def show(self):
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item}")
        while True:
            try:
                user_input= int(input("Введите пункт:"))
                if 0 < user_input <= len(self.items):
                    return user_input
                raise ValueError
            except ValueError:
                print("Неверное значение")