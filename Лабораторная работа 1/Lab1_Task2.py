# TODO: импортируйте классы, созданные в ходе выполнения прошлого задания
from Lab2_Task1 import Generator, Oscilloscope, Transistor

# TODO: инстанцировать все описанные классы, создав три объекта.C()
if __name__ == "__main__":
    generator = Generator(1000, 50)
    oscilloscope = Oscilloscope(100, 'Hantek DSO2D10', 7)
    transistor = Transistor('NPN', 0.5)

    # TODO: вызвать метод с некорректными аргументами(b)
    try:
        generator.adjust_frequency(-2)
    except ValueError:
        print('Ошибка: неправильные данные')

    # TODO: вызвать метод с некорректными аргументами(a)
    try:
        oscilloscope.set_bandwidth(-50)
    except ValueError:
        print('Ошибка: неправильные данные')

    # TODO: вызвать метод с некорректными аргументами(a)
    try:
        transistor.check_current(-15)
    except ValueError:
        print('Ошибка: неправильные данные')
