# TODO Написать 3 класса с документацией и аннотацией типов

#if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
 #   pass

import doctest


class Tree:
    def __init__(self, name: str, height: float):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param name: Название дерева
        :param height: Высота дерева в метрах

        Примеры:
        >>> tree = Tree("oak", 30)  # инициализация экземпляра класса
        """
        if not isinstance(name, (str)):
            raise TypeError("Название дерева должно быть типа str ")
        self.name = name

        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть int или float")
        if height <= 0:
            raise ValueError("Высота дерева не может быть отрицательным числом или равной нулю")
        self.height = height

    def is_tree(self) -> bool:
        """
        Функция которая проверяет есть ли дерево с таким названием

        :return: Присутствует ли дерево с таким названием

        Примеры:
        >>> tree = Tree("birch", 20)
        >>> tree.is_tree()
        """
        ...

    def is_height(self) -> bool:
        """
     Функция которая проверяет есть ли дерево с такой высотой

        :return: Присутствует ли дерево с такой высотой

        Примеры:
        >>> tree = Tree("birch", 25)
        >>> tree.is_height()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации