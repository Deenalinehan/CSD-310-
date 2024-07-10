#Deena Linehan
#Assingment 7.1
#07/04/2024

import mysql.connector
from mysql.connector import errorcode

def connect_to_db():
    config = {
        "user": "movies_user",
        "password": "popcorn",
        "host": "127.0.0.1",
        "database": "movies",
        "raise_on_warnings": True
}

    try:
        db = mysql.connector.connect(**config)
        print("\n Database user{} connected to MySQL on host{} with database{}". format(config["user"], config["host"], config["database"]))
        input("\n\n Press any key to continue...")
        return db

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(" The supplied username or password are invalid")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(" The specified database does not exist")

        else:
            print(err)
        return None

def close_connection(db):
    if db:
        db.close()
        print('Connection closed')


def query_studio_records(db):
    cursor = db.cursor()
    cursor.execute('SELECT studio_id, studio_name FROM studio')
    studios = cursor.fetchall()
    cursor.close()
    return studios

def query_genre_records(db):
    cursor = db.cursor()
    cursor.execute('SELECT genre_id, genre_name FROM genre')
    genres = cursor.fetchall()
    cursor.close()
    return genres

def query_short_film_records(db):
    cursor = db.cursor()
    cursor.execute('SELECT film_name, film_runtime FROM film WHERE film_runtime < 120')
    short_films = cursor.fetchall()
    cursor.close()
    return short_films

def query_director_records(db):
    cursor = db.cursor()
    cursor.execute('SELECT film_name, film_director FROM film ORDER BY film_director')
    directors = cursor.fetchall()
    cursor.close()
    return directors

def main():
    db = connect_to_db()
    if not db:
        print('Failed to connect to the database. Exiting...')
        return

    print("-- Studio Records --")
    studios = query_studio_records(db)
    for studio in studios:
        print(f"Studio ID: {studio[0]}\nStudio Name: {studio[1]}")
    print()

    print("-- Genre Records --")
    genres = query_genre_records(db)
    for genre in genres:
        print(f"Genre ID: {genre[0]}\nGenre Name: {genre[1]}")
    print()

    print("-- Short Films --")
    short_films = query_short_film_records(db)
    for film in short_films:
        print(f"Film Name: {film[0]}\nRun Time: {film[1]}")
    print()

    print("-- Director Records --")
    directors = query_director_records(db)
    for film in directors:
        print(f"Film Name: {film[0]}\nDirector: {film[1]}")

    close_connection(db)

if __name__ == "__main__":
    main()



