

/** Inner join **/
SELECT orders.*
FROM orders
JOIN accounts
ON orders.account_id = accounts.id;

/** **/
SELECT accounts.name, orders.occurred_at
FROM orders
JOIN accounts
ON orders.account_id = accounts.id;

/** **/
SELECT orders.*,accounts.*
FROM orders
JOIN accounts
ON orders.account_id = accounts.id;

/** **/
SELECT orders.standard_qty,orders.gloss_qty,orders.poster_qty,
accounts.website,accounts.primary_poc
FROM orders
JOIN accounts
ON orders.account_id = accounts.id;

/**joioning more than two table**/
SELECT *
FROM web_events
JOIN accounts
ON web_events.account_id = accounts.id
JOIN orders
ON accounts.id = orders.account_id

 /** giving table name aliases **/
 Select t1.column1 aliasname, t2.column2 aliasname2
FROM tablename AS t1
JOIN tablename2 AS t2
/** **/
select a.name,s.name
from accounts as a
join sales_reps as s
on a.sales_rep_id= s.id
join region as r
on r.id = s.region_id
/** **/
SELECT r.name region, a.name account,
       o.total_amt_usd/(o.total + 0.01) unit_price
FROM region r
JOIN sales_reps s
ON s.region_id = r.id
JOIN accounts a
ON a.sales_rep_id = s.id
JOIN orders o
ON o.account_id = a.id;
