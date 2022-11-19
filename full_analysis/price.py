from full_analysis.get_data import *

df_price2022['sum'] = df_price2022['sum'].astype(int)
df_price2022 = df_price2022.rename(columns={'sum': '2022'})
df_price2022 = df_price2022[df_price2022['2022'] > 77000]

df_price2021['sum'] = df_price2021['sum'].astype(int)
df_price2021 = df_price2021.rename(columns={'sum': '2021'})
df_price2021 = df_price2021[df_price2021['2021'] > 77000]

df_price2021_group = df_price2021.groupby(by=['price_name', 'date']).agg(sum21=('2021', 'sum')).reset_index()
df_price2022_group = df_price2022.groupby(by=['price_name', 'date']).agg(sum22=('2022', 'sum')).reset_index()

df_price = df_price2021_group.merge(df_price2022_group, how='outer', on=('price_name', 'date'))
df_pivot_price21 = df_price.pivot_table(index='price_name', columns='date', values='sum21')
df_pivot_price22 = df_price.pivot_table(index='price_name', columns='date', values='sum22')
df_pivot_price = pd.concat([df_pivot_price21, df_pivot_price22], axis=1).reset_index()

