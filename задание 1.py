# TODO Написать 3 класса с документацией и аннотацией типов

class Home:
    """
    Документация на класс.
    Класс описывает дом человека.
    """
    def __init__(self, square_meters: (int, float), number_of_rooms: int):
        """
        Создание и подготовка к работе объекта 'Дом'

        :param square_meters: количество квадратных метров дома
        :param number_of_rooms: количество комнат дома

        Примеры:
        >>> cottage = Home(200, 5)
        """
        """Инициализация экземпляра класса"""
        if not isinstance(square_meters, (int, float)):  # Проверка на правильное введение площади дома
            raise TypeError("Нужно ввести число")
        if square_meters < 10:
            raise ValueError("Таких маленьких квартир в России не существует(")
        self.square_meters = square_meters
        if not isinstance(number_of_rooms, int):  # Проверка на правильный ввод количества комнат дома
            raise TypeError("Введите целое число")
        if number_of_rooms <= 0:
            raise ValueError("Квартир с нулём комнат не бывает")
        self.number_of_rooms = number_of_rooms

    def home_price(self, square_meters: (int, float), number_of_rooms: int, distance_to_city_center: (int, float)) -> (int, float):
        """
        Функция, которая вычисляет вычисляет цену дома на рынке

        :return: Сколько стоит дом?

        Примеры:
        >>> cottage_price = Home(200, 5)
        >>> cottage_price.home_price(200, 5, 27)
        """
        ...

    def comfort(self, square_meters: (int, float), number_of_rooms: int, distance_to_city_center: (int, float)) -> (int, float):
        """
        Функция вычисляет насколько человеку комфортно жить в таком доме

        :return: В вашем доме по 10-балльной шкале комфортно жить на...

        Прмиеры:
        >>> cottage_price = Home(200, 5)
        >>> cottage_price.comfort(200, 5, 27)
        """
        ...


class Car:
    """
    Документация на класс.
    Класс описывает машину человека.
    """
    def __init__(self, price_in_dollars: (int, float), model: str, year_of_manufacture: int):
        """
                Создание и подготовка к работе объекта 'Машина'

                :param price_in_dollars: цена машины в долларах
                :param model: марка автомобиля
                :param year_of_manufacture: год создания автомобиля

                Примеры:
                >>> lamborghini = Car(2000000, "Lamborghini", 2015)
                """
        if not isinstance(price_in_dollars, (int, float)):  # Проверка на правильный ввод цены автомобиля
            raise TypeError("Вводите цену цифрами")
        if price_in_dollars < 100:
            raise ValueError("Машина не может быть настолько дешёвой")
        self.price_in_dollars = price_in_dollars
        if not isinstance(model, str):  # Проверка на правильное введение наименования автомобиля
            raise TypeError("Вводите текст, а не буквы")
        self.model = model
        if not isinstance(year_of_manufacture, int):  # Проверка на правильное введение года выпуска
            raise TypeError("Введите целое число года, когда была выпущена машина")
        if year_of_manufacture < 1900 or year_of_manufacture > 2023:
            raise ValueError("Укажите год выпуска в диапазоне 1900-2023")
        self.year_of_manufacture = year_of_manufacture

    def horsepower(self, power: int) -> int:
        """
        Функция переводит мощность из киловатт в лошадиные силы

        :param power: мощность двигателя в киловаттах

        Примеры:
        >>> power_normal = Car(100000, "Lexus", 2020)
        >>> power_normal.horsepower(200)
        """
        ...

    def max_speed(self, way: int, time: float) -> int:
        """
        Функция находит максимальную скорость автомобиля

        :param way: Путь, который проехала машина на максимальной скорости.
        :param time: Время, которое машина затратила на путь

        Примеры:
        >>> speed_normal = Car(20000, "Kia", 2021)
        >>> speed_normal.max_speed(4, 1.32)
        """
        ...

    def car_rating(self, price_in_dollars: (int, float), model: str, horsepower: int, max_speed: int) -> float:
        """
        Функция оценивает машину по 10-балльной шкале


        :param price_in_dollars: цена автомобиля в долларах
        :param model: марка автомобиля
        :param max_speed: максимальная скорость автомобиля
        :param horsepower: лошадиные силы автомобиля

        Примеры:
        >>> speed_normal = Car(20000, "Kia", 2021)
        >>> speed_normal.car_rating(20000, "Kia", 180, 231)
        """
        ...


class Work:
    """
    Документация на класс.
    Класс описывает работу человека.
    """
    def __init__(self, salary_in_dollars: (int, float), name: str):
        """
        Создание и подготовка к работе объекта 'Работа'

        :param salary_in_dollars: зарплата в долларах
        :param name: наименование должности

        >>> work = Work(2500, "C++ backend developer")
        """
        if not isinstance(salary_in_dollars, (int, float)):  # Проверка на правильное введение зарплаты человека
            raise TypeError("Вводите числа")
        if salary_in_dollars < 175.69:  # Зарплата должна быть больше, чем МРОТ
            raise ValueError("Зарплата может быть только больше МРОТ")
        self.salary = salary_in_dollars
        if not isinstance(name, str):  # Проверка на правильное введение наименования должности
            raise TypeError("Вводите текст, а не буквы")
        self.name = name

    def danger_at_work(self, name: str, quantity_of_danger: int, percent_of_danger_area: (float, int)) -> (int, float):
        """
        Функция оценивает насколько опасна работа для человеческого организма по 10-балльной шкале

        :param name: наименование должности
        :param quantity_of_danger: количество опасных областей
        :param percent_of_danger_area: процент опасных областей от всей площади места работы

        >>> work = Work(2500, "C++ backend developer")
        >>> work.danger_at_work("C++ backend developer", 3, 7)
        """
        ...

    def happiness(self, danger_at_work: (float, int), respectability: (float, int), salary_in_dollars: (float, int)) -> (float, int):
        """
        Функция вычисляет насколько человек счастлив на работе по 10-балльной шкале

        :param danger_at_work: опасность работы
        :param respectability: респектабельность работы
        :param salary_in_dollars: зарплата в долларах

        >>> work = Work(2500, "C++ backend developer")
        >>> work.happiness(1.37, 8.21, 2500)
        """
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
