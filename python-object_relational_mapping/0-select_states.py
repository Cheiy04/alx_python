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
    cursor.execute('SELECT * FROM states ORDER BY id ASC')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()