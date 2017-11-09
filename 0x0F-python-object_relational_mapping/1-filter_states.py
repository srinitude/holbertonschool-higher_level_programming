#!/usr/bin/python3
"""
List all states from database hbtn_0e_0_usa
starting with an "N"
"""
import MySQLdb


class StateStr(str):
    """
    Custom string subclass
    """
    def first_letter(self, letter):
        """
        Tests to see if first letter of string matches another letter
        """
        return self[0] == letter


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
        cur.close()
        conn.close()
        return states

    @staticmethod
    def list_all_states_starting_with(letter, *args):
        """
        List all states starting with a certain letter
        """
        states = HBTNDBRunner.list_all_states(*args)
        for state in states:
            name = StateStr(state[1])
            if name.first_letter(letter):
                print(state)


if __name__ == "__main__":
    from sys import argv

    HBTNDBRunner.list_all_states_starting_with("N", *argv)
