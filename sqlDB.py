import pymysql
from dotenv import load_dotenv
import os


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