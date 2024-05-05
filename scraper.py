import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='swapadmin',
    password='DAAdckljda!?zlkj97987',
    database='scrapswap'
)

#USE scrapswap;
# CREATE TABLE sneakers (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     nom VARCHAR(255),
#     marque VARCHAR(255),
#     photo VARCHAR(255),
#     date_sortie DATE
# );

def insert_data(nom, marque, photo, date_sortie):
    cursor = conn.cursor()
    cursor.execute(f'''INSERT INTO sneakers (nom, marque, photo, date_sortie) VALUES ('{nom}', '{marque}', '{photo}', '{date_sortie}');''')
    conn.commit()

def display_data():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sneakers;")
    for row in cursor.fetchall():
        print(row)


