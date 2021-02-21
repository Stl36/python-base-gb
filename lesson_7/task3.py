"""
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных
двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух
клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному
аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.

"""


class Cell:

    def __init__(self, nucleus):
        if type(nucleus) == int and nucleus > 0:
            self.nucleus = nucleus
        else:
            raise TypeError("Количество ячеек должно быть целым положительным числом")

    def __add__(self, other):
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):
        if self.nucleus - other.nucleus < 1:
            raise ValueError("Вычитаемый компонент больше или равен чем уменьшаемый")
        return Cell(self.nucleus - other.nucleus)

    def __mul__(self, other):
        return Cell(self.nucleus * other.nucleus)

    def __truediv__(self, other):
        if self.nucleus < other.nucleus:
            raise ValueError("Делитель больше делимого компонента")
        return Cell(self.nucleus // other.nucleus)

    def make_order(self, row):
        my_str = ''
        for i in range(self.nucleus // row):
            my_str += '*' * row + "\n"
        if self.nucleus % row > 0:
            my_str += '*' * (self.nucleus % row) + "\n"
        return my_str


covid_19 = Cell(12)
hiv = Cell(4)
variola = Cell(21)
anthrax = Cell(134)

print(covid_19.make_order(7))
print(hiv.make_order(3))

print((covid_19 + hiv).nucleus)
print((variola - hiv).nucleus)
print((anthrax * hiv).nucleus)
print((anthrax / variola).make_order(21))