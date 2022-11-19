import psycopg2 as ps2
from psycopg2 import extras
import pandas as pd
from full_analysis.queries import *
from full_analysis.queries_abc import *
import time

date = time.strftime('%Y-%m-%d %H:%M:%S')

conn = ps2.connect(dbname='1c_postgresql',
                   host='1xx.2xx.9x.1xx',
                   user='user',
                   password='password',
                   cursor_factory=ps2.extras.DictCursor)


def query():
    data = []
    for i in record:
        data.append(dict(i))
    return data


with conn:
    with conn.cursor() as curs:
        curs.execute(query_agent2021)
        record = curs.fetchall()
    df_revenue2021 = pd.DataFrame(query())
    df_revenue2021.to_csv('/home/root/PycharmProjects/github/1c_postgresql/data/agent2021'+date+'.csv')

with conn:
    with conn.cursor() as curs:
        curs.execute(query_agent2022)
        record = curs.fetchall()
    df_revenue2022 = pd.DataFrame(query())
    df_revenue2022.to_csv('/home/root/PycharmProjects/github/1c_postgresql/data/agent2022'+date+'.csv')

# cohorts
with conn:
    with conn.cursor() as curs:
        curs.execute(query_all)
        record = curs.fetchall()
    df_cohort = pd.DataFrame(query())
    df_cohort.to_csv('/home/root/PycharmProjects/github/1c_postgresql/data/cohort'+date+'.csv')


conn.close()
