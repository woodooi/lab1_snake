# pylint: disable = import-error, invalid-name
"""
Contains PenManager class
"""
from ua.lviv.iot.algo.part1.models.BuilderPen import BuilderPen
from ua.lviv.iot.algo.part1.models.DoctorPen import DoctorPen
from ua.lviv.iot.algo.part1.models.MarkerPen import MarkerPen
from ua.lviv.iot.algo.part1.models.SchoolPen import SchoolPen


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
        :return: list of pens, more expensive than price
        """
        _list = []
        for pen in cls.pen_storage:
            if pen.calculate_price() > price:
                _list.append(pen)
        return _list

    @classmethod
    def find_all_bigger_than(cls, size):
        """
        :param size:
        :return: list of pens that are larger than size
        """
        _list = []
        for pen in cls.pen_storage:
            if pen.size > size:
                _list.append(pen)
        return _list


if __name__ == '__main__':
    school = SchoolPen("", "", 21, 4, 5, 1)
    marker = MarkerPen("", "", 12, 4, False)
    builder = BuilderPen("", "", 58, 5, 6)
    doctor = DoctorPen("", "", 26, 3, True)
    pen_list = [school, marker, builder, doctor]
    for x in pen_list:
        print(str(x))
    pen_manager = PenManager(pen_list)
    price_list = PenManager.find_all_worth_more_than(18)
    size_list = PenManager.find_all_bigger_than(25)

    print("\nPrinting out pens worth more than 10 UAH"
          + "\n---------------------")
    for x in price_list:
        print(str(x))
    print("---------------------")

    print("\nPrinting out pens larger than 25 sm^3"
          + "\n---------------------")
    for x in size_list:
        print(str(x))
    print("---------------------")
