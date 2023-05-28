# pylint: disable = invalid-name
"""
Contains PenManager class
"""


class PenManager:
    """
    Describes a pen manager class. Contains a list of pens and several search functions
    """
    pen_storage = []

    @classmethod
    def __init__(cls, _list):
        cls.pen_storage = _list

    @classmethod
    def add_pen(cls, pen):
        """
        :param pen:
        adds a pen into a pen_storage
        """
        cls.pen_storage.append(pen)

    @classmethod
    def find_all_worth_more_than(cls, price):
        """
        :param price:
        prints pens more expensive than "price" using lambda expressions
        """
        expensive_pens = filter(lambda pen: pen.calculate_price() > price, cls.pen_storage)
        for pens in expensive_pens:
            print(pens)
#       _list = []
#       for pen in cls.pen_storage:
#           if pen.calculate_price() > price:
#               _list.append(pen)
#       return _list

    @classmethod
    def find_all_bigger_than(cls, size):
        """
        :param size:
        prints pens that are larger than "size" using lambda expressions
        """
        big_pens = filter(lambda pen: pen.size > size, cls.pen_storage)
        for pens in big_pens:
            print(pens)
#       _list = []
#        for pen in cls.pen_storage:
#            if pen.size > size:
#                _list.append(pen)
#       return _list
