import sqlite3 as lite
import sys


postid = '1'



con = lite.connect('orders.db')
cur = con.cursor()
data = cur.fetchall()

cur.execute("select userid from users where userid=?", (postid,))

if not data:
	print("kek")
else:
	print("hib")