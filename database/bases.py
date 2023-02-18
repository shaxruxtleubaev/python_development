import psycopg2
from config import host, user, password, db_name

try:
    #Попоробуем подключиться к БД
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
except Exception as e_:
    print(f"[INFO] Ошибка при подключений")
finally:
    if connection:
        connection.close()
        print(f'[INFO] Соединение с БД отключено')
