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
    def __init__(cls, _list, index=0):
        cls.pen_storage = _list
        cls.index = index

    def __iter__(self):
        """
        __iter__ overwriting
        :return: self
        """
        return self

    def __next__(self):
        """
        __next__ overwriting
        :return: item with corresponding index
        """
        if self.index >= len(self):
            raise StopIteration
        item = self[self.index]
        self.index += 1
        return item

    def __getitem__(self, item):
        """
        __getitem__ overwriting
        :param item:
        :return: pen_storage[item]
        """
        return self.pen_storage[item]

    def __len__(self):
        """
        __len__overwriting
        :return: length of pen_storage
        """
        return len(self.pen_storage)

    @classmethod
    def price_list(cls):
        """
        executes method calculate_price for every pen in the pen_storage
        :return: list of pen`s prices
        """
        prices_ = [pen.calculate_price() for pen in cls.pen_storage]
        return prices_

    @classmethod
    def find_all_worth_more_than(cls, price):
        """
        :param price:
        prints pens more expensive than "price" using lambda expressions
        """
        expensive_pens = filter(lambda pen: pen.calculate_price() > price, cls.pen_storage)
        for pens in expensive_pens:
            print(pens)

    def pen_with_index(self, name):
        """
        :param name:
        :return enumerated object with index "index":
        """
        for number, pen in enumerate(self.pen_storage, 1):
            if pen == name:
                return number, str(pen)

    def pen_with_price(self, name):
        """
        :param name:
        :return pen + its price:
        """
        for pen in self.pen_storage:
            if pen == name:
                return str(name), pen.calculate_price()

    @classmethod
    def if_has_id(cls):
        id_list = []
        bool_list = []
        for pen in cls.pen_storage:
            id_list.append(pen.id_)
        for id_ in id_list:
            bool_list.append(id_ == 'isn-101')
        return {'any': any(bool_list), 'all': all(bool_list)}

    @classmethod
    def find_all_bigger_than(cls, size):
        """
        :param size:
        prints the list of pens, bigger than size
        """
        big_pens = [pen for pen in cls.pen_storage if pen.size > size]
        for x in big_pens:
            print(str(x))
