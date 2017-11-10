#!/usr/bin/python3
"""
Filter states from database hbtn_0e_0_usa with certain name
"""
import MySQLdb


class StateStr(str):
    """
    Custom string subclass
    """
    def contains(self, letter):
        """
        Tests to see if letter contains malicious character
        """
        for char in self:
            if char == letter:
                return True
        return False


class HBTNDBRunner:
    """
    Execute various SQL scripts
    """
    @staticmethod
    def filter_cities(*args):
        """
        List all of the states with certain name
        """
        conn = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=args[1],
                               passwd=args[2],
                               db=args[3])
        cur = conn.cursor()
        query = StateStr(args[4])
        if query.contains(";"):
            raise Exception("Hey hacker")
        query = "SELECT cities.name FROM cities "
        query += "JOIN states ON states.id = cities.state_id "
        query += "WHERE states.name = '{:s}' "
        query += "ORDER BY cities.id ASC"
        cur.execute(query.format(argv[4]))
        states = cur.fetchall()
        states_length = len(states)
        for i in range(0, states_length):
            if i == states_length - 1:
                print(states[i][0])
            else:
                print(states[i][0], end=", ")
        cur.close()
        conn.close()


if __name__ == "__main__":
    from sys import argv

    HBTNDBRunner.filter_cities(*argv)
