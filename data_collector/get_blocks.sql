SELECT
    *
FROM
  `bigquery-public-data.crypto_bitcoin.transactions` AS transactions
WHERE DATE(block_timestamp_month) BETWEEN {0} AND {1}

create table blocks_0_to_100k partition of blocks for values from (0)to(100000);
create table blocks_100k_to_200k partition of blocks for values from (100000)to(200000);
create table blocks_200k_to_300k partition of blocks for values from (200000)to(300000);
create table blocks_300k_to_400k partition of blocks for values from (300000)to(400000);
create table blocks_400k_to_500k partition of blocks for values from (400000)to(500000);
create table blocks_500k_to_600k partition of blocks for values from (500000)to(600000);
create table blocks_600k_to_700k partition of blocks for values from (600000)to(700000);
create table blocks_700k_to_800k partition of blocks for values from (700000)to(800000);
create table blocks_800k_to_900k partition of blocks for values from (800000)to(900000);
create table blocks_900k_to_1000k partition of blocks for values from (900000)to(1000000);
create table blocks_1000k_to_1100k partition of blocks for values from (1000000)to(1100000);


create table blocks_09 partition of blocks for values from ('2009-01-01')to('2009-12-31');
create table blocks_10 partition of blocks for values from ('2010-01-01')to('2010-12-31');
create table blocks_11 partition of blocks for values from ('2011-01-01')to('2011-12-31');
create table blocks_12 partition of blocks for values from ('2012-01-01')to('2012-12-31');
create table blocks_13 partition of blocks for values from ('2013-01-01')to('2013-12-31');
create table blocks_14 partition of blocks for values from ('2014-01-01')to('2014-12-31');
create table blocks_15 partition of blocks for values from ('2015-01-01')to('2015-12-31');
create table blocks_16 partition of blocks for values from ('2016-01-01')to('2016-12-31');
create table blocks_17 partition of blocks for values from ('2017-01-01')to('2017-12-31');
create table blocks_18 partition of blocks for values from ('2018-01-01')to('2018-12-31');
create table blocks_19 partition of blocks for values from ('2019-01-01')to('2019-12-31');
create table blocks_20 partition of blocks for values from ('2020-01-01')to('2020-12-31');
create table blocks_21 partition of blocks for values from ('2021-01-01')to('2021-12-31');
create table blocks_22 partition of blocks for values from ('2022-01-01')to('2022-12-31');
create table blocks_23 partition of blocks for values from ('2023-01-01')to('2023-12-31');
create table blocks_24 partition of blocks for values from ('2024-01-01')to('2024-12-31');
create table blocks_25 partition of blocks for values from ('2025-01-01')to('2025-12-31');
create table blocks_26 partition of blocks for values from ('2026-01-01')to('2026-12-31');
create table blocks_27 partition of blocks for values from ('2027-01-01')to('2027-12-31');
create table blocks_28 partition of blocks for values from ('2028-01-01')to('2028-12-31');
create table blocks_29 partition of blocks for values from ('2029-01-01')to('2029-12-31');
create table blocks_30 partition of blocks for values from ('2030-01-01')to('2030-12-31');



