use customer;
SELECT * from orders;

set SQL_SAFE_UPDATES=1;
start transaction;
delete from orders where id = 3;

rollback;

use IPL;
select * from teams;
select * from matches
where match_type="Final";