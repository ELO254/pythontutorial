import sqlite3
conn = sqlite3.connect("mid morning")
print("open database successfuly")
conn.execute("INSERT INTO wanafunz(ID,NAME,AGE,SCHOOL,GENDER)VALUES (1,'ELVIS',18,'EMOBILIS','MALE')")
conn.execute("INSERT INTO wanafunz(ID,NAME,AGE,SCHOOL,GENDER)VALUES (2,'JOHN',12,'EMOBILIS','MALE')")
conn.execute("INSERT INTO wanafunz(ID,NAME,AGE,SCHOOL,GENDER)VALUES (3,'COLLINCE',21,'KCA','MALE')")
conn.execute("INSERT INTO wanafunz(ID,NAME,AGE,SCHOOL,GENDER)VALUES (4,'VINCENT',18,'EMOBILIS','MALE')")
conn.execute("INSERT INTO wanafunz(ID,NAME,AGE,SCHOOL,GENDER)VALUES (5,'ROSE',18,'EMOBILIS','FEMALE')")
conn.execute("INSERT INTO wanafunz(ID,NAME,AGE,SCHOOL,GENDER)VALUES (6,'jane',18,'EMOBILIS','FEMALE')")

conn.commit()
print("records are added")
conn.close()