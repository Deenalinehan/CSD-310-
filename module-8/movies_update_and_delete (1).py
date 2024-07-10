#Deena Linehan
#Assignment 8.2
#07/06/2024

import mysql.connector

def show_films(cursor, title):
    query = """
        SELECT film_name AS Name, film_director AS Director,
               genre_name AS Genre, studio_name AS 'Studio Name'
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """
    cursor.execute(query)
    films = cursor.fetchall()
    
    print("\n -- {} --".format(title))
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre: {}\nStudio Name: {}\n".format(
            film[0], film[1], film[2], film[3]))

cnx = mysql.connector.connect(
    user='movies_user',
    password='popcorn',
    host='localhost',
    database='movies'
)

# Create cursor object
cursor = cnx.cursor()

# Step 5
show_films(cursor, "DISPLAYING FILMS")

# Step 6
cursor.execute("SELECT studio_id FROM studio WHERE studio_name = 'Universal Pictures'")
studio_id = cursor.fetchone()[0]

cursor.execute("SELECT genre_id FROM genre WHERE genre_name = 'Horror'")
genre_id = cursor.fetchone()[0]

new_film_data = ("The Invisible Man", "2020", 124, "Leigh Whannell", studio_id, genre_id)
insert_query = """
    INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) 
    VALUES (%s, %s, %s, %s, %s, %s)
"""
cursor.execute(insert_query, new_film_data)
cnx.commit()

# Step 7
show_films(cursor, "AFTER INSERTING NEW FILM")

# Step 8
update_query = """
    UPDATE film 
    SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror')
    WHERE film_name = 'Alien'
"""
cursor.execute(update_query)
cnx.commit()

# Step 9
show_films(cursor, "AFTER UPDATING 'Alien' TO HORROR FILM")

# Step 10
delete_query = "DELETE FROM film WHERE film_name = 'Gladiator'"
cursor.execute(delete_query)
cnx.commit()

# Step 11
show_films(cursor, "AFTER DELETING 'Gladiator'")

# Close cursor and connection
cursor.close()
cnx.close()
