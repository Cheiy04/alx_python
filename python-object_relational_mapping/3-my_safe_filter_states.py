# script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!

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

    query = """ SELECT * FROM states
                WHERE BINARY name = %s
                ORDER BY id
            """
    cursor.execute(query, (argv[4], ))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    conn.close()