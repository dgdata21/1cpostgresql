from full_analysis.get_data import *
from operator import attrgetter

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
