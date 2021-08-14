import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE employee_data")

print("Database Created Successful !!!")