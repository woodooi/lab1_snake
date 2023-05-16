# pylint: disable = invalid-name, too-many-instance-attributes
"""
This module contains SchoolPen class and
"""


class SchoolPen:
    """
    This class represents school pen, which contains pens, pencils, erasers.
    Class methods provide adding/removing items to and from the pen,
    and creating a unique instance of the class.
    """
    __instance = None

# pylint: disable = too-many-arguments
    def __init__(self, id_="isn-101", brand="", color="", material="",
                 size=0.0, num_pencils=0, num_pens=0, num_erasers=0):
        self.id_ = id_
        self.brand = brand
        self.color = color
        self.material = material
        self.size = size
        self.num_pencils = num_pencils
        self.num_pens = num_pens
        self.num_erasers = num_erasers

    @classmethod
    def get_instance(cls):
        """
        returns an instance of a class
        """
        if cls.__instance is None:
            cls.__instance = SchoolPen()
        return cls.__instance

    @staticmethod
    def print_hello():
        """
        prints "Hello"
        """
        print("Hello")

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
        self.num_erasers += 1

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
        return f" SchoolPen(id='{self.id_}', brand='{self.brand}', color='{self.color}'," \
               f" material='{self.material}', size={self.size}, num_pencils={self.num_pencils}," \
               f" num_pens={self.num_pens}, num_erasers={self.num_erasers})"


if __name__ == '__main__':
    pen = SchoolPen("a1", "Mercedes", "purple", "wood", 23.8, 2, 4, 5)
    print(str(pen) + "\n" + str(SchoolPen.get_instance()))
    SchoolPen.print_hello()

i = 0
list_50 = []
while i < 51:
    list_50.append(i)
    i += 1
print(list_50[:25:-1])
