import mysql.connector
import os

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="employee_data",
)


def insert_data(db):
  name = input("Enter Name: ")
  address = input("Enter Address: ")
  val = (name, address)
  cursor = db.cursor()
  sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} data Inserted".format(cursor.rowcount))


def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM customers"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("There is not any data")
  else:
    for data in results:
      print(data)


def update_data(db):
  cursor = db.cursor()
  show_data(db)
  customer_id = input("Choose id customer> ")
  name = input("New Name: ")
  address = input("New Address: ")

  sql = "UPDATE customers SET name=%s, address=%s WHERE customer_id=%s"
  val = (name, address, customer_id)
  cursor.execute(sql, val)
  db.commit()
  print("{} data successfully changed".format(cursor.rowcount))


def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  customer_id = input("Choose id customer> ")
  sql = "DELETE FROM customers WHERE customer_id=%s"
  val = (customer_id,)
  cursor.execute(sql, val)
  db.commit()
  print("{} data successfully deleted".format(cursor.rowcount))


def search_data(db):
  cursor = db.cursor()
  keyword = input("Keyword: ")
  sql = "SELECT * FROM customers WHERE name LIKE %s OR address LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("There is not any data")
  else:
    for data in results:
      print(data)


def show_menu(db):
  print("=== APPLICATION DATABASE PYTHON ===")
  print("1. Insert Data")
  print("2. Show Data")
  print("3. Update Data")
  print("4. Delete Data")
  print("5. Search Data")
  print("0. GO Out")
  print("------------------")
  menu = input("Choose menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    update_data(db)
  elif menu == "4":
    delete_data(db)
  elif menu == "5":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu WRONG!")


if __name__ == "__main__":
  while(True):
    show_menu(db)