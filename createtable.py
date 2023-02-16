import sqlite3
conn = sqlite3.connect("mid morning")
print("open database successfuly")
conn.execute("CREATE TABLE wanafunz ("
             "ID INT PRIMARY KEY NOT NULL,"
             "NAME TEXT NOT NULL,"
             "AGE INIT NOT NULL,"
             "SCHOOL TEXT INIT NOT NULL,"
             "GENDER TEXT NOT NULL)")
print("table created success")
conn.close()