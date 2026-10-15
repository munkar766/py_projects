class Jar:


    def __init__(self, capacity=12):

        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._size = 0
        self._capacity = capacity




    def __str__(self):

        return '🍪'*self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError
        else:
            self._size+=n
        ...

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError
        else:
            self._size -= n

        ...

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


