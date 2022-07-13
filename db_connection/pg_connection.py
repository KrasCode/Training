import psycopg2
from config_pg import host, user, password, db_name

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT version()'
        )
        print(f'Server sersion: {cursor.fetchone()[0]}')
except Exception as _ex:
    print(f'[INFO] Error while working with PostgreSQL {_ex}')
finally:
    if connection:
        connection.close()
        print(f'[INFO] PostgreSQL connection closed')
