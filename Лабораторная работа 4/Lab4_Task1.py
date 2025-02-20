# TODO: описать базовый класс
class Application:
    """
    Базовый класс для приложений.
    Атрибуты:
        developer (str): Разработчик приложения.
        app_type (str): Тип приложения (социальное, развлекательное, путеводитель).
    """

    def __init__(self, developer: str, app_type: str) -> None:
        self.developer = developer
        self.app_type = app_type

    @staticmethod
    def developer() -> str:
        """Возвращает разработчика."""
        return "Разбработчик"

    def __str__(self) -> str:
        """Возвращает тип приложения."""
        return "Тип приложения"

    def __repr__(self) -> str:
        """Возвращает описание приложения."""
        return f"Application(developer='{self.developer}', app_type='{self.app_type}')"


# TODO: описать дочерний класс
class WhatsApp(Application):
    """
    Класс для WhatsApp, наследующий от Application.
    Атрибуты:
        version (str): Версия приложения WhatsApp.
    """

    def __init__(self, developer: str, app_type: str, version: str) -> None:
        super().__init__(developer, app_type)  # Вызов конструктора базового класса
        self.__version = version  # Непубличный атрибут

    def __str__(self) -> str:
        """Возвращает версию приложения."""
        return f"{super().__str__()} - Версия: {self.__version}"

    def __repr__(self) -> str:
        """Возвращает описание приложения WhatsApp."""
        return f"WhatsApp(developer='{self.developer}', app_type='{self.app_type}', version='{self.__version}')"


# Дочерний класс для YouTube
class YouTube(Application):
    """
    Класс для YouTube, наследующий от Application.
    Атрибуты:
        version (str): Версия приложения YouTube.
    """

    def __init__(self, developer: str, app_type: str, version: str) -> None:
        super().__init__(developer, app_type)  # Вызов конструктора базового класса
        self.__version = version  # Непубличный атрибут

    def __str__(self) -> str:
        """Возвращает информацию о приложении YouTube."""
        return f"{super().__str__()} - Версия: {self.__version}"

    def __repr__(self) -> str:
        """Возвращает описание приложения YouTube."""
        return f"YouTube(developer='{self.developer}', app_type='{self.app_type}', version='{self.__version}')"


# Дочерний класс для 2GIS
class TwoGIS(Application):
    """
    Класс для 2GIS, наследующий от Application.
    Атрибуты:
        version (str): Версия приложения 2GIS.
    """

    def __init__(self, developer: str, app_type: str, version: str) -> None:
        super().__init__(developer, app_type)  # Вызов конструктора базового класса
        self.__version = version  # Непубличный атрибут

    def __str__(self) -> str:
        """Возвращает информацию о приложении 2GIS."""
        return f"{super().__str__()} - Версия: {self.__version}"

    def __repr__(self) -> str:
        """Возвращает описание приложения 2GIS."""
        return f"TwoGIS(developer='{self.developer}', app_type='{self.app_type}', version='{self.__version}')"


# Пример использования классов

if __name__ == "__main__":
    whatsapp = WhatsApp("Facebook", "Социальное", "2.21.11")
    youtube = YouTube("Google", "Развлекательное", "16.25.0")
    twogis = TwoGIS("3GIS", "Путеводитель", "5.9.7")

    print(repr(whatsapp))  # WhatsApp - Тип приложения: Социальное - Версия: 2.21.11
    print(repr(youtube))  # YouTube - Тип приложения: Развлекательное - Версия: 16.25.0
    print(repr(twogis))  # 2GIS - Тип приложения: Путеводитель - Версия: 5.9.7
