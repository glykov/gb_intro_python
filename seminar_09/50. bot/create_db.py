import sqlite3

conn = sqlite3.connect("phonebook.db")
cursor = conn.cursor()
cursor.execute("drop table if exists people")
cursor.execute("create table people(id integer primary key, last_name text, first_name text, phone text, description text)")
cursor.execute("insert into people(last_name, first_name, phone, description) values(?, ?, ?, ?)",
            ("Иванов", "Иван", "111", "очень любит заполнять бланки"))
cursor.execute("insert into people(last_name, first_name, phone, description) values(?, ?, ?, ?)",
            ("Петров", "Петр", "222", "не любит анекдоты про Чапаева"))
cursor.execute("insert into people(last_name, first_name, phone, description) values(?, ?, ?, ?)",
            ("Васичкина", "Василиса", "333", "украшает офис"))
cursor.execute("insert into people(last_name, first_name, phone, description) values(?, ?, ?, ?)",
            ("Змиев", "Антон", "444", "умеет в Питон"))
# result = cursor.execute("select * from people")
# for row in result:
#     print(row)
conn.commit()
conn.close()