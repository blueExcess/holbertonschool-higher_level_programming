#!/usr/bin/python3
# Print states by cities


from sys import argv
import MySQLdb

if __name__ == "__main__":
    username, password, database = argv[1:]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
    FROM hbtn_0e_4_usa.cities \
    INNER JOIN hbtn_0e_0_usa.states ON states.id = cities.state_id")

    querry = cur.fetchall()
    for row in querry:
        print(row)

    cur.close()
    db.close()
