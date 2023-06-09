"""
Contains BuilderPen class
"""
from ua.lviv.iot.algo.part1.models.pen import Pen


class BuilderPen(Pen):
    """
    Describes a builder pen class
    """
    SCREW_PRICE = 5
    RULER_PRICE = 3
    top_models = ["Brick", "Ruler"]

    def __init__(self, id_="", color="", size=0.0,
                 rulers=0, screwdrivers=0):
        self.num_rulers = rulers
        self.num_screwdrivers = screwdrivers
        super().__init__(id_, color, size)

    def calculate_price(self):
        """
        :return: num rulers + num screwdrivers, multiplied by corresponding prices
        """
        return self.num_rulers * self.SCREW_PRICE \
            + self.num_screwdrivers * self.SCREW_PRICE

    def __str__(self):
        return "BuilderPen(" + super().__str__() + \
               f" Rulers:'{self.num_rulers}', Screwdrivers:'{self.num_screwdrivers}')"
