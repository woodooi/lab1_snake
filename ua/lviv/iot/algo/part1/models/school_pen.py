# pylint: disable = invalid-name, too-many-instance-attributes
"""
Contains SchoolPen class
"""
from ua.lviv.iot.algo.part1.decorators import logged
from ua.lviv.iot.algo.part1.models.pen import Pen
from ua.lviv.iot.algo.part1.my_exception import ZeroItemsError


class SchoolPen(Pen):
    """
    This class represents school pen, which contains pens, pencils, erasers.
    Class methods provide adding/removing items to and from the pen,
    and creating a unique instance of the class.
    """
    __instance = None
    PEN_PRICE = 2
    PENCIL_PRICE = 1
    ERASER_PRICE = 6
    top_models = ["Gymnasium", "Garden"]

    # pylint: disable = too-many-arguments
    def __init__(self, id_="isn-101", color="", size=0.0,
                 num_pencils=0, num_pens=0, num_erasers=0):
        self.num_pencils = num_pencils
        self.num_pens = num_pens
        self.num_erasers = num_erasers
        super().__init__(id_, color, size)

    @classmethod
    def get_instance(cls):
        """
        returns an instance of a class
        """
        if cls.__instance is None:
            cls.__instance = SchoolPen()
        return cls.__instance

    @logged(ZeroItemsError, "console")
    def remove_pen(self):
        if self.num_pens == 0:
            raise ZeroItemsError(type(self))
        else:
            self.num_pens -= 1

    def calculate_price(self):
        """
        :return: num pens, num pencils and num erasers, multiplied by corresponding prices
        """
        return self.num_erasers * self.ERASER_PRICE \
             + self.num_pens * self.PEN_PRICE \
             + self.num_pencils * self.PENCIL_PRICE

    def __str__(self):
        """
        returns an object in string
        """
        return "SchoolPen(" + super().__str__() + \
            f" Num_pencils:{self.num_pencils}, Num_pens:{self.num_pens}, Num_erasers:{self.num_erasers})"
