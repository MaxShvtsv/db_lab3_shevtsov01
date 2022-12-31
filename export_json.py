import json
import os
import psycopg2

username = 'postgres'
password = '133451'
database = 'mobiles'
host = 'localhost'
port = '5432'

query_phones = """
SELECT *
FROM phones
"""

query_customers = """
SELECT *
FROM customers
"""

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
cur = conn.cursor()

cwd = os.path.dirname(os.path.realpath(__file__))

data = {}

cur.execute(query_phones)

cur = conn.cursor()

cur.execute(query_phones)
rows = []
fields = [x[0] for x in cur.description]
for row in cur:
    rows.append(dict(zip(fields, row)))

data['phones'] = rows

cur.execute(query_customers)
rows = []
fields = [x[0] for x in cur.description]
for row in cur:
    rows.append(dict(zip(fields, row)))

data['customers'] = rows

with open(os.path.join(cwd, 'data.json'), 'w') as f:
    json.dump(data, f, default=str)
