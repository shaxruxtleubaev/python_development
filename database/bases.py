import psycopg2
from config import host
from config import user
from config import password
from config import db_name

try:
    #Попоробуем подключиться к БД
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
except Exception as e:
    print(f"[INFO] Ошибка при подключений")
finally:
    if connection:
        connection.close()
        print(f'[INFO] Соединение с БД отключено')