from full_analysis.get_data_abc import *

df_sku_month['period'] = pd.to_datetime(df_sku_month['period'])
df_sku_month = df_sku_month.drop(columns=['total'])
df_sku_month['share_percent'] = df_sku_month['share_percent'].astype(float)
df_sku_month['cumulative'] = df_sku_month.groupby('period')['share_percent'].cumsum()
df_sku_month['group_abc'] = ''
df_sku_month.loc[df_sku_month['cumulative'] <= 20, 'group_abc'] = 'group_a'
df_sku_month.loc[df_sku_month['cumulative'].between(20.01, 30), 'group_abc'] = 'group_b'
df_sku_month.loc[df_sku_month['cumulative'] > 30, 'group_abc'] = 'group_c'
df_sku_month['rn'] = df_sku_month.groupby(['period', 'group_abc']).cumcount()
df_sku_month = df_sku_month.drop(columns=['share_percent', 'cumulative'])

df_sku_month['month'] = ''

df_sku_quarter['period'] = pd.to_datetime(df_sku_quarter['period'])
df_sku_quarter = df_sku_quarter.drop(columns='total')
df_sku_quarter['share_percent'] = df_sku_quarter['share_percent'].astype(float)
df_sku_quarter['cumulative'] = df_sku_quarter.groupby('period')['share_percent'].cumsum()
df_sku_quarter['group_abc'] = ''
df_sku_quarter.loc[df_sku_quarter['cumulative'] <= 20, 'group_abc'] = 'group_a'
df_sku_quarter.loc[df_sku_quarter['cumulative'].between(20.01, 30), 'group_abc'] = 'group_b'
df_sku_quarter.loc[df_sku_quarter['cumulative'] > 30, 'group_abc'] = 'group_c'
df_sku_quarter['rn'] = df_sku_quarter.groupby(['period', 'group_abc']).cumcount()
df_sku_quarter = df_sku_quarter.drop(columns=['share_percent', 'cumulative'])

df_sku_quarter['quarter'] = ''
df_sku_quarter.loc[df_sku_quarter['period'] == '2022-01-01', 'quarter'] = 'q1_2022'
df_sku_quarter.loc[df_sku_quarter['period'] == '2022-04-01', 'quarter'] = 'q2_2022'
df_sku_quarter.loc[df_sku_quarter['period'] == '2022-07-01', 'quarter'] = 'q3_2022'
df_sku_quarter.loc[df_sku_quarter['period'] == '2022-10-01', 'quarter'] = 'q4_2022'

df_sku_quarter.loc[df_sku_quarter['period'] == '2021-01-01', 'quarter'] = 'q1_2021'
df_sku_quarter.loc[df_sku_quarter['period'] == '2021-04-01', 'quarter'] = 'q2_2021'
df_sku_quarter.loc[df_sku_quarter['period'] == '2021-07-01', 'quarter'] = 'q3_2021'
df_sku_quarter.loc[df_sku_quarter['period'] == '2021-10-01', 'quarter'] = 'q4_2021'

df_sku_quarter_pivot = df_sku_quarter.pivot_table(index='group_abc', columns='quarter', values='sum')
