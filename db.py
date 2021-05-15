import sqlite3
import random



num = random.randint(0, 100000)
number = "0000" + str(num)

name = input("Введите имя: ")
family = input("Введите фамилию: ")
pol = input("М/Ж: ")






#Подключение файла SQLite:

conn = sqlite3.connect('orders.db')
cur = conn.cursor()

#Создание таблицы SQLite:

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")
conn.commit()

#Добавление значения в таблицу:

user = (number, name, family, pol)

cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
conn.commit()