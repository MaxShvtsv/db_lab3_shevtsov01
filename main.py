import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import psycopg2

username = 'postgres'
password = '133451'
database = 'mobiles'
host = 'localhost'
port = '5432'

query_1 = '''
CREATE VIEW Mobiles_features_main AS
SELECT phone_id, label, int_memory
FROM phones
'''
query_2 = '''
CREATE VIEW Mobiles_customers AS
SELECT customers.country, COUNT(*) AS phone_count
FROM customers, phones
WHERE customers.phone_id = phones.phone_id
GROUP BY customers.country
'''

query_3 = '''
CREATE VIEW Mobiles_customers_age AS
SELECT phones.phone_id, phones.label, customers.cust_name, customers.age
FROM phones, customers
WHERE customers.phone_id = phones.phone_id AND customers.age > 20
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:

    print ("Database opened successfully")

    print('1.  \n')

    cur_1 = conn.cursor()

    cur_1.execute('DROP VIEW IF EXISTS Mobiles_features_main')
    cur_1.execute(query_1)
    cur_1.execute('SELECT * FROM Mobiles_features_main')
    df_1 = pd.DataFrame(cur_1.fetchall(), columns=['phone_id', 'label', 'int_memory'])

    print(df_1)

    print('2.  \n')

    cur_2 = conn.cursor()

    cur_2.execute('DROP VIEW IF EXISTS Mobiles_customers')
    cur_2.execute(query_2)
    cur_2.execute('SELECT * FROM Mobiles_customers')
    df_2 = pd.DataFrame(cur_2.fetchall(), columns=['country', 'phone_count'])

    print(df_2)

    print('3.  \n')

    cur_3 = conn.cursor()

    cur_3.execute('DROP VIEW IF EXISTS Mobiles_customers_age')
    cur_3.execute(query_3)
    cur_3.execute('SELECT * FROM Mobiles_customers_age')
    df_3 = pd.DataFrame(cur_3.fetchall(), columns=['phone_id', 'label', 'cust_name', 'age'])

    print(df_3)

    # Visualization
    fig, axs = plt.subplots(3, figsize=(10, 10))
    # Query 1 - Histogram
    axs[0].bar(df_1['label'], df_1['int_memory'])

    axs[0].set_yticks(list(range(0, df_1['int_memory'].max() + 10, 5)))

    axs[0].set_xlabel('Label')
    axs[0].set_ylabel('Int Memory')
    axs[0].set_title('Query 1')

    axs[0].grid(axis='y')

    chartBox = axs[0].get_position()
    axs[0].set_position([chartBox.x0, chartBox.y0,
                         chartBox.width * 0.6,
                         chartBox.height])

    # # Query 2 - Pie Diagram

    labels = df_2['country']
    sizes = df_2['phone_count']

    axs[1].pie(sizes, labels=labels, autopct='%1.1f%%')

    axs[1].set_title('Query 2')

    chartBox = axs[1].get_position()
    axs[1].set_position([chartBox.x0 + 0.15, chartBox.y0,
                         chartBox.width * 2,
                         chartBox.height * 2])

    # Query 3 - Scatter

    axs[2].scatter(df_3['cust_name'] + '\\' + df_3['label'], df_3['age'])

    axs[2].set_xlabel('Customer Name/Phone Label')
    axs[2].set_ylabel('Age')
    axs[2].set_title('Query 3')

    axs[2].grid()

    chartBox = axs[2].get_position()
    axs[2].set_position([chartBox.x0, chartBox.y0 + 0.15,
                         chartBox.width * 0.6,
                         chartBox.height])

    plt.show()
