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