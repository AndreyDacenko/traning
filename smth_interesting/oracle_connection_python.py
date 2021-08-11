import cx_Oracle


username = 'hr'
password = 'hr2020'
# dsn = """(DESCRIPTION =
#     (ADDRESS = (PROTOCOL = TCP)(HOST = 185.12.95.186)(PORT = 1521))
#     (CONNECT_DATA =
#       (SERVER = DEDICATED)
#       (SERVICE_NAME = xepdb1)
#     )
#   )"""
# dsn = '185.12.95.186'
# port = 1521

""" connection install """
connection = cx_Oracle.connect(
    username,
    password,
    dsn='xepdb1',
    encoding="UTF-8"
)

# print(conn.version)
cursor = connection.cursor()


cars = cursor.execute("""
SELECT regnum, color, phonenum
FROM auto
WHERE mark = 'BMW'
""")
for row in cars:
    print(row)


connection.close()