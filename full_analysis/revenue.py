from full_analysis.get_data import *
import time

date = time.strftime('%Y-%m-%d %H:%M:%S')

df_revenue_annual2021 = df_revenue2021.groupby(['agent']).agg(sum=('sum', 'sum')).reset_index()
df_revenue_annual2021 = df_revenue_annual2021.rename(columns={'sum': 'sum2021'})

df_revenue_annual2022 = df_revenue2022.groupby(['agent']).agg(sum=('sum', 'sum')).reset_index()
df_revenue_annual2022 = df_revenue_annual2022.rename(columns={'sum': 'sum2022'})

df_revenue = df_revenue_annual2021.merge(df_revenue_annual2022, on='agent', how='outer')

df_revenue = df_revenue.fillna(0)
df_revenue['sum2021'] = df_revenue['sum2021'].astype(int)
df_revenue['sum2022'] = df_revenue['sum2022'].astype(int)
df_revenue.to_csv('/home/dgdata21/PycharmProjects/github/1c_postgresql/csv/revenue' + date + '.csv')
df_revenue = df_revenue[(df_revenue['sum2021'] & df_revenue['sum2022']) > 12000].reset_index(drop=True)

df_revenue_quarter2021 = df_revenue2021.groupby(['agent', 'quarter']).agg(sum=('sum', 'sum')).reset_index()
df_revenue_quarter2022 = df_revenue2022.groupby(['agent', 'quarter']).agg(sum=('sum', 'sum')).reset_index()
df_revenue_quarter2022.to_csv('/home/dgdata21/PycharmProjects/github/1c_postgresql/csv/revenue_q' + date + '.csv')
df_revenue_quarter = pd.concat([df_revenue_quarter2021, df_revenue_quarter2022], axis=0)
df_revenue_quarter_all = df_revenue_quarter[df_revenue_quarter['sum'] > 3000]

df_revenue_quarter_pivot = df_revenue_quarter_all.pivot_table(index='agent',
                                                              columns='quarter',
                                                              values='sum').reset_index()
df_revenue_quarter_pivot = df_revenue_quarter_pivot.fillna(0)

df_sum['sum'] = df_sum['sum'].astype(int)
df_sum['sum'] = df_sum['sum'] / 1000
df_sum['date'] = df_sum['date'].dt.month
df_sum.to_csv('/home/dgdata21/PycharmProjects/github/1c_postgresql/csv/money' + date + '.csv')
