import psycopg2
from contextlib import contextmanager


@contextmanager
def create_connection():
    try:
        conn = psycopg2.connect(host='localhost', database='WEB_6', user='postgres', password='mysecretpassword')
        yield conn
        conn.close()
    except psycopg2.OperationalError as err:
        raise RuntimeError(f'Failed to create database connection{err}')
    