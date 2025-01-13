# TODO Написать 3 класса с документацией и аннотацией типов

#if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
 #   pass

import doctest


class Mill:
    def __init__(self, empty_space: int, flour:  float):
        """
        Создание и подготовка к работе объекта "Мельница"

        :param empty_space: Свободное место для зерна в килограммах
        :param flour: Количество муки в килограммах

        Примеры:
        >>> mill = Mill(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(empty_space, (int)):
            raise TypeError("Свободное место для зерна должно быть типа int ")
        if empty_space <= 0:
            raise ValueError("Свободное место для зерна должно быть положительным числом")
        self.empty_space = empty_space

        if not isinstance(flour, (int, float)):
            raise TypeError("Количество муки должно быть int или float")
        if flour < 0:
            raise ValueError("Количество муки не может быть отрицательным числом")
        self.flour = flour


    def add_millet(self, millet: int) -> None:
        """
        Доставка пшена в мельницу.
        :param millet: Количество добавляемого пшена в килограммах

        :raise ValueError: Если количество добавляемого пшена превышает свободное место в мельнице, то вызываем ошибку

        Примеры:
        >>> mill = Mill(1500, 200)
        >>> mill.add_millet(200)
        """
        if not isinstance(millet, (int)):
            raise TypeError("Добавляемое пшено должно быть типа int ")
        if millet < 0:
            raise ValueError("Добавляемое пшено должно быть положительным числом")
        ...

    def remove_flour(self, estimate_flour: float) -> None:
        """
        Извлечение муки из мельницы.

        :param estimate_flour: Объем извлекаемой муки в килограммах
        :raise ValueError: Если количество извлекаемой муки превышает количество имеющейся муки,
        то возвращается ошибка.

        :return: Объем реально извлеченного количества муки

        Примеры:
        >>> mill = Mill(500, 500)
        >>> mill.remove_flour(200)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации