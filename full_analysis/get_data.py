import psycopg2 as ps2
from psycopg2 import extras
import pandas as pd
from full_analysis.queries import *
import time

date = time.strftime('%Y-%m-%d %H:%M:%S')   # variable for saving files with current date and time

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
        curs.execute(query_agent2021)
        record = curs.fetchall()
    df_revenue2021 = pd.DataFrame(query())

    # If you need to save the result of query you do have to put in following line
    # if you don't - If you don't need - delete it
    # df_revenue2021.to_csv('~/data/agent2021'+date+'.csv')  # directory path you need

with conn:
    with conn.cursor() as curs:
        curs.execute(query_agent2022)
        record = curs.fetchall()
    df_revenue2022 = pd.DataFrame(query())

    # If you need to save the result of query you do have to put in following line
    # if you don't - If you don't need - delete it
    # df_revenue2022.to_csv('~/data/agent2022'+date+'.csv')  # directory path you need

# cohorts
with conn:
    with conn.cursor() as curs:
        curs.execute(query_all)
        record = curs.fetchall()
    df_cohort = pd.DataFrame(query())

    # If you need to save the result of query you do have to put in following line
    # if you don't - If you don't need - delete it
    # df_cohort.to_csv('~/data/cohort'+date+'.csv')  # directory path you need


conn.close()    # don't forget to close connection!!!
