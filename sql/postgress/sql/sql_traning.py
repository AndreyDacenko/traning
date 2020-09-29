import sqlite3


conn = sqlite3.connect('Chinook_Sqlite.sqlite')
# Укажем тип получаемых данных
conn.text_factory = bytes
# Создадим курсор - специальный объект, с помощью которого мы сможем делать запросы к БД на языке запросов
cursor = conn.cursor()

conn.close()