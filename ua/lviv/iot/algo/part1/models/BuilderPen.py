"""
Contains BuilderPen class
"""
from ua.lviv.iot.algo.part1.models.Pen import Pen


class BuilderPen(Pen):
    """

    """

    SCREW_PRICE = 5
    RULER_PRICE = 3

    def __init__(self, id_="isn-101", color="", size=0.0,
                 rulers=0, screwdrivers=0):
        self.num_rulers = rulers
        self.num_screwdrivers = screwdrivers
        super().__init__(id_, color, size)

    def calculate_price(self):
        return self.num_rulers * self.SCREW_PRICE \
             + self.num_screwdrivers * self.SCREW_PRICE

    def __str__(self):
        return super().__str__() + \
               f"Rulers:'{self.num_rulers}', Screwdrivers:'{self.num_screwdrivers}'"

