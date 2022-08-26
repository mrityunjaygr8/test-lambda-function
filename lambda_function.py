import socket
import os
import psycopg2 

def lambda_handler(event, context):   
    # replace the os.getenv calls with the correct config for the DB
    DB_NAME = os.getenv("DB_NAME", "postgres")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASS = os.getenv("DB_PASS", "postgres")
    ip = socket.gethostbyname(DB_HOST)
    conn = psycopg2.connect(
        user=DB_USER, password=DB_PASS, host=DB_HOST, port="5432", database=DB_NAME
    )
    SELECT_QUERY = """
    SELECT * FROM django_migrations;
    """
    # SELECT_QUERY = f"""select * from public.comm_otpreason"""
    cursor = conn.cursor()
    cursor.execute(SELECT_QUERY)
    data = cursor.fetchone()
    # print(str(data))
    return {
        "ip": ip,
        "data": str(data),
    }
