import psycopg2


DB_NAME = 'ziebamhc'
DB_USER = 'ziebamhc'
DB_PASS = '2xDluopdmVTBq1sC9OJSJ88OeFkIbWLX'
DB_HOST = 'lallah.db.elephantsql.com'
DB_PORT = '5432'


conn = psycopg2.connect(database= DB_NAME, user= DB_USER, password= DB_PASS, host= DB_HOST, port= DB_PORT)

print('Connected')

cur = conn.cursor()
cur.execute("SELECT ID, NAME, EMAIL FROM Emploee")

rows = cur.fetchall()

for data in rows:
    print(f'ID : {data[0]}')
    print(f'NAME : {data[1]}')
    print(f'EMAIL : {data[2]}')

conn.close()
print('\ndata selected')

