#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name != "first_name":
            e = "'LockedClass' object has no attribute '{}'".format(name)
            raise AttributeError(e)
        else:
            setattr(self, name, value)
