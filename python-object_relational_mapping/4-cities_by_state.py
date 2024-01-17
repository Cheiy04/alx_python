#

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db_config = {
        'host':     'localhost',
        'user':     argv[1],
        'passwd':   argv[2],
        'db':       argv[3],
        'port':     3306
    }

    conn = MySQLdb.connect(**db_config)
    cursor = conn.cursor()

    query = """ SELECT states.name, cities.id, cities.name, FROM cities
                INNER JOIN states ON
                cities.state_id = states.id 
                ORDER BY cities.id
            """
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    conn.close()