#!/usr/bin/python3
""" display all datas that meets the criteria """
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) >= 5:
        db_connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
        )
        cursor = db_connection.cursor()
        state_name = sys.argv[4]
        cursor.execute(
            "SELECT * FROM states WHERE CAST(name AS BINARY) "
            + "LIKE %s ORDER BY id ASC;",
            [state_name],
        )
        results = cursor.fetchall()
        for result in results:
            print(result)
        db_connection.close()
