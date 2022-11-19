query_abc_2021_1q = '''
with rtu as
         (select date(_date_time)                                     as date,
                 encode(1c_postgresql.public._document497._fld7908rref, 'hex') as client_id,
                 _fld7907                                             as sum
          from 1c_postgresql.public._document497
          where _posted = 'true'),
     client as
         (select encode(1c_postgresql.public._reference212._idrref, 'hex') as client_id,
                 _description                                     as client_name
          from 1c_postgresql.public._reference212),
     revenue as
         (select client.client_name,
                 round(sum(rtu.sum)::decimal / 1000, 0) as sum
          from rtu
                   join client on client.client_id = rtu.client_id
          where rtu.date between '2021-01-01' and '2021-03-31'
          group by 1
          order by 2 desc),
     all_sum as
         (select sum(revenue.sum) as all_sum
          from revenue),
     share as
         (select row_number() over ()                  as rn,
                 revenue.client_name,
                 revenue.sum,
                 all_sum,
                 round(revenue.sum / all_sum * 100, 2) as share
          from all_sum,
               revenue)
select
       share.client_name,
       share.sum,
       share.all_sum,
       share.share,
       sum(share.share) over (order by share.rn range unbounded preceding) as cumm_percent,
       case
           when sum(share.share) over (order by share.rn range unbounded preceding) between 0 and 20 then 'group_a'
           when sum(share.share) over (order by share.rn range unbounded preceding) between 20.01 and 80 then 'group_b'
           when sum(share.share) over (order by share.rn range unbounded preceding) between 80.01 and 100 then 'group_c'
           else 'other'
           end                                                             as group,       
       case
           when share.client_name is not null then '1q_2021'
           end                                                             as quarter

from share
'''

query_abc_2021_2q = '''
with rtu as
         (select date(_date_time)                                     as date,
                 encode(1c_postgresql.public._document497._fld7908rref, 'hex') as client_id,
                 _fld7907                                             as sum
          from 1c_postgresql.public._document497
          where _posted = 'true'),
     client as
         (select encode(1c_postgresql.public._reference212._idrref, 'hex') as client_id,
                 _description                                     as client_name
          from 1c_postgresql.public._reference212),
     revenue as
         (select client.client_name,
                 round(sum(rtu.sum)::decimal / 1000, 0) as sum
          from rtu
                   join client on client.client_id = rtu.client_id
          where rtu.date between '2021-04-01' and '2021-06-30'
          group by 1
          order by 2 desc),
     all_sum as
         (select sum(revenue.sum) as all_sum
          from revenue),
     share as
         (select row_number() over ()                  as rn,
                 revenue.client_name,
                 revenue.sum,
                 all_sum,
                 round(revenue.sum / all_sum * 100, 2) as share
          from all_sum,
               revenue)
select
       share.client_name,
       share.sum,
       share.all_sum,
       share.share,
       sum(share.share) over (order by share.rn range unbounded preceding) as cumm_percent,
       case
           when sum(share.share) over (order by share.rn range unbounded preceding) between 0 and 20 then 'group_a'
           when sum(share.share) over (order by share.rn range unbounded preceding) between 20.01 and 80 then 'group_b'
           when sum(share.share) over (order by share.rn range unbounded preceding) between 80.01 and 100 then 'group_c'
           else 'other'
           end                                                             as group,
       case
           when share.client_name is not null then '2q_2021'
           end                                                             as quarter
from share
'''

query_abc_2021_3q = '''
with rtu as
         (select date(_date_time)                                     as date,
                 encode(1c_postgresql.public._document497._fld7908rref, 'hex') as client_id,
                 _fld7907                                             as sum
          from 1c_postgresql.public._document497
          where _posted = 'true'),
     client as
         (select encode(1c_postgresql.public._reference212._idrref, 'hex') as client_id,
                 _description                                     as client_name
          from 1c_postgresql.public._reference212),
     revenue as
         (select client.client_name,
                 round(sum(rtu.sum)::decimal / 1000, 0) as sum
          from rtu
                   join client on client.client_id = rtu.client_id
          where rtu.date between '2021-07-01' and '2021-09-30'
          group by 1
          order by 2 desc),
     all_sum as
         (select sum(revenue.sum) as all_sum
          from revenue),
     share as
         (select row_number() over ()                  as rn,
                 revenue.client_name,
                 revenue.sum,
                 all_sum,
                 round(revenue.sum / all_sum * 100, 2) as share
          from all_sum,
               revenue)
select
       share.client_name,
       share.sum,
       share.all_sum,
       share.share,
       sum(share.share) over (order by share.rn range unbounded preceding) as cumm_percent,
       case
           when sum(share.share) over (order by share.rn range unbounded preceding) between 0 and 20 then 'group_a'
           when sum(share.share) over (order by share.rn range unbounded preceding) between 20.01 and 80 then 'group_b'
           when sum(share.share) over (order by share.rn range unbounded preceding) between 80.01 and 100 then 'group_c'
           else 'other'
           end                                                             as group,
       case
           when share.client_name is not null then '3q_2021'
           end                                                             as quarter
from share
'''

query_abc_2021_4q = '''
with rtu as
         (select date(_date_time)                                     as date,
                 encode(1c_postgresql.public._document497._fld7908rref, 'hex') as client_id,
                 _fld7907                                             as sum
          from 1c_postgresql.public._document497
          where _posted = 'true'),
     client as
         (select encode(1c_postgresql.public._reference212._idrref, 'hex') as client_id,
                 _description                                     as client_name
          from 1c_postgresql.public._reference212),
     revenue as
         (select client.client_name,
                 round(sum(rtu.sum)::decimal / 1000, 0) as sum
          from rtu
                   join client on client.client_id = rtu.client_id
          where rtu.date between '2021-10-01' and '2021-12-31'
          group by 1
          order by 2 desc),
     all_sum as
         (select sum(revenue.sum) as all_sum
          from revenue),
     share as
         (select row_number() over ()                  as rn,
                 revenue.client_name,
                 revenue.sum,
                 all_sum,
                 round(revenue.sum / all_sum * 100, 2) as share
          from all_sum,
               revenue)
select
       share.client_name,
       share.sum,
       share.all_sum,
       share.share,
       sum(share.share) over (order by share.rn range unbounded preceding) as cumm_percent,
       case
           when sum(share.share) over (order by share.rn range unbounded preceding) between 0 and 20 then 'group_a'
           when sum(share.share) over (order by share.rn range unbounded preceding) between 20.01 and 80 then 'group_b'
           when sum(share.share) over (order by share.rn range unbounded preceding) between 80.01 and 100 then 'group_c'
           else 'other'
           end                                                             as group,
       case
           when share.client_name is not null then '4q_2021'
           end                                                             as quarter
from share
'''

query_abc_2022_1q = '''
with rtu as
         (select date(_date_time)                                     as date,
                 encode(1c_postgresql.public._document497._fld7908rref, 'hex') as client_id,
                 _fld7907                                             as sum
          from 1c_postgresql.public._document497
          where _posted = 'true'),
     client as
         (select encode(1c_postgresql.public._reference212._idrref, 'hex') as client_id,
                 _description                                     as client_name
          from 1c_postgresql.public._reference212),
     revenue as
         (select client.client_name,
                 round(sum(rtu.sum)::decimal / 1000, 0) as sum
          from rtu
                   join client on client.client_id = rtu.client_id
          where rtu.date between '2022-01-01' and '2022-03-31'
          group by 1
          order by 2 desc),
     all_sum as
         (select sum(revenue.sum) as all_sum
          from revenue),
     share as
         (select row_number() over ()                  as rn,
                 revenue.client_name,
                 revenue.sum,
                 all_sum,
                 round(revenue.sum / all_sum * 100, 2) as share
          from all_sum,
               revenue)
select
       share.client_name,
       share.sum,
       share.all_sum,
       share.share,
       sum(share.share) over (order by share.rn range unbounded preceding) as cumm_percent,
       case
           when sum(share.share) over (order by share.rn range unbounded preceding) between 0 and 20 then 'group_a'
           when sum(share.share) over (order by share.rn range unbounded preceding) between 20.01 and 80 then 'group_b'
           when sum(share.share) over (order by share.rn range unbounded preceding) between 80.01 and 100 then 'group_c'
           else 'other'
           end                                                             as group,
       case
           when share.client_name is not null then '1q_2022'
           end                                                             as quarter
from share
'''

query_abc_2022_2q = '''
with rtu as
         (select date(_date_time)                                     as date,
                 encode(1c_postgresql.public._document497._fld7908rref, 'hex') as client_id,
                 _fld7907                                             as sum
          from 1c_postgresql.public._document497
          where _posted = 'true'),
     client as
         (select encode(1c_postgresql.public._reference212._idrref, 'hex') as client_id,
                 _description                                     as client_name
          from 1c_postgresql.public._reference212),
     revenue as
         (select client.client_name,
                 round(sum(rtu.sum)::decimal / 1000, 0) as sum
          from rtu
                   join client on client.client_id = rtu.client_id
          where rtu.date between '2022-04-01' and '2022-06-30'
          group by 1
          order by 2 desc),
     all_sum as
         (select sum(revenue.sum) as all_sum
          from revenue),
     share as
         (select row_number() over ()                  as rn,
                 revenue.client_name,
                 revenue.sum,
                 all_sum,
                 round(revenue.sum / all_sum * 100, 2) as share
          from all_sum,
               revenue)
select
       share.client_name,
       share.sum,
       share.all_sum,
       share.share,
       sum(share.share) over (order by share.rn range unbounded preceding) as cumm_percent,
       case
           when sum(share.share) over (order by share.rn range unbounded preceding) between 0 and 20 then 'group_a'
           when sum(share.share) over (order by share.rn range unbounded preceding) between 20.01 and 80 then 'group_b'
           when sum(share.share) over (order by share.rn range unbounded preceding) between 80.01 and 100 then 'group_c'
           else 'other'
           end                                                             as group,
       case
           when share.client_name is not null then '2q_2022'
           end                                                             as quarter
from share
'''

query_abc_2022_3q = '''
with rtu as
         (select date(_date_time)                                     as date,
                 encode(1c_postgresql.public._document497._fld7908rref, 'hex') as client_id,
                 _fld7907                                             as sum
          from 1c_postgresql.public._document497
          where _posted = 'true'),
     client as
         (select encode(1c_postgresql.public._reference212._idrref, 'hex') as client_id,
                 _description                                     as client_name
          from 1c_postgresql.public._reference212),
     revenue as
         (select client.client_name,
                 round(sum(rtu.sum)::decimal / 1000, 0) as sum
          from rtu
                   join client on client.client_id = rtu.client_id
          where rtu.date between '2022-07-01' and '2022-09-30'
          group by 1
          order by 2 desc),
     all_sum as
         (select sum(revenue.sum) as all_sum
          from revenue),
     share as
         (select row_number() over ()                  as rn,
                 revenue.client_name,
                 revenue.sum,
                 all_sum,
                 round(revenue.sum / all_sum * 100, 2) as share
          from all_sum,
               revenue)
select
       share.client_name,
       share.sum,
       share.all_sum,
       share.share,
       sum(share.share) over (order by share.rn range unbounded preceding) as cumm_percent,
       case
           when sum(share.share) over (order by share.rn range unbounded preceding) between 0 and 20 then 'group_a'
           when sum(share.share) over (order by share.rn range unbounded preceding) between 20.01 and 80 then 'group_b'
           when sum(share.share) over (order by share.rn range unbounded preceding) between 80.01 and 100 then 'group_c'
           else 'other'
           end                                                             as group,
       case
           when share.client_name is not null then '3q_2022'
           end                                                             as quarter
from share
'''

query_abc_2022_4q = '''
with rtu as
         (select date(_date_time)                                     as date,
                 encode(1c_postgresql.public._document497._fld7908rref, 'hex') as client_id,
                 _fld7907                                             as sum
          from 1c_postgresql.public._document497
          where _posted = 'true'),
     client as
         (select encode(1c_postgresql.public._reference212._idrref, 'hex') as client_id,
                 _description                                     as client_name
          from 1c_postgresql.public._reference212),
     revenue as
         (select client.client_name,
                 round(sum(rtu.sum)::decimal / 1000, 0) as sum
          from rtu
                   join client on client.client_id = rtu.client_id
          where rtu.date between '2022-10-01' and '2022-12-31'
          group by 1
          order by 2 desc),
     all_sum as
         (select sum(revenue.sum) as all_sum
          from revenue),
     share as
         (select row_number() over ()                  as rn,
                 revenue.client_name,
                 revenue.sum,
                 all_sum,
                 round(revenue.sum / all_sum * 100, 2) as share
          from all_sum,
               revenue)
select
       share.client_name,
       share.sum,
       share.all_sum,
       share.share,
       sum(share.share) over (order by share.rn range unbounded preceding) as cumm_percent,
       case
           when sum(share.share) over (order by share.rn range unbounded preceding) between 0 and 20 then 'group_a'
           when sum(share.share) over (order by share.rn range unbounded preceding) between 20.01 and 80 then 'group_b'
           when sum(share.share) over (order by share.rn range unbounded preceding) between 80.01 and 100 then 'group_c'
           else 'other'
           end                                                             as group,
       case
           when share.client_name is not null then '4q_2022'
           end                                                             as quarter
from share
'''

# having round(sum(rtu.sum)::decimal / 1000, 0) > 5000

query_sku_abc_quarter = '''
with rtu as
         (select date_trunc('quarter', _date_time)                             as date,
                 _fld7907                                                    as sum,
                 encode(1c_postgresql.public._document497_vt7964._fld7966rref, 'hex') as sku_id
          from 1c_postgresql.public._document497
                   join 1c_postgresql.public._document497_vt7964
                        on 1c_postgresql.public._document497_vt7964._document497_idrref =
                           1c_postgresql.public._document497._idrref
          where _posted = 'true'
            and _date_time between '2021-01-01' and '2022-12-31'),
     sku as
         (select encode(1c_postgresql.public._reference185._idrref, 'hex') as sku_id,
                 1c_postgresql.public._reference185._description           as sku_name
          from 1c_postgresql.public._reference185
          where _folder = 'true'),
     all_sku as
         (select rtu.date                      as period,
                 sku.sku_name                  as sku,
                 round(sum(rtu.sum) / 1000, 0) as sum
          from rtu
                   join sku on sku.sku_id = rtu.sku_id
          group by 1, 2)
select all_sku.period,
       all_sku.sku,
       all_sku.sum,
       sum(all_sku.sum) over (partition by all_sku.period)                               as total,
       round(all_sku.sum / sum(all_sku.sum) over (partition by all_sku.period) * 100, 2) as share_percent
from all_sku
group by 1, 2, 3
order by 1, 5 desc
'''

query_sku_abc_month = '''
with rtu as
         (select date_trunc('month', _date_time)                             as date,
                 _fld7907                                                    as sum,
                 encode(1c_postgresql.public._document497_vt7964._fld7966rref, 'hex') as sku_id
          from 1c_postgresql.public._document497
                   join 1c_postgresql.public._document497_vt7964
                        on 1c_postgresql.public._document497_vt7964._document497_idrref =
                           1c_postgresql.public._document497._idrref
          where _posted = 'true'
            and _date_time between '2021-01-01' and '2022-12-31'),
     sku as
         (select encode(1c_postgresql.public._reference185._idrref, 'hex') as sku_id,
                 1c_postgresql.public._reference185._description           as sku_name
          from 1c_postgresql.public._reference185
          where _folder = 'true'),
     all_sku as
         (select rtu.date                      as period,
                 sku.sku_name                  as sku,
                 round(sum(rtu.sum) / 1000, 0) as sum
          from rtu
                   join sku on sku.sku_id = rtu.sku_id
          group by 1, 2)
select all_sku.period,
       all_sku.sku,
       all_sku.sum,
       sum(all_sku.sum) over (partition by all_sku.period)                               as total,
       round(all_sku.sum / sum(all_sku.sum) over (partition by all_sku.period) * 100, 2) as share_percent
from all_sku
group by 1, 2, 3
order by 1, 5 desc
'''