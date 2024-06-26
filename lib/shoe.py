#!/usr/bin/env python3

class Shoe:
    all = []
    def __init__(self,brand,size):
        self._brand = brand
        self._size = size
        self._condition = ''

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")
    def cobble(self):
        self.condition = 'New'
        print("Your shoe is as good as new!")