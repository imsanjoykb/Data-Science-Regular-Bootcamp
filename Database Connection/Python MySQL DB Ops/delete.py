import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="employee_data",
)

cursor = db.cursor()
sql = "DELETE FROM customers WHERE customer_id=%s"
val = (4, )
cursor.execute(sql, val)

db.commit()

print("{} data deleted".format(cursor.rowcount))