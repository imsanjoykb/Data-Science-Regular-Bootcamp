import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="employee_data",
)

cursor = db.cursor()
sql = """CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  address Varchar(255)
)
"""
cursor.execute(sql)

print("Table Created Successful !!!")