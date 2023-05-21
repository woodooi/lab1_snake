"""
Contains PenManager class
"""
from ua.lviv.iot.algo.part1.models.MarkerPen import MarkerPen
from ua.lviv.iot.algo.part1.models.SchoolPen import SchoolPen


class PenManager:
    pass


pen = SchoolPen("a1", "purple", 23.8, 2, 4, 5)
print(str(pen) + "\n" + str(SchoolPen.get_instance()))
marker = MarkerPen("a", "sad", 23.4, 1, True)
print(str(marker))

