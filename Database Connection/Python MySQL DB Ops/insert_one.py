import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="employee_data",
)

cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Mr Taif", "Dhaka")
cursor.execute(sql, val)

db.commit()

print("{} data added".format(cursor.rowcount))