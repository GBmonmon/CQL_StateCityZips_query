# CQL_StateCityZips_query

task1:
Add/revise the primary key in the cityinfo table to support wide rows

think about which columns should be the partition key and which should be clustering keys. 

Is zip-code a good partition key?

Are City,State good clustering keys?


task2:
Find all San Jose rows
add a column just into the San Jose rows (and no other rows) named “Misc” and enter value “Silicon Valley South” into the Misc column.
write queries (as many or as few queries as needed) that gets all rows that have a misc column with value “silicon valley south”


task3:
Find all San Francisco rows
add a column named “Misc” with entry “Silicon Valley North”,
Write queries (as many or as few queries as needed) that gets all rows that have a Misc column with value “Silicon Valley North”
