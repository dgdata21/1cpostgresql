if __name__ == '__main__':
    print('\nGetting and analysing data')
    import full_analysis
    graph_agent_quarter = full_analysis.revenue_quarter()
    graph_revenue = full_analysis.revenue()
    graph_retail_quarter = full_analysis.retail_quarter()
    graph_retail_year = full_analysis.retail_year()
    graph_cohort = full_analysis.cohort()
    graph_price = full_analysis.price()
    graph_abc_client = full_analysis.abc_client()
    graph_abc_sku = full_analysis.abc_sku_quarter()
    graph_sum = full_analysis.money_out()
