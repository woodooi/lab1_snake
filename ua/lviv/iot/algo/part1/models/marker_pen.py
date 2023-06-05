from ua.lviv.iot.algo.part1.models.pen import Pen
"""
Contains MarkerPen class
"""


class MarkerPen(Pen):
    """
    Class describers a pen for markers
    """
    MARKER_PRICE = 3
    top_models = ["Purple", "Molberd"]

    def __init__(self, id_="isn=101", color="", size=0.0,
                 markers=0, pockets=bool):
        self.num_markers = markers
        self.has_pockets = pockets
        super().__init__(id_, color, size)

    def calculate_price(self):
        """
        :return: num_markers multiplied by its price
        """
        return self.num_markers * self.MARKER_PRICE

    def __str__(self):
        return "MarkerPen(" + super().__str__() + \
               f" Markers:'{self.num_markers}', Pockets:'{self.has_pockets}')"
