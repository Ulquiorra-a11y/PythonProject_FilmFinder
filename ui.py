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


def search_film(db):
    while True:
        try:
            film_name = input("Введите название фильма или ключевое слово: ").strip()
            if not film_name:
                raise ValueError("Поле не должно быть пустым")
            films = db.film_finder(film_name)
            if not films:
                print("Фильмы не найдены")
                return
            for i, title in enumerate(films, start=1):
                print(f"{i}. {title[0]}")
            return
        except ValueError as e:
            print(e)


def search_category(db):
    db.print_genre()
    id_genre = int(input("Выберите жанр: "))
    while True:
        film_year = input("Хотите ли сделать поиск по году выпуска? (y/n) ").strip().lower()
        if film_year in ("y", "n"):
            break
        print("Введите 'y' или 'n'.")
    if film_year == "y":
        input_year = int(input("Введите желаемый год: "))
        films = db.film_by_genre_and_year(id_genre, input_year)
    else:
        films = db.film_by_genre(id_genre)
    if films:
        for i in films:
            print(i[0])
    else:
        print("Фильмы не найдены")

    return