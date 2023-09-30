import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Karios___254",
)

# prepare cursor object
cursorObject = database.cursor()

# creating DB
cursorObject.execute("CREATE DATABASE kariosCRM")

print("Done")
