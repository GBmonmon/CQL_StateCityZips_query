from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

cluster = Cluster()
session = cluster.connect()
session.set_keyspace('usdata')

update = SimpleStatement('''
    UPDATE cityinfo SET misc = %s WHERE
    state = 'CA' AND city = 'SAN FRANCISCO'
''')


session.execute(update,('Silicon Valley North',))

select = SimpleStatement('''
    SELECT * FROM cityinfo WHERE 
    state = 'CA' AND city = 'SAN FRANCISCO' 
''')

rows = session.execute(select)
for row in rows:
    print(row)
