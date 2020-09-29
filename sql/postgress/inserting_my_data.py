import psycopg2


DB_NAME = 'ziebamhc'
DB_USER = 'ziebamhc'
DB_PASS = '2xDluopdmVTBq1sC9OJSJ88OeFkIbWLX'
DB_HOST = 'lallah.db.elephantsql.com'
DB_PORT = '5432'


conn = psycopg2.connect(database= DB_NAME, user= DB_USER, password= DB_PASS, host= DB_HOST, port= DB_PORT)

print('Connected')

cur = conn.cursor()
cur.execute("INSERT INTO Emploee (ID, NAME, EMAIL) VALUES(1, 'Vasisily', 'vasily@gmail.com')")
conn.commit()
print('data inserted')
conn.close()