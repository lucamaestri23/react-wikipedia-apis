import mysql.connector
import os


def db_connection():
    try:
        host = os.getenv("MYSQL_URL")
        user = os.getenv("MYSQL_USER")
        password = os.getenv("MYSQL_PASSWORD")
        database_name = os.getenv("MYSQL_DATABASE")
        port = os.getenv("MYSQL_PORT")

        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database_name,
            port=port
        )

        mycursor = mydb.cursor()

        return mydb, mycursor

    except Exception:
        msg = "Could not connect to DB"
        print(msg)
        # return(failed_json(msg))
