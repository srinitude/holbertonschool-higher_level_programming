#!/usr/bin/python3
"""
List all states from database hbtn_0e_0_usa
"""
import MySQLdb


class HBTNDBRunner:
    """
    Execute various SQL scripts
    """
    @staticmethod
    def list_all_states(*args):
        """
        List all of the states
        """
        conn = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=args[1],
                               passwd=args[2],
                               db=args[3])
        cur = conn.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        states = cur.fetchall()
        for state in states:
            print(state)
        cur.close()
        conn.close()


if __name__ == "__main__":
    from sys import argv

    HBTNDBRunner.list_all_states(*argv)
