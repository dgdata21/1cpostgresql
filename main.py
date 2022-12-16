if __name__ == '__main__':
    print('\nGetting and analysing data')
    import full_analysis
    graph_agent_quarter = full_analysis.revenue_quarter()
    graph_revenue = full_analysis.revenue()
    graph_cohort = full_analysis.cohort()
    graph_abc_sku = full_analysis.abc_sku_quarter()
