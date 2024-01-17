# script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa

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

    query = """ SELECT cities.name
                FROM cities 
                INNER JOIN states ON 
                cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id
            """
    cursor.execute(query, (argv[4],))
    states = cursor.fetchall()
    for i, state in enumerate(states):
        print(state[0], end='')
        if i < len(states)-1:
            print(', ', end='')
    print('')
        #     print("".join(state[0]), end=' ')
        # else:
        #     print("".join(state[0]), end=', ')

    cursor.close()
    conn.close()