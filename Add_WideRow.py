from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import csv


cluster = Cluster()
session = cluster.connect()
session.set_keyspace('usdata')

query_droptable = SimpleStatement('''
    DROP TABLE IF EXISTS usdata.cityinfo;
''')
session.execute(query_droptable)

query_widerow_table = SimpleStatement('''
    CREATE TABLE usdata.cityinfo(
        zip int,
        city text,
        loc text,
        pop int,
        state text,

        PRIMARY KEY(state,city)
    );
''')
session.execute(query_widerow_table)


with open('zips.csv', 'r') as fh:
    data = csv.reader(fh)
    for row in data:
        zip = int(row[0])
        city = row[1]
        loc = row[2]
        population = int(row[3])
        state = row[4]

        query_insert = SimpleStatement('''
           INSERT INTO usdata.cityinfo(zip, city, loc, pop, state) 
           VALUES(%s,%s,%s,%s,%s)
        ''')
        session.execute(query_insert,(zip,city,loc,population,state))


