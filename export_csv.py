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

to_csv_phones = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query_phones)
to_csv_customers = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query_customers)

cwd = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(cwd, 'phones.csv'), 'w') as f:
    cur.copy_expert(to_csv_phones, f)

with open(os.path.join(cwd, 'customers.csv'), 'w') as f:
    cur.copy_expert(to_csv_customers, f)

conn.close()