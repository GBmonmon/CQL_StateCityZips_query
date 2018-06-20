from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

cluster = Cluster()
session = cluster.connect()
session.set_keyspace('usdata')

add_misc = SimpleStatement('''
    ALTER TABLE cityinfo ADD Misc text
''')

try:
    session.execute(add_misc)
except:
    print('Misc has already been there!')


update = SimpleStatement('''
    UPDATE cityinfo SET misc = %s
    WHERE state = 'CA' AND city = 'SAN JOSE';
''')
print('===')
session.execute(update,('Silicon Valley South',))

select = SimpleStatement('''
    SELECT * FROM cityinfo WHERE
    state = 'CA' AND city = 'SAN JOSE'
''')

rows = session.execute(select)
for row in rows:
    print(row)
