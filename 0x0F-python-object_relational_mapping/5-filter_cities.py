#!/usr/bin/python3
# cities by state


from sys import argv
import MySQLdb

if __name__ == "__main__":
    username, password, database, state = argv[1:]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
        INNER JOIN states ON states.id = cities.state_id \
        WHERE states.name = %s;", (state,))
    # cur.execute("SELECT * FROM hbtn_0e_0_usa.states \
    # INNER JOIN hbtn_0e_4_usa.cities ON states.id = cities.state_id \
    # WHERE states.name LIKE %s", (state,))

    querry = cur.fetchall()
    count = 0
    lis = []
    for row in querry:
        lis.append(row[0])
    print(', '.join(lis))
    cur.close()
    db.close()
