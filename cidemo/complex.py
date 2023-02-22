from typing import Union


class Complex:
    def __init__(self, real=0.0, image=0.0):
        self.__real = real
        self.__image = image

    @property
    def real(self):
        return self.__real

    @property
    def image(self):
        return self.__image

    def __add__(self, other: Union[int, float, 'Complex']) -> 'Complex':
        if isinstance(other, (int, float)):
            return Complex(self.real + other, self.image)
        if isinstance(other, type(self)):
            return Complex(self.real + other.real, self.image + other.image)
        raise TypeError
