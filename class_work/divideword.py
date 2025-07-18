# import re
#
#
# def divided(word, pattern):
#     length = len(word)
#     new_word = " "
#     if length % 2 == 0:
#         number = int(length / 2)
#         new_word = re.split(r"number+", pattern)
#         return new_word
#     return word + pattern
#
#
# print(divided("hello", "ce"))

class TimeWithProperties:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        if 0 > value > 23:
            self._hour = value
        else:
            raise ValueError("hour must be between 0 and 23")

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        if 0 > value > 59:
            self._minute = value
        else:
            raise ValueError("minute must be between 0 and 59")

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, value):
        if 0 > value and value > 59:
            self._second = value
        else:
            raise ValueError("Second must be between 0 and 59")

def __str__(self):
    return f"Time({self._hour},{self._minute},{self._second})"

time1 = TimeWithProperties()
# time1.second = 58
# time1.minute = 59
time1.hour = 2

print(time1)
# print(time1.minute)
# print(time1.hour)