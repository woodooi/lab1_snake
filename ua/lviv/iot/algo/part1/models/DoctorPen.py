"""
Contains DoctorPen class
"""
from ua.lviv.iot.algo.part1.models.Pen import Pen


class DoctorPen(Pen):
    """

    """
    SYRINGE_PRICE = 4
    STETHO_PRICE = 10

    def __init__(self, id_="isn-101", color="", size=0.0,
                 syringes=0, stethoscope=bool):
        self.num_syringes = syringes
        self.has_stethoscope = stethoscope
        super().__init__(id_, color, size)

    def calculate_price(self):
        if self.has_stethoscope:
            return self.num_syringes * self.SYRINGE_PRICE \
                 + self.STETHO_PRICE
        else:
            return self.num_syringes * self.SYRINGE_PRICE

    def __str__(self):
        return "DoctorPen(" + super().__str__() + \
               f" Syringes:'{self.num_syringes}', Stethoscope:'{self.has_stethoscope}')"
