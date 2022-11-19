import matplotlib.pyplot as plt
import seaborn as sns
from full_analysis.cohorts import *
from full_analysis.revenue import *
from full_analysis.client_abc import *
from full_analysis.sku_abc import *
import time

date = time.strftime('%Y-%m-%d %H:%M:%S')


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

    # plt.savefig('~/diag/revenue' + date + '.pdf')   # If you need to save the result of plotting
                                                      # you do have to put in following line
                                                      # if you don't - If you don't need - delete it

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

    # plt.savefig('~/diag/revenue_q' + date + '.pdf')   # If you need to save the result of plotting
                                                        # you do have to put in following line
                                                        # if you don't - If you don't need - delete it

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

    # plt.savefig('~/diag/full_analysis' + date + '.pdf')   # If you need to save the result of plotting
                                                            # you do have to put in following line
                                                            # if you don't - If you don't need - delete it

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


def abc_sku_quarter():
    fig, ax = plt.subplots(figsize=(12, 8))
    df_sku_quarter_pivot.plot(kind='bar', rot=0, ax=ax)
    ax.set_title('Revenue of sku by groups', fontsize=16, fontweight='bold', fontstyle='italic', fontfamily='sans')
    ax.set_xlabel('group', fontfamily='serif', fontweight='bold')
    ax.set_ylabel('Revenue, ths. r.', fontfamily='serif', fontweight='bold')
    ax.grid(axis='y')
    plt.show()
