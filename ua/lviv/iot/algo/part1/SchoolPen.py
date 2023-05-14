class SchoolPen:
    """
    This class 
    """

    def __init__(self, id="isn-101", brand="", color="", material="", size="", num_pencils=0, num_pens=0, num_erasers=0):
        self.id = id
        self.brand = brand
        self.color = color
        self.material = material
        self.size = size
        self.num_pencils = num_pencils
        self.num_pens = num_pens
        self.num_erasers = num_erasers

    def add_pencil(self):
        self.num_pencils += 1

    def add_pen(self):
        self.num_pens += 1

    def remove_pencil(self):
        if self.num_pencils > 0:
            self.num_pencils -= 1
        else:
            print("No pencils left in the pen.")

    def remove_pen(self):
        if self.num_pens > 0:
            self.num_pens -= 1
        else:
            print("No pens left in the pen.")
