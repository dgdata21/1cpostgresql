# for all notes about getting data look at the file get_data.py
from full_analysis.queries_abc import *
import pandas as pd
import psycopg2 as ps2
from psycopg2 import extras

conn = ps2.connect(dbname='1c_postgresql',                     # your own credentials
                   host='1xx.2xx.9x.1xx',                      # host you need (where the base is)
                   user='user',                                # your own credentials
                   password='password',                        # your own credentials
                   cursor_factory=ps2.extras.DictCursor)

def query():
    data = []
    for i in record:
        data.append(dict(i))
    return data

with conn:
    with conn.cursor() as curs:
        curs.execute(query_abc_2021_1q)
        record = curs.fetchall()
    df_abc_2021_1q = pd.DataFrame(query())
with conn:
    with conn.cursor() as curs:
        curs.execute(query_abc_2021_2q)
        record = curs.fetchall()
    df_abc_2021_2q = pd.DataFrame(query())
with conn:
    with conn.cursor() as curs:
        curs.execute(query_abc_2021_3q)
        record = curs.fetchall()
    df_abc_2021_3q = pd.DataFrame(query())
with conn:
    with conn.cursor() as curs:
        curs.execute(query_abc_2021_4q)
        record = curs.fetchall()
    df_abc_2021_4q = pd.DataFrame(query())


with conn:
    with conn.cursor() as curs:
        curs.execute(query_abc_2022_1q)
        record = curs.fetchall()
    df_abc_2022_1q = pd.DataFrame(query())
with conn:
    with conn.cursor() as curs:
        curs.execute(query_abc_2022_2q)
        record = curs.fetchall()
    df_abc_2022_2q = pd.DataFrame(query())
with conn:
    with conn.cursor() as curs:
        curs.execute(query_abc_2022_3q)
        record = curs.fetchall()
    df_abc_2022_3q = pd.DataFrame(query())
with conn:
    with conn.cursor() as curs:
        curs.execute(query_abc_2022_4q)
        record = curs.fetchall()
    df_abc_2022_4q = pd.DataFrame(query())

with conn:
    with conn.cursor() as curs:
        curs.execute(query_sku_abc_quarter)
        record = curs.fetchall()
    df_sku_quarter = pd.DataFrame(query())

with conn:
    with conn.cursor() as curs:
        curs.execute(query_sku_abc_month)
        record = curs.fetchall()
    df_sku_month = pd.DataFrame(query())

conn.close()
