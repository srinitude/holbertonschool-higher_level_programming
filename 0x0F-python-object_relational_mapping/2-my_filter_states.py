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
    def filter_certain_states(*args):
        """
        List all of the states with certain name
        """
        conn = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=args[1],
                               passwd=args[2],
                               db=args[3])
        cur = conn.cursor()
        cur.execute("SELECT * FROM states WHERE name = {:s} ORDER BY id ASC"
                    .format(argv[4]))
        states = cur.fetchall()
        for state in states:
            print(state)
        cur.close()
        conn.close()


if __name__ == "__main__":
    from sys import argv

    HBTNDBRunner.filter_certain_states(*argv)
