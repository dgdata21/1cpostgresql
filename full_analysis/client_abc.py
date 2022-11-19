from full_analysis.get_data_abc import *

df_abc = pd.concat([df_abc_2021_1q, df_abc_2021_2q, df_abc_2021_3q, df_abc_2021_4q,
                    df_abc_2022_1q, df_abc_2022_2q, df_abc_2022_3q, df_abc_2022_4q], axis=0)
df_abc['sum'] = df_abc['sum'].astype(int)

df_abc_group = df_abc.groupby(['group', 'quarter']).agg(sum=('sum', 'sum')).reset_index()
df_abc_pivot = df_abc.pivot_table(index='group', columns='quarter', values='sum').reset_index()




