# script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
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

    query = """ SELECT * FROM states WHERE name like '{}'
                ORDER BY id ASC
            """.format(argv[4])
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    conn.close()