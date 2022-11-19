Hi, folks. My name's Dmitriy.\
Here I'm gonna share my experience in getting and analyzing data from russian application system 1C Enterprise:Trade Management v.11.4
This research is just example and not full observing the structure of the postgresql base of configuration Trade Management v.11.4, so I'll take only few tables.

Problems to be solved:
- Analyze revenue of each manager in quarters of the certain period
- Analyze revenue of each manager in years of the certain period
- ABC-analysis of sku in quarters of the certain period

The tables to use:
- table of sales orders
- table of managers
- table of sku
