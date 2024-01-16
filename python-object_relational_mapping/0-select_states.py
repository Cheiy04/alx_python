import MySQLdb
from sys import argv

if __name__ == '__main__':
    mysql_username = argv[1]
    mysql_pass = argv[2]
    db_name = argv[3]

    conn = MySQLdb.connect(host='localhost', passwd=mysql_pass, port=3306, user=mysql_username, db=db_name)

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()


