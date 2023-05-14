class SchoolPen:
    """
    This class represents school pen, which contains pens, pencils, erasers.
    Class methods provide adding/removing items to and from the pen,
    and creating a unique instance of the class.
    """

    def __init__(self, id="isn-101", brand="", color="", material="",
                 size=0.0, num_pencils=0, num_pens=0, num_erasers=0):
        self.id = id
        self.brand = brand
        self.color = color
        self.material = material
        self.size = size
        self.num_pencils = num_pencils
        self.num_pens = num_pens
        self.num_erasers = num_erasers

    @staticmethod
    def get_instance():
        """
        returns an instance of a class
        """
        return SchoolPen()

    def add_pencil(self):
        """
        increases num_pencils by 1
        """
        self.num_pencils += 1

    def add_pen(self):
        """
        increases num_pens by 1
        """
        self.num_pens += 1

    def add_eraser(self):
        """
        increases num_erasers by 1
        """
        self.num_erasers +=1

    def remove_pencil(self):
        """
        decreases num_pencils by 1
        if num_pencils = 0 - prints a statement
        """
        if self.num_pencils > 0:
            self.num_pencils -= 1
        else:
            print("No pencils left in the pen.")

    def remove_pen(self):
        """
        decreases num_pens by 1
        if num_pens = 0 - prints a statement
        """
        if self.num_pens > 0:
            self.num_pens -= 1
        else:
            print("No pens left in the pen.")

    def remove_eraser(self):
        """
        decreases num_erasers by 1
        if num_erasers = 0 - prints a statement
        """
        if self.num_erasers > 0:
            self.num_erasers -= 1
        else:
            print("No erasers left in the pen")

    def __str__(self):
        """
        returns an object in string
        """
        return f"SchoolPen(id='{self.id}', brand='{self.brand}', color='{self.color}'," \
               f" material='{self.material}', size={self.size}, num_pencils={self.num_pencils}," \
              f" num_pens={self.num_pens}, num_erasers={self.num_erasers})"


pen = SchoolPen("a1", "Mercedes", "purple", "wood", 23.8, 2, 4, 5)
print(str(pen) + "\n" + str(SchoolPen.get_instance()))

