DB_HOST = "postgres"
DB_NAME = "postgres" 
DB_USER = "postgres" 
DB_PASS = "postgres"

import psycopg2
import psycopg2.extras

conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS)

cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

cur.execute("CREATE TABLE IF NOT EXISTS htmltagsinfo (id SERIAL PRIMARY KEY, link VARCHAR, tagsquantity integer)")

cur.execute("insert into htmltagsinfo (link, tagsquantity) VALUES (%s, %s)", ("asdfasdf", 1, ))
cur.execute("insert into htmltagsinfo (link, tagsquantity) VALUES (%s, %s)", ("asdfasdf", 1, ))
cur.execute("select * from htmltagsinfo where id=1")
cur.execute("select * from htmltagsinfo")
print(cur.fetchall())



conn.commit()