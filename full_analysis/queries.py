# getting revenue by agents 2022
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

# getting revenue by agents 2021
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


