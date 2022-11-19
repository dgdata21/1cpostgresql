# # getting codes and names of organizations
# query_org = '''
# select encode(1c_postgresql.public._reference195._idrref, 'hex') as id,
#        _fld21353                                        as name
# from 1c_postgresql.public._reference195
# '''

# getting id and names of partners
query_clients = '''
select encode(1c_postgresql.public._reference212._idrref, 'hex') as id,
       _description                                     as name
from 1c_postgresql.public._reference212
'''

# getting id and names of projects
query_project = '''
select encode(1c_postgresql.public._reference225._idrref, 'hex') as id,
       _description                                     as name
from 1c_postgresql.public._reference225
'''

# getting cohorts
query_cohort2022 = '''
select distinct(encode(1c_postgresql.public._document497._fld7908rref, 'hex')) as client,
               _date_time                                             as date
from 1c_postgresql.public._document497
where _posted = 'true' and _date_time >= '2022-01-01'
'''

query_cohort2021 = '''
select distinct(encode(1c_postgresql.public._document497._fld7908rref, 'hex')) as client,
               _date_time                                             as date
from 1c_postgresql.public._document497
where _posted = 'true' and _date_time < '2022-01-01' and _date_time >= '2021-01-01'
'''

# getting revenue by agents
query_agent2022 = '''
with rtu as
         (select encode(1c_postgresql.public._document497._idrref, 'hex')      as doc_id,
                 _number                                              as number,
                 date(_date_time)                                     as date,
                 encode(1c_postgresql.public._document497._fld7904rref, 'hex') as client,
                 _fld7907                                             as sum,
                 encode(1c_postgresql.public._document497._fld7905rref, 'hex') as agent
          from 1c_postgresql.public._document497
          where _posted = 'true'
          order by 3 desc),
     agent as
         (select encode(1c_postgresql.public._reference225._idrref, 'hex') as agent_id,
                 _description                                     as agent_name
          from 1c_postgresql.public._reference225),
     revenue as
         (select date_trunc('quarter', rtu.date)::date  as date,
                 agent.agent_name                       as agent,
                 round(sum(rtu.sum)::decimal / 1000, 0) as sum
          from rtu
                   join agent on agent.agent_id = rtu.agent
          where rtu.date between '2022-01-01' and '2022-12-31'
          group by 1, 2
          order by 1)
select revenue.date,
       revenue.agent,
       revenue.sum,
       case
           when revenue.date = '2022-01-01' then 'q1_2022'
           when revenue.date = '2022-04-01' then 'q2_2022'
           when revenue.date = '2022-07-01' then 'q3_2022'
           when revenue.date = '2022-10-01' then 'q4_2022'
           end as quarter
from revenue
'''

query_agent2021 = '''
with rtu as
         (select encode(1c_postgresql.public._document497._idrref, 'hex')      as doc_id,
                 _number                                              as number,
                 date(_date_time)                                     as date,
                 encode(1c_postgresql.public._document497._fld7904rref, 'hex') as client,
                 _fld7907                                             as sum,
                 encode(1c_postgresql.public._document497._fld7905rref, 'hex') as agent
          from 1c_postgresql.public._document497
          where _posted = 'true'
          order by 3 desc),
     agent as
         (select encode(1c_postgresql.public._reference225._idrref, 'hex') as agent_id,
                 _description                                     as agent_name
          from 1c_postgresql.public._reference225),
     revenue as
         (select date_trunc('quarter', rtu.date)::date  as date,
                 agent.agent_name                       as agent,
                 round(sum(rtu.sum)::decimal / 1000, 0) as sum
          from rtu
                   join agent on agent.agent_id = rtu.agent
          where rtu.date between '2021-01-01' and '2021-12-31'
          group by 1, 2
          order by 1)
select revenue.date,
       revenue.agent,
       revenue.sum,
       case
           when revenue.date = '2021-01-01' then 'q1_2021'
           when revenue.date = '2021-04-01' then 'q2_2021'
           when revenue.date = '2021-07-01' then 'q3_2021'
           when revenue.date = '2021-10-01' then 'q4_2021'
           end as quarter
from revenue
'''

# getting sums toward partners
query_sum = '''
with rko as
         (select _date_time                                           as date,
                 encode(1c_postgresql.public._document492._fld7754rref, 'hex') as id,
                 _fld7717                                             as sum
          from 1c_postgresql.public._document492
          where _posted = 'true'),
     partner as
         (select encode(1c_postgresql.public._reference165._idrref, 'hex') as client_id,
                 _description                                     as client_name
          from 1c_postgresql.public._reference165)
select date_trunc('month', rko.date) as date,
       partner.client_name,
       sum(rko.sum)                  as sum
from rko
         join partner on partner.client_id = rko.id
where partner.client_name = 'У_К'
group by 1, 2
order by 1
'''

# getting cohorts
query_all = '''
with rtu as
         (select encode(1c_postgresql.public._document497._idrref, 'hex')      as doc_id,
                 _number                                              as number,
                 date(_date_time)                                     as date,
                 encode(1c_postgresql.public._document497._fld7908rref, 'hex') as client,
                 _fld7907                                             as sum,
                 encode(1c_postgresql.public._document497._fld7905rref, 'hex') as agent
          from 1c_postgresql.public._document497
          where _posted = 'true'),
     client as
         (select encode(1c_postgresql.public._reference212._idrref, 'hex') as client_id,
                 date(_fld21814)                                  as reg_date,
                 _description                                     as client_name
          from 1c_postgresql.public._reference212)
select client.reg_date    as reg_date,
       rtu.date           as doc_date,
       client.client_id   as id,
       client.client_name as client_name,
       round(rtu.sum, 0)  as sum
from rtu
         join client
              on client.client_id = rtu.client
where client.reg_date >= '2021-04-01'
  and rtu.date >= '2021-04-01'
  and client.client_name != 'КАРАВАН 24 ул.Калинина, 93'
  and client.client_name != 'КАРАВАН 24 ул.К.Цеткин, 55'
  and client.client_name != 'Рамзаев Станислав Владимирович ул.Белинского, 2а "Деловая колбаса"'
'''

# getting docs by price
queryprices2022 = '''
with rtu as
         (select encode(1c_postgresql.public._document497._idrref, 'hex')             as doc_id,
                 _number                                                     as number,
                 date(_date_time)                                            as date,
                 encode(1c_postgresql.public._document497._fld7904rref, 'hex')        as client,
                 _fld7907                                                    as sum,
                 encode(1c_postgresql.public._document497._fld7905rref, 'hex')        as agent,
                 encode(1c_postgresql.public._document497_vt7964._fld7972rref, 'hex') as price_type
          from 1c_postgresql.public._document497
               join 1c_postgresql.public._document497_vt7964 on
                   encode(1c_postgresql.public._document497_vt7964._document497_idrref, 'hex') =
                   encode(1c_postgresql.public._document497._idrref, 'hex')
          where _posted = 'true'
          order by 3 desc),
     price as
         (select encode(1c_postgresql.public._reference75._idrref, 'hex') as price_id,
                 _description                                    as price_name
          from 1c_postgresql.public._reference75)
select date_trunc('quarter', rtu.date)::date    as date,
       price.price_name,
       round(sum(rtu.sum)::decimal / 1000, 0) as sum
from rtu
         join price on price.price_id = rtu.price_type
where rtu.date between '2022-01-01' and '2022-12-31'
group by 1, 2
order by 1 desc
'''

queryprices2021 = '''
with rtu as
         (select encode(1c_postgresql.public._document497._idrref, 'hex')      as doc_id,
                 _number                                              as number,
                 date(_date_time)                                     as date,
                 encode(1c_postgresql.public._document497._fld7904rref, 'hex') as client,
                 _fld7907                                             as sum,
                 encode(1c_postgresql.public._document497._fld7905rref, 'hex') as agent,
                 encode(1c_postgresql.public._document497_vt7964._fld7972rref, 'hex') as price_type
          from 1c_postgresql.public._document497
               join 1c_postgresql.public._document497_vt7964 on
                   encode(1c_postgresql.public._document497_vt7964._document497_idrref, 'hex') =
                   encode(1c_postgresql.public._document497._idrref, 'hex')
          where _posted = 'true'
          order by 3 desc),
     price as
         (select encode(1c_postgresql.public._reference75._idrref, 'hex') as price_id,
                 _description                                    as price_name
          from 1c_postgresql.public._reference75)
select date_trunc('quarter', rtu.date)::date    as date,
       price.price_name,
       round(sum(rtu.sum)::decimal / 1000, 0) as sum
from rtu
         join price on price.price_id = rtu.price_type
where rtu.date between '2021-01-01' and '2022-12-31'
group by 1, 2
order by 1 desc
'''

query_retail_quarter2021 = '''
with orp as
         (select encode(1c_postgresql.public._document459._idrref, 'hex')      as doc_id,
                 encode(1c_postgresql.public._document459._fld5805rref, 'hex') as retailer_id,
                 _fld5808                                             as sum,
                 _date_time                                           as date
          from 1c_postgresql.public._document459
          where _posted = 'true'),
     retailer as
         (select encode(1c_postgresql.public._reference225._idrref, 'hex') as retailer_id,
                 _description                                     as retailer
          from 1c_postgresql.public._reference225),
     revenue as
         (select date_trunc('quarter', orp.date)::date  as date,
                 retailer.retailer                      as retailer,
                 round(sum(orp.sum)::decimal / 1000, 0) as sum
          from orp
                  join retailer on retailer.retailer_id = orp.retailer_id
          where orp.date between '2021-01-01' and '2021-12-31'
          group by 1, 2
          order by 1 desc)
select revenue.date,
       revenue.retailer,
       revenue.sum,
       case
           when revenue.date = '2021-01-01' then 'q1_2021'
           when revenue.date = '2021-04-01' then 'q2_2021'
           when revenue.date = '2021-07-01' then 'q3_2021'
           when revenue.date = '2021-10-01' then 'q4_2021'
           end as quarter
from revenue
'''

query_retail_quarter2022 = '''
with orp as
         (select encode(1c_postgresql.public._document459._idrref, 'hex')      as doc_id,
                 encode(1c_postgresql.public._document459._fld5805rref, 'hex') as retailer_id,
                 _fld5808                                             as sum,
                 _date_time                                           as date
          from 1c_postgresql.public._document459
          where _posted = 'true'),
     retailer as
         (select encode(1c_postgresql.public._reference225._idrref, 'hex') as retailer_id,
                 _description                                     as retailer
          from 1c_postgresql.public._reference225),
     revenue as
         (select date_trunc('quarter', orp.date)::date  as date,
                 retailer.retailer                      as retailer,
                 round(sum(orp.sum)::decimal / 1000, 0) as sum
          from orp
                  join retailer on retailer.retailer_id = orp.retailer_id
          where orp.date between '2022-01-01' and '2022-12-31'
          group by 1, 2
          order by 1 desc)
select revenue.date,
       revenue.retailer,
       revenue.sum,
       case
           when revenue.date = '2022-01-01' then 'q1_2022'
           when revenue.date = '2022-04-01' then 'q2_2022'
           when revenue.date = '2022-07-01' then 'q3_2022'
           when revenue.date = '2022-10-01' then 'q4_2022'
           end as quarter
from revenue
'''

query_retail_year = '''
with orp as
         (select encode(1c_postgresql.public._document459._idrref, 'hex')      as doc_id,
                 encode(1c_postgresql.public._document459._fld5805rref, 'hex') as agent_id,
                 _fld5808                                             as sum,
                 _date_time                                           as date
          from 1c_postgresql.public._document459
          where _posted = 'true'),
     agent as
         (select encode(1c_postgresql.public._reference225._idrref, 'hex') as agent_id,
                 _description                                     as agent_name
          from 1c_postgresql.public._reference225),
     revenue as
         (select date_trunc('year', orp.date)::date     as date,
                 agent.agent_name                       as retailer,
                 round(sum(orp.sum)::decimal / 1000, 0) as sum
          from orp
                   join agent on agent.agent_id = orp.agent_id
          group by 1, 2
          order by 1 desc)
select
    revenue.date,
    revenue.retailer,
    revenue.sum,
       case
           when revenue.date = '2021-01-01' then '2021'
           when revenue.date = '2022-01-01' then '2022'
           end as year
from revenue
'''

