import psycopg2 as ps2
from psycopg2 import extras
import pandas as pd
from full_analysis.queries import *
from full_analysis.queries_abc import *
import time

date = time.strftime('%Y-%m-%d %H:%M:%S')

# # getting codes and names of organizations
# query_org = '''
# select encode(1c_postgresql.public._reference195._idrref, 'hex') as id,
#        _fld21353                                        as name
# from 1c_postgresql.public._reference195
# '''
#
# # getting id and names of partners
# query_clients = '''
# select encode(1c_postgresql.public._reference212._idrref, 'hex') as id,
#        _description                                     as name
# from 1c_postgresql.public._reference212
# '''
#
# # getting id and names of projects
# query_project = '''
# select encode(1c_postgresql.public._reference225._idrref, 'hex') as id,
#        _description                                     as name
# from 1c_postgresql.public._reference225
# '''
#
# # getting cohorts
# query_cohort = '''
# select distinct(encode(1c_postgresql.public._document401._fld3124rref, 'hex')) as client,
#                _date_time::date                                       as date
# from 1c_postgresql.public._document401
# where _posted = 'true' and _date_time < '2022-11-01' and _date_time > '2021-12-31'
# '''


conn = ps2.connect(dbname='1c_postgresql',
                   host='109.236.90.133',
                   user='postgres',
                   password='Eghfdktybt<fpfvb',
                   cursor_factory=ps2.extras.DictCursor)


def query():
    data = []
    for i in record:
        data.append(dict(i))
    return data


with conn:
    with conn.cursor() as curs:
        curs.execute(query_org)
        record = curs.fetchall()
    # df_org = pd.DataFrame(data)

with conn:
    with conn.cursor() as curs:
        curs.execute(query_clients)
        record = curs.fetchall()
    # df_client = pd.DataFrame(data)

with conn:
    with conn.cursor() as curs:
        curs.execute(query_project)
        record = curs.fetchall()
    # df_project = pd.DataFrame(data)

with conn:
    with conn.cursor() as curs:
        curs.execute(query_cohort2022)
        record = curs.fetchall()
    df_cohort2022 = pd.DataFrame(query())

with conn:
    with conn.cursor() as curs:
        curs.execute(query_cohort2021)
        record = curs.fetchall()
    df_cohort2021 = pd.DataFrame(query())

with conn:
    with conn.cursor() as curs:
        curs.execute(query_agent2021)
        record = curs.fetchall()
    df_revenue2021 = pd.DataFrame(query())
    df_revenue2021.to_csv('/home/dgdata21/PycharmProjects/github/1c_postgresql/data/agent2021'+date+'.csv')

with conn:
    with conn.cursor() as curs:
        curs.execute(query_agent2022)
        record = curs.fetchall()
    df_revenue2022 = pd.DataFrame(query())
    df_revenue2022.to_csv('/home/dgdata21/PycharmProjects/github/1c_postgresql/data/agent2022'+date+'.csv')

with conn:
    with conn.cursor() as curs:
        curs.execute(query_sum)
        record = curs.fetchall()
    df_sum = pd.DataFrame(query())
    df_sum.to_csv('/home/dgdata21/PycharmProjects/github/1c_postgresql/data/sum'+date+'.csv')

# cohorts
with conn:
    with conn.cursor() as curs:
        curs.execute(query_all)
        record = curs.fetchall()
    df_cohort = pd.DataFrame(query())
    df_cohort.to_csv('/home/dgdata21/PycharmProjects/github/1c_postgresql/data/cohort'+date+'.csv')

with conn:
    with conn.cursor() as curs:
        curs.execute(queryprices2022)
        record = curs.fetchall()
    df_price2022 = pd.DataFrame(query())

with conn:
    with conn.cursor() as curs:
        curs.execute(queryprices2021)
        record = curs.fetchall()
    df_price2021 = pd.DataFrame(query())

# retail 2021 quarter
with conn:
    with conn.cursor() as curs:
        curs.execute(query_retail_quarter2021)
        record = curs.fetchall()
        data = []
        for i in record:
            data.append(dict(i))
    df_retail_quarter2021 = pd.DataFrame(data)

# retail 2022 quarter
with conn:
    with conn.cursor() as curs:
        curs.execute(query_retail_quarter2022)
        record = curs.fetchall()
    df_retail_quarter2022 = pd.DataFrame(query())

# retail year
with conn:
    with conn.cursor() as curs:
        curs.execute(query_retail_year)
        record = curs.fetchall()
    df_retail_year = pd.DataFrame(query())
    df_retail_year.to_csv('/home/dgdata21/PycharmProjects/github/1c_postgresql/data/retail'+date+'.csv')

conn.close()
