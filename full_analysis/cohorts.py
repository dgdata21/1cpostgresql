import pandas as pd

from full_analysis.get_data import *
from operator import attrgetter

# cohorts 2022
df_cohort2022['full_analysis'] = df_cohort2022.groupby('client')['date'].transform('min').dt.to_period('M')
df_cohort2022['date'] = df_cohort2022['date'].dt.to_period('M')
df_cohort2022['period'] = (df_cohort2022['date'] - df_cohort2022['full_analysis']).apply(attrgetter('n'))
df_cohort2022 = df_cohort2022.groupby(['full_analysis', 'date', 'period']).agg(clients=('client', 'nunique')).reset_index()
df_cohort2022 = df_cohort2022.pivot_table(index='full_analysis',
                                          columns='period',
                                          values='clients')
df_cohort_return2022 = df_cohort2022.divide(df_cohort2022.iloc[:, 0], axis=0)

# cohorts 2021
df_cohort2021['full_analysis'] = df_cohort2021.groupby('client')['date'].transform('min').dt.to_period('M')
df_cohort2021['date'] = df_cohort2021['date'].dt.to_period('M')
df_cohort2021['period'] = (df_cohort2021['date'] - df_cohort2021['full_analysis']).apply(attrgetter('n'))
df_cohort2021 = df_cohort2021.groupby(['full_analysis', 'date', 'period']).agg(clients=('client', 'nunique')).reset_index()
df_cohort2021 = df_cohort2021.pivot_table(index='full_analysis',
                                          columns='period',
                                          values='clients')
df_cohort_return2021 = df_cohort2021.divide(df_cohort2021.iloc[:, 0], axis=0)

df_cohort['reg_date'] = pd.to_datetime(df_cohort['reg_date'])
df_cohort['doc_date'] = pd.to_datetime(df_cohort['doc_date'])
df_cohort['sum'] = df_cohort['sum'].astype(int)
df_cohort['full_analysis'] = df_cohort.groupby('id')['reg_date'].transform('min').dt.to_period('M')
df_cohort['reg_date'] = df_cohort['reg_date'].dt.to_period('M')
df_cohort['doc_date'] = df_cohort['doc_date'].dt.to_period('M')
df_cohort['period'] = (df_cohort['doc_date'] - df_cohort['full_analysis']).apply(attrgetter('n'))
df_cohort_new = df_cohort.groupby(['full_analysis', 'doc_date', 'period']).agg(clients=('id', 'nunique')).reset_index()
df_cohort_return = df_cohort_new.pivot_table(index='full_analysis',
                                             columns='period',
                                             values='clients')
df_cohort_return = df_cohort_return.divide(df_cohort_return.iloc[:, 0], axis=0)
