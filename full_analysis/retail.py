from full_analysis.get_data import *

df_retail_quarter2021['sum'] = df_retail_quarter2021['sum'].astype(int)
df_retail_quarter2021 = df_retail_quarter2021[df_retail_quarter2021['sum'] > 100]
df_retail_quarter2021_group = df_retail_quarter2021.groupby(by=['retailer', 'quarter']).agg(
    sum=('sum', 'sum')).reset_index()

df_retail_quarter2022['sum'] = df_retail_quarter2022['sum'].astype(int)
df_retail_quarter2022 = df_retail_quarter2022[df_retail_quarter2022['sum'] > 100]
df_retail_quarter2022_group = df_retail_quarter2022.groupby(by=['retailer', 'quarter']).agg(
    sum=('sum', 'sum')).reset_index()

df_retail_quarter = pd.concat([df_retail_quarter2021_group, df_retail_quarter2022_group], axis=0).reset_index(drop=True)
df_retail_quarter = df_retail_quarter.groupby(by=['retailer', 'quarter']).agg('sum', 'sum').reset_index()
df_retail_quarter = df_retail_quarter.pivot_table(index='retailer', columns='quarter', values='sum').reset_index()

df_retail_year['sum'] = df_retail_year['sum'].astype(int)
df_retail_year = df_retail_year[df_retail_year['sum'] > 400]
df_retail_year = df_retail_year.pivot_table(index='retailer', columns='year', values='sum').reset_index()
