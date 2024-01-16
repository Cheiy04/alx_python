# script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa

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

    cursor.execute("SELECT * FROM states WHERE name like BINARY 'N%' ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    conn.close()