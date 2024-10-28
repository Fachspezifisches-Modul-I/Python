import sqlite3

connection = sqlite3.connect('erste_db.db')

cursor = connection.cursor()

# cursor.execute('DROP TABLE IF EXISTS person')
cursor.execute('CREATE TABLE IF NOT EXISTS person(id int, name text, age int)')

# Dateien einfügen INSERT INTO person VALUES (81, 'David', 37)
cursor.execute('INSERT INTO person VALUES (3, "Arthudituh", 49)')

connection.commit()


cursor.execute('SELECT * FROM person')
datensaetze = cursor.fetchall()

for datensatz in datensaetze:
    print(datensatz)


connection.close()



 

# DQL > Data Query Language
# DML > Data Manipulation Language
# TCL > Transaction Control Language

# Transaktionen
# Konto1 = 10€; Konto2 = 10€ -> 5€ Überwiesen
# Konto1: 5€ abziehen; Konto2: 5€ hinzufügen


# DDL > Data Definition Language (CREATE, ALTER, DROP)
# DCL > (Nicht in SQLite) Data Control Language (GRANT, REVOKE)

# SQL > Struktured Query Language
# DML, DCL, DML, DQL, TCL
