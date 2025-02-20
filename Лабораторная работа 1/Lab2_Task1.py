import doctest


class Generator:
    """Класс, описывающий генератор."""

    def __init__(self, power: float, frequency: float):
        """
        :param power: Мощность генератора в ваттах (Мощность должна быть больше 0)
        :param frequency: Частота генератора в герцах (Частота должна быть целым числом больше 0)

        >>> generator = Generator(1000, 50)
        >>> generator.power
        1000
        >>> generator.frequency
        50
        """
        if not isinstance(power, (int, float)):
            raise TypeError("Мощность должна быть типа int или float")
        if power <= 0:
            raise ValueError("Мощность должна быть положительна")

        if not isinstance(frequency, (int, float)):
            raise TypeError("Частота должна быть типа int или float")
        if frequency <= 0:
            raise ValueError("Частота должна быть положительна")

        self.power = power
        self.frequency = frequency

    def generate_signal(self) -> str:
        """
        Генерация сигнала.

        >>> generator = Generator(1000, 50)
        >>> generator.generate_signal()
        'Сигнал с мощностью 1000 Вт и частотой 50 Гц'
        """
        return f'Сигнал с мощностью {self.power} Вт и частотой {self.frequency} Гц'

    def adjust_frequency(self, new_frequency: float) -> None:
        """
        Изменение частоты генератора.

        :param new_frequency: Новая частота в герцах (Частота должна быть больше 0)
        :raise ValueError: Если новая частота не положительная, то вызываем ошибку

        >>> generator = Generator(1000, 50)
        >>> generator.adjust_frequency(60)
        >>> generator.frequency
        60
        """
        if not isinstance(new_frequency, (int, float)):
            raise TypeError("Частота должна быть типа int или float")
        if new_frequency <= 0:
            raise ValueError("Частота должна быть положительным числом")
        self.frequency = new_frequency


class Oscilloscope:
    """Класс, описывающий осциллограф."""

    def __init__(self, bandwidth: float, model: str, display_size: float):
        """
        :param bandwidth: Полосовая частота осциллографа в мегагерцах (Частота должна быть больше нуля)
        :param model: Модель осциллографа (Модель обязана указываться)
        :param display_size: Размер дисплея осциллографа в дюймах (Размер дисплея должен быть больше нуля)

        >>> oscilloscope = Oscilloscope(100, 'Hantek DSO2D10', 7)
        >>> oscilloscope.bandwidth
        100
        >>> oscilloscope.model
        'Hantek DSO2D10'
        >>> oscilloscope.display_size
        7
        """
        if not isinstance(bandwidth, (int, float)):
            raise TypeError("Полосовая частота должна быть типа int или float")
        if bandwidth <= 0:
            raise ValueError("Полосовая частота должна быть положительным числом")

        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not model:
            raise ValueError("Модель не может быть пустой строкой")

        if not isinstance(display_size, (int, float)):
            raise TypeError("Размер дисплея должен быть типа int или float")
        if display_size <= 0:
            raise ValueError("Размер дисплея должен быть положительным числом")

        self.bandwidth = bandwidth
        self.model = model
        self.display_size = display_size

    def measure_signal(self, frequency: float) -> str:
        """
        Измерение сигнала.

        :param frequency: Частота сигнала в герцах
        :return: Результат измерения

        >>> oscilloscope = Oscilloscope(100, 'Hantek DSO2D10', 7)
        >>> oscilloscope.measure_signal(50)
        'Измерение сигнала с частотой 50 Гц'
        """
        if not isinstance(frequency, (int, float)):
            raise TypeError("Частота должна быть типа int или float")
        if frequency <= 0:
            raise ValueError("Частота должна быть положительным числом")
        return f'Измерение сигнала с частотой {frequency} Гц'

    def set_bandwidth(self, new_bandwidth: float = 100) -> None:
        """
        Установка новой полосы частот.

        :param new_bandwidth: Новая полоса частот в мегагерцах (по умолчанию 100 МГц)

        >>> oscilloscope = Oscilloscope(100, 'Hantek DSO2D10', 7)
        >>> oscilloscope.set_bandwidth(200)
        >>> oscilloscope.bandwidth
        200
        """
        if not isinstance(new_bandwidth, (int, float)):
            raise TypeError("Полосовая частота должна быть типа int или float")
        if new_bandwidth <= 0:
            raise ValueError("Полосовая частота должна быть положительным числом")
        self.bandwidth = new_bandwidth


class Transistor:
    """Класс, описывающий транзистор."""

    def __init__(self, type: str, max_current: float):
        """
        :param type: Тип транзистора (например, 'NPN' или 'PNP')
        :param max_current: Максимальный ток через транзистор в амперах (Ток должен быть больше нуля)

        >>> transistor = Transistor('NPN', 0.5)
        >>> transistor.type
        'NPN'
        >>> transistor.max_current
        0.5
        """
        if type not in ['NPN', 'PNP']:
            raise ValueError("Тип транзистора должен быть 'NPN' или 'PNP'")
        if not isinstance(max_current, (int, float)):
            raise TypeError("Максимальный ток должен быть типа int или float")
        if max_current <= 0:
            raise ValueError("Максимальный ток должен быть положительным числом")

        self.type = type
        self.max_current = max_current

    def switch_on(self) -> str:
        """
        Включение транзистора.

        :return: Строка, указывающая на состояние транзистора

        >>> transistor = Transistor('NPN', 0.5)
        >>> transistor.switch_on()
        'Транзистор NPN включен'
        """
        return f'Транзистор {self.type} включен'

    def check_current(self, current: float) -> str:
        """
        Проверка тока через транзистор.

        :param current: Текущий ток в амперах (ток должен быть больше 0)
        :return: Строка с результатом проверки

        >>> transistor = Transistor('NPN', 0.5)
        >>> transistor.check_current(0.3)
        'Ток в пределах нормы'
        >>> transistor.check_current(0.6)
        'Ток превышает максимальный предел'
        """
        if not isinstance(current, (int, float)):
            raise TypeError("Ток должен быть типа int или float")
        if current < 0:
            raise ValueError("Ток не может быть отрицательным числом")
        if current > self.max_current:
            return 'Ток превышает максимальный предел'
        return 'Ток в пределах нормы'


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
