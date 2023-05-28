from ua.lviv.iot.algo.part1.managers.pen_manager import PenManager
from ua.lviv.iot.algo.part1.models.builder_pen import BuilderPen
from ua.lviv.iot.algo.part1.models.doctor_pen import DoctorPen
from ua.lviv.iot.algo.part1.models.marker_pen import MarkerPen
from ua.lviv.iot.algo.part1.models.school_pen import SchoolPen

if __name__ == '__main__':
    school = SchoolPen("", "", 21, 4, 5, 1)
    marker = MarkerPen("", "", 12, 4, False)
    builder = BuilderPen("", "", 58, 5, 6)
    doctor = DoctorPen("", "", 26, 3, True)
    pen_list = [school, marker, builder, doctor]
    print("All the pens are on the table:"
          + "\n---------------------")
    for x in pen_list:
        print(str(x))
    print("---------------------")
    pen_manager = PenManager(pen_list)

    print("\nPrinting out pens worth more than 10 UAH"
          + "\n---------------------")
    pen_manager.find_all_worth_more_than(10)
    print("---------------------")

    print("\nPrinting out pens larger than 25 sm^3"
          + "\n---------------------")
    pen_manager.find_all_bigger_than(25)
    print("---------------------")
