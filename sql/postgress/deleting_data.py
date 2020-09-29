import psycopg2


DB_NAME = 'ziebamhc'
DB_USER = 'ziebamhc'
DB_PASS = '2xDluopdmVTBq1sC9OJSJ88OeFkIbWLX'
DB_HOST = 'lallah.db.elephantsql.com'
DB_PORT = '5432'


conn = psycopg2.connect(database= DB_NAME, user= DB_USER, password= DB_PASS, host= DB_HOST, port= DB_PORT)
print('Connected')
cur = conn.cursor()

cur.execute("DELETE FROM Emploee WHERE ID = 1")
conn.commit()

print(f'count deleted rows: {cur.rowcount}')
print('rows in data deleted')
conn.close()