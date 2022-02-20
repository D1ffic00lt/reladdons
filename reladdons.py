""" Riffraff """
from datetime import datetime
import random
import emoji
from random import randint

rand = {}


class long(object):
    """
        longs
    """
    now = None
    time2 = datetime.now()
    now2 = time2.strftime("%Y-%m-%d %H:%M:%S")
    dt_start = datetime.strptime(now2, "%Y-%m-%d %H:%M:%S")
    now_date = datetime.now()
    time = 0

    def __init__(self):
        pass

    @classmethod
    def seconds(cls, data):
        """

        :return:
        """
        cls.now = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
        cls.time = cls.dt_start - cls.now
        cls.time = int(cls.time.total_seconds())

        return cls.time

    @classmethod
    def minutes(cls, data):
        """

        :return:
        """
        cls.now = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
        cls.time = cls.dt_start - cls.now
        cls.time = int(cls.time.total_seconds() // 60)

        return cls.time

    @classmethod
    def hours(cls, data):
        """

        :return:
        """
        cls.now = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
        cls.time = cls.dt_start - cls.now
        cls.time = int(cls.time.total_seconds() // 60) // 60

        return cls.time

    @classmethod
    def days(cls, data):
        """

        :return:
        """
        cls.now = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
        cls.time = cls.dt_start - cls.now
        cls.time = int((cls.time.total_seconds() // 60) // 60) // 24

        return cls.time

    @classmethod
    def mounts(cls, data):
        """

        :return:
        """
        cls.now = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
        cls.time = cls.dt_start - cls.now
        cls.time = int(((cls.time.total_seconds() // 60) // 60) // 24) // 30

        return cls.time

    @classmethod
    def years(cls, data):
        """

        :return:
        """
        cls.now = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
        cls.time = cls.dt_start - cls.now
        cls.time = int(((cls.time.total_seconds() // 60) // 60) // 24) // 365

        return cls.time


class mathematics(object):
    """
        math
    """
    kolv = 0
    result = 0

    def __init__(self):
        pass

    @classmethod
    def average(cls, *nums: int):
        """

        :param nums:
        :return:
        """
        for i in nums:
            cls.kolv += 1
            cls.result += i
        return float(cls.result) / cls.kolv

    @classmethod
    def percent(cls, num: int, percent: int, mod: str = "add"):
        """
         reladdons percent function
        :param num:
        :param percent:
        :param mod:
        :return:
        """
        if mod == "add":
            return num + (num / 100 * percent)
        elif mod == "remove":
            return num - (num / 100 * percent)
        elif mod == "percent":
            return num / 100
        elif mod == "get":
            return num / 100 * percent
        else:
            raise Exception("mod error(add/remove/get/percent)")


class randoms(object):
    """
        random
    """
    num3 = 0
    args_list2 = []
    out = []
    args_list = {}

    def __init__(self):
        pass

    @classmethod
    def randint(cls, number: int = 1, number2: int = None, key: str = None, array_long: int = 2,
                shuffle_long: int = 1):
        """

        :param number:
        :param number2:
        :param key:
        :param array_long:
        :param shuffle_long:
        :return:
        """
        cls.num3 += 1
        if key is None:
            key = str(random.randint(1, 999999))
        if number2 is None:
            rand[key] = []
            for i in range(array_long):
                rand[key].append(random.randint(1, number))
            for i in range(shuffle_long):
                random.shuffle(rand[key])

            return rand[key][0], rand[key]
        else:
            rand[key] = []
            for i in range(array_long):
                rand[key].append(random.randint(number, number2))
            for i in range(shuffle_long):
                random.shuffle(rand[key])
            return rand[key][0], rand[key]

    @classmethod
    def chance(cls, _from: int, _to: int):
        """

        :param _from:
        :param _to:
        :return:
        """
        if randint(_from, _to) == randint(_from, _to):
            return True
        return False

    @classmethod
    def coefficient(cls, coefficient: float):
        """

        :return:
        """
        if randint(0, 100) in range(0, int(coefficient * 100)):
            return True
        return False

    @classmethod
    def choice(cls, *args, output: int = 1, shuffle_long: int = 2, array_long: int = 1, key: str = None):
        """

        :param args:
        :param output:
        :param shuffle_long:
        :param array_long:
        :param key:
        :return:
        """
        if key is None:
            key = str(random.randint(1, 999999))
        rand[key] = []
        for i in args:
            cls.args_list2.append(i)
        for i in range(len(args)):
            cls.args_list[str(i)] = cls.args_list2[random.randint(0, len(args) - 1)]
        for i in range(array_long):
            rand[key].append(cls.args_list[str(random.randint(0, len(args) - 1))])
        for i in range(shuffle_long):
            random.shuffle(rand[key])
        for i in range(output):
            cls.out.append(rand[key][i])
        return cls.out


def razr(num):
    """

    :param num:
    :return:
    """
    num = int(num)
    return '{:,}'.format(num).replace('.', ' ')


class work_text(object):
    """
        work with text
    """

    text_no_emoji = None

    def __init__(self):
        self.text_no_emoji = ""

    @classmethod
    def remove_emoji(cls, text):
        """

        :param text:
        :return:
        """
        cls.text_no_emoji = emoji.get_emoji_regexp().sub(u'', text)
        return cls.text_no_emoji

    @classmethod
    def palindrome(cls, word: str):
        """

        :param word:
        :return:
        """
        if word != word[::-1]:
            return False
        return True
