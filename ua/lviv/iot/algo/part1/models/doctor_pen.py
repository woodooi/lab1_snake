"""
Contains DoctorPen class
"""
from ua.lviv.iot.algo.part1.models.pen import Pen


class DoctorPen(Pen):
    """
    Describes a doctor pen class
    """
    SYRINGE_PRICE = 4
    STETHO_PRICE = 10
    top_models = ["Domestos", "Caries"]

    def __init__(self, id_="isn-101", color="", size=0.0,
                 syringes=0, stethoscope=bool):
        self.num_syringes = syringes
        self.has_stethoscope = stethoscope
        super().__init__(id_, color, size)

    def calculate_price(self):
        """
        :return: num syringes, multiplied by its price + stethoscope price, if there is one in the pen.
        """
        if self.has_stethoscope:
            price = self.num_syringes * self.SYRINGE_PRICE \
                 + self.STETHO_PRICE
        else:
            price = self.num_syringes * self.SYRINGE_PRICE
        return price

    def __str__(self):
        return "DoctorPen(" + super().__str__() + \
               f" Syringes:'{self.num_syringes}', Stethoscope:'{self.has_stethoscope}')"
