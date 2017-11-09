#!/usr/bin/python3
"""
Filter states from database hbtn_0e_0_usa with certain name
"""
import MySQLdb


class HBTNDBRunner:
    """
    Execute various SQL scripts
    """
    @staticmethod
    def list_cities_and_states(*args):
        """
        List all of the states with certain name
        """
        conn = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=args[1],
                               passwd=args[2],
                               db=args[3])
        cur = conn.cursor()
        query = "SELECT cities.id, cities.name, states.name FROM cities "
        query += "JOIN states ON states.id = cities.state_id "
        query += "ORDER BY cities.id"
        cur.execute(query)
        city_states = cur.fetchall()
        for city_state in city_states:
            print(city_state)
        cur.close()
        conn.close()


if __name__ == "__main__":
    from sys import argv

    HBTNDBRunner.list_cities_and_states(*argv)
