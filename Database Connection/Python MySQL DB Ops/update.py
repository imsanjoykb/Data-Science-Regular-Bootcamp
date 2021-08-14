import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="employee_data",
)

cursor = db.cursor()
sql = "UPDATE customers SET name=%s, address=%s WHERE customer_id=%s"
val = ("ShakibAL", "Dhaka", 2)
cursor.execute(sql, val)

db.commit()

print("{} data changed".format(cursor.rowcount))