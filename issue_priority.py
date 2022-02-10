import abc


class Base:
    def __init__(self):
        self.base = 1


class BaseOne:
    def __init__(self):
        self.base_one = 2


class Child(Base, BaseOne, Base, BaseOne):
    """Some Child class"""


class ChildOne(Base, BaseOne, Base, BaseOne, abc.ABC, abc.ABCMeta, abc.ABCMeta):
    """Class with duplicate bases"""


def get_number(min_max=[1, 10]):
    assert all([isinstance(i, int) for i in min_max])
    return random.randint(*min_max)


def play_with_magic_numbers():
    magic_numbers = {0, 1, 1, 2, 3, 5}

    for elem in magic_numbers:
        magic_numbers.add(get_next(elem))
    return magic_numbers
