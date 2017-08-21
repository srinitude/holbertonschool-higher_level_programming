#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        result = fct(*args)
    except Exception as e:
        result = None
        print("Exception: {}".format(e), file=stderr)
    finally:
        return result
