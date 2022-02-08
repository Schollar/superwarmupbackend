import dbcreds
import mariadb as db


def db_connect():
    conn = None
    cursor = None
    try:
        conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                          host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
    except db.OperationalError:
        print('Something is wrong with the DB')
    except:
        print('Something went wrong connecting to the DB')
    return conn, cursor
# Disconnect function that takes in the conn and cursor and attempts to close both


def db_disconnect(conn, cursor):
    try:
        cursor.close()
    except:
        print('Error closing cursor')
    try:
        conn.close()
    except:
        print('Error closing connection')
# Get animal function gets the animal name and description from animals table in DB


def get_heros():
    heros = []
    conn, cursor = db_connect()
    try:
        cursor.execute(
            "SELECT id, name, secret_identity, powers, power_rating, image_url FROM hero")
        heros = cursor.fetchall()
    except db.OperationalError:
        print('Something is wrong with the db!')
    except db.ProgrammingError:
        print('Error running DB query')
    db_disconnect(conn, cursor)

    return heros


def get_villians():
    villians = []
    conn, cursor = db_connect()
    try:
        cursor.execute(
            "SELECT id, name, secret_identity, powers, power_rating, image_url FROM villian")
        villians = cursor.fetchall()
    except db.OperationalError:
        print('Something is wrong with the db!')
    except db.ProgrammingError:
        print('Error running DB query')
    db_disconnect(conn, cursor)

    return villians
