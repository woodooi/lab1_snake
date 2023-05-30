from ua.lviv.iot.algo.part1.managers.pen_manager import PenManager
from ua.lviv.iot.algo.part1.models.builder_pen import BuilderPen
from ua.lviv.iot.algo.part1.models.doctor_pen import DoctorPen
from ua.lviv.iot.algo.part1.models.marker_pen import MarkerPen
from ua.lviv.iot.algo.part1.models.school_pen import SchoolPen

if __name__ == '__main__':
    school = SchoolPen("a1", "", 21, 4, 5, 1)
    marker = MarkerPen("", "", 12, 4, False)
    builder = BuilderPen("b1", "", 58, 5, 6)
    doctor = DoctorPen("", "", 26, 3, True)
    pen_list = [school, marker, builder, doctor]
    pen_manager = PenManager(pen_list)
    print("All the pens are on the table:"
          + "\n---------------------")
    for x in pen_manager:
        print(str(x))
    print("---------------------")

    print("\nPrinting out pens worth more than 10 UAH"
          + "\n---------------------")
    pen_manager.find_all_worth_more_than(10)
    print("---------------------")

    print("\nPrinting out pens larger than 25 sm^3"
          + "\n---------------------")
    pen_manager.find_all_bigger_than(25)
    print("---------------------")
    prices_ = pen_manager.price_list()
    for x in prices_:
        print(x)
    print(pen_manager.pen_with_index(school))
    print(pen_manager.pen_with_price(school))
    print(school.attributes_by_type(str))
    print(pen_manager.if_has_id())
    print(pen_manager[1])

