"""
Contains Pen class
"""
from abc import ABC, abstractmethod


class Pen(ABC):
    """
    Pen is a father class for all classes in the "lab1_unique" project.
    (except the PenManager class)
    """

    def __init__(self, id_="isn-101", color="", size=0.0):
        self.color = color
        self.size = size
        if id_ == "":
            self.id_ = "isn-101"
        else:
            self.id_ = id_

    def attributes_by_type(self, data_type):
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

    @abstractmethod
    def calculate_price(self):
        """
        abstract method for calculating the price of a pen
        by multiplying number of its items by corresponding prices
        """
        pass

    @abstractmethod
    def __str__(self):
        return f"ID:'{self.id_}', Color:'{self.color}', Size:'{self.size}'"
