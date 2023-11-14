#!/usr/bin/python3
""" Base module """


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize Base instance with id """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
