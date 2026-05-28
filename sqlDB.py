import pymysql
from dotenv import load_dotenv
import os
from queries import *

load_dotenv()

class DB:
    def __init__(self):
        self.__config = {"host": os.getenv("DB_HOST"),
                         "user": os.getenv("DB_USER"),
                         "password": os.getenv("DB_PASSWORD"),
                         "database": os.getenv("DB_NAME")}


    def __enter__(self):
        self.__conn = pymysql.connect(**self.__config)
        self.__cursor = self.__conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__cursor.close()
        self.__conn.close()
        return False

    def _execute(self, sql, params=None):
        self.__cursor.execute(sql, params)
        self.__conn.commit()
        return self.__cursor.fetchall()


    def film_finder(self, film_name):
        return self._execute(SELECT_FILM,(f"% {film_name}%",))

    def print_genre(self):
        for i,item in  enumerate(self._execute(SELECT_GENRE), start=1):
            print(f"{i}. {item[0]}")

    def film_by_genre(self, id_genre):
        return self._execute(SELECT_FILM_BY_GENRE, (id_genre,))

    def film_by_genre_and_year(self, id_genre, year):
        return self._execute(SELECT_FILM_BY_GENRE_AND_YEAR, (id_genre, year))


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
    film_year = input("Хотите ли сделать поиск по году выпуска? (y/n) ").strip().lower()
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
