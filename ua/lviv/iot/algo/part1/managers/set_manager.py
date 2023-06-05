from ua.lviv.iot.algo.part1.managers.pen_manager import PenManager

"""
Contains SetManager class
"""


class SetManager:
    """
    SetManager class
    """
    all_top = []

    def __init__(self, manager: PenManager):
        self.manager = manager
        self.index = 0
        for pen in manager:
            for sales in pen.top_models:
                self.all_top.append(sales)

    def __len__(self):
        """
        __len__ overwriting
        :return: length of all_top
        """
        return len(self.all_top)

    def __getitem__(self, item):
        try:
            return self.all_top[item]
        except IndexError:
            print("No such object exist")

    def __iter__(self):
        """
        __iter__ overwriting
        :return: iter object
        """
        return self

    def __next__(self):
        """
        __next__ overwriting
        :return item:
        """
        if self.index >= len(self):
            raise StopIteration
        else:
            item = self[self.index]
            self.index += 1
            return item
