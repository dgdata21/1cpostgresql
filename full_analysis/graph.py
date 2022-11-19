import matplotlib.pyplot as plt
import seaborn as sns
from full_analysis.cohorts import *
from full_analysis.revenue import *
from full_analysis.price import *
from full_analysis.client_abc import *
from full_analysis.retail import *
import time
from full_analysis.sku_abc import *

date = time.strftime('%Y-%m-%d %H:%M:%S')


def money_out():
    fig, ax = plt.subplots(figsize=(12, 6))
    df_sum[['sum', 'date']].plot(kind='bar', x='date', color='olive', ax=ax, rot=0, fontsize=11)
    ax.set_xlabel('Month', fontsize=12)
    ax.set_ylabel('Sum', fontsize=12)
    ax.set_title('Period 2021 - 2022', fontsize=12, fontstyle='italic', fontweight='bold')
    ax.grid(True)
    return plt.show()


def revenue():
    fig, ax = plt.subplots(figsize=(12, 9))
    df_revenue.plot(kind='bar', ax=ax, x='agent', fontsize=7, rot=0)
    ax.set_ylabel('Revenue, thousand roubles', fontsize=8)
    ax.grid(True)
    ax.set_title('Revenue by agent in years 2021 - 2022', fontsize=14, fontweight='bold')
    ax.set_xlabel('agent', fontsize=9, fontstyle='italic')
    ax.text(3, 105000, 'limit of revenue per year - 12000',
            fontsize=9, fontweight='bold',
            bbox={'facecolor': 'green', 'alpha': 0.3})
    plt.savefig('/home/dgdata21/PycharmProjects/github/1c_postgresql/diag/revenue' + date + '.pdf')
    return plt.show()


def revenue_quarter():
    fig, ax = plt.subplots(figsize=(12, 9))
    df_revenue_quarter_pivot.plot(kind='bar', ax=ax,
                                  x='agent',
                                  fontsize=7,
                                  rot=0)
    ax.set_ylabel('Revenue, thousand roubles', fontsize=8)
    ax.grid(True)
    ax.set_title('Revenue by agent in quarters 2021 - 2022', fontsize=14, fontweight='bold')
    ax.set_xlabel('agent', fontsize=9, fontstyle='italic')
    ax.text(2, 32000, 'limit of revenue per quarter - 3000',
            fontsize=9, fontweight='bold',
            bbox={'facecolor': 'green', 'alpha': 0.2})
    plt.savefig('/home/dgdata21/PycharmProjects/github/1c_postgresql/diag/revenue_q' + date + '.pdf')
    return plt.show()


def cohort():
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.set(font_scale=0.6)
    sns.heatmap(df_cohort_return,
                annot=True,
                fmt='.0%',
                mask=df_cohort_return.isnull(),
                ax=ax,
                cmap='Greens')
    ax.set_title('2021 - 2022', fontsize=12, fontweight='bold')
    ax.set(xlabel='Period of the "life" of cohorts', ylabel='Cohort')
    plt.savefig('/home/dgdata21/PycharmProjects/github/1c_postgresql/diag/full_analysis' + date + '.pdf')
    return plt.show()


def price():
    fig, ax = plt.subplots(figsize=(12, 9))
    df_pivot_price.plot(kind='bar', ax=ax, x='price_name', fontsize=7, rot=0)
    ax.set_ylabel('Revenue, thousand roubles', fontsize=9)
    ax.grid(True)
    ax.set_xlabel('Type of price', fontsize=9)
    ax.set_title('Revenue by the type of price by quarters', fontsize=14, fontweight='bold')
    ax.text(1.5, 2200000, 'limit of revenue per year - 77000', fontsize=9, fontweight='bold',
            bbox={'facecolor': 'blue', 'alpha': 0.2})
    return plt.show()


def abc_client():
    fig, ax = plt.subplots(figsize=(12, 9))
    df_abc_pivot.plot(kind='bar',
                      ax=ax,
                      x='group',
                      fontsize=7, rot=0)
    ax.grid(axis='y')
    ax.set_xlabel('Group')
    ax.set_title('Revenue by groups in period', fontsize=14, fontweight='bold', fontfamily='serif')
    ax.legend(loc='upper right', ncol=4)
    ax.set_yscale(value='log')
    return plt.show()


def retail_quarter():
    fig, ax = plt.subplots(figsize=(12, 9))
    df_retail_quarter.plot(kind='bar', ax=ax, x='retailer', fontsize=7, rot=0)
    ax.grid(True)
    ax.set_ylabel('Revenue, thousand roubles')
    ax.set_xlabel('Retailer')
    ax.set_title('Revenue by retailer in quarters', fontsize=14, fontweight='bold')
    ax.legend(loc='best', ncol=4)
    plt.savefig('/home/dgdata21/PycharmProjects/github/1c_postgresql/diag/retail_q' + date + '.pdf')
    return plt.show()


def retail_year():
    fig, ax = plt.subplots(figsize=(12, 9))
    df_retail_year.plot(kind='bar', ax=ax, x='retailer', fontsize=7, rot=0)
    ax.grid(True)
    ax.set_ylabel('Revenue, thousand roubles')
    ax.set_xlabel('Retailer')
    ax.set_title('Revenue by retailer in years', fontsize=14, fontweight='bold')
    ax.legend(loc='best', ncol=4)
    plt.savefig('/home/dgdata21/PycharmProjects/github/1c_postgresql/diag/retail' + date + '.pdf')
    return plt.show()

def abc_sku_quarter():
    fig, ax = plt.subplots(figsize=(12, 8))
    df_sku_quarter_pivot.plot(kind='bar', rot=0, ax=ax)
    ax.set_title('Revenue of sku by groups', fontsize=16, fontweight='bold', fontstyle='italic', fontfamily='sans')
    ax.set_xlabel('group', fontfamily='serif', fontweight='bold')
    ax.set_ylabel('Revenue, ths. r.', fontfamily='serif', fontweight='bold')
    # ax.minorticks_on()
    ax.grid(axis='y', which='major')
    ax.grid(axis='y', which='minor')
    plt.show()
