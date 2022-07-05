# выебонский вариант решения 
# x = int(input())
# print(x, x*2, x*3, x*4, x*5, sep='---')

# from task10 import StringsWithSeparator
# from task1 import TestUnit
from typing import List


class TestUnit:
    def __init__(self, _class, _input, _output):
        self._class = _class
        self._input = _input
        self._output = _output
        self.is_passed = self.is_passed_test()
        print('testing...', self._class, end=' ')

    def is_passed_test(self):
        test = self._class(self._input)
        return test.__str__() == self._output


class StringsWithSeparator:
    def __init__(self, strings: List[str], separator: str = None):
        self.strings = strings
        if separator is None:
            self.separator = '***'
        else:
            self.separator = separator

    def separate(self):
        result = ''
        for string in self.strings:
            result += string + self.separator

        return result[:-len(self.separator)]

    def __repr__(self):
        return self.separate()

    
#--------- testing ----------
# if __name__ == '__main__':
#     test = TestUnit(StringsWithSeparator, ['7', '14', '21', '28', '35'], '7***14***21***28***35')
#     print('passed' if test.is_passed else 'failed')


# -------- running ----------
if __name__ == '__main__':
    value = int(input())
    sequence = [value * i for i in range(1, 6)]
    for i in range(len(sequence)):
        sequence[i] = str(sequence[i])
    result = StringsWithSeparator(sequence, separator='---')
    print(result)