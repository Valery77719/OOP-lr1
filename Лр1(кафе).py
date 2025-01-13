# TODO Написать 3 класса с документацией и аннотацией типов

#if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
 #   pass

import doctest

class Cafe:
    def __init__(self, seats: int, p_in_hall: int):
        """
        Создание и подготовка к работе объекта "Кафе"

        :param seats: Посадочные места
        :param p_in_hall: Количество людей в зале

        Примеры:
        >>> cafe = Cafe(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(seats, (int)):
            raise TypeError("Количество посадочных мест должно быть типа int ")
        if seats < 0:
            raise ValueError("Количество посадочных мест должно быть положительным числом")
        self.seats = seats

        if not isinstance(p_in_hall, (int)):
            raise TypeError("Количество людей в зале должно быть int")
        if p_in_hall < 0:
            raise ValueError("Количество людей в зале не может быть отрицательным числом")
        self.p_in_hall = p_in_hall

    def seats_left(self) -> int:

        """
        Функция, которая счиатет оставшиеся посадочные места

        :return: Сколько осталось посадочных мест

        Примеры:
        >>> cafe = Cafe(500, 0)
        >>> cafe.seats_left()
        """
        ...

    def is_empty_cafe(self) -> bool:
        """
        Функция которая проверяет является ли кафе пустым

        :return: Является ли кафе пустым

        Примеры:
        >>> cafe = Cafe(500, 0)
        >>> cafe.is_empty_cafe()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации