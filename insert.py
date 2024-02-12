import sqlite3
conn = sqlite3.connect('example.db')
print("opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (1,'FAITH KARIMI',23,3450000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2,'BOB KURIA',32,1500000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (3,'JANE MUTHONI',27,450000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4,'JAMES MAKOSA',51,3500000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (5,'PAUL KAMAU',45,50000.00)")

conn.commit()
print("Records inserted Successfully")
conn.close()
