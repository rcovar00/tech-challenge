def validate_integer(f):
    def wrapper(self, *args):
        for value in args:
            if not isinstance(value, int):
                raise Exception("The value must be an integer")
            if value < 1 or value > 999:
                raise Exception("The value must be between 1 and 999")

        return f(self, *args)
    return wrapper


def validate_int_range(f):
    def wrapper(self, *args):
        start = args[0]
        end = args[1]

        if end < start:
            raise Exception("The end must be greater than or equal to start")

        return f(self, *args)
    return wrapper


def validate_execution(f):
    def wrapper(self, *args):
        if self.wasBuilt:
            raise Exception(
                "You cannot add more values after call build_stats()")

        return f(self, *args)
    return wrapper


class Stats:

    def __init__(self, data):
        self.data = data

    @validate_integer
    def less(self, n: int) -> int:
        if n < self.data.min_num:
            return 0
        elif n > self.data.max_num + 1:
            return self.data.less_than[self.data.max_num + 1]

        return self.data.less_than[n]

    @validate_integer
    @validate_int_range
    def between(self, start: int, end: int) -> int:
        first = start
        last = end + 1
        if start < self.data.min_num:
            first = self.data.min_num
        if end > (self.data.max_num + 1):
            last = self.data.max_num + 1

        return self.data.less_than[last] - self.data.less_than[first]

    @validate_integer
    def greater(self, n: int) -> int:
        if n > self.data.max_num:
            return 0
        elif n < self.data.min_num:
            return self.data.less_than[self.data.max_num + 1]

        return self.data.less_than[self.data.max_num +
                                   1] - self.data.less_than[n + 1]


class DataCapture:

    def __init__(self):
        self.values = {}
        self.less_than = {}  # Amount of numbers that are less than the key value
        self.min_num = None
        self.max_num = None
        self.wasBuilt = False

    @validate_execution
    @validate_integer
    def add(self, n: int) -> None:
        if self.min_num is None or n < self.min_num:
            self.min_num = n

        if self.max_num is None or n > self.max_num:
            self.max_num = n

        if n not in self.values:
            self.values[n] = 1
        else:
            self.values[n] += 1

    def build_stats(self) -> Stats:
        count = 0
        for x in range(self.min_num, self.max_num + 2):
            self.less_than[x] = count

            if x in self.values:
                count += self.values[x]

        self.wasBuilt = True

        return Stats(self)
