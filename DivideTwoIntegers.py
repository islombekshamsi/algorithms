class DivideTwoIntegers:
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor
    def DivideTwoIntegers(self):
        if self.divisor < 0 and self.dividend < 0:
            self.divisor -= (self.divisor + self.divisor)
            self.dividend -= (self.dividend + self.dividend)
            output = self.dividend // self.divisor
            if output > (2 ** 31 - 1):
                output = 2 ** 31 - 1
        elif self.divisor < 0:
            self.dividend -= (self.dividend + self.dividend)
            output = self.dividend // self.divisor
            output -= (output + output)
            if output < (-2 ** 31):
                output = (-2 ** 31)
        elif self.dividend < 0:
            self.divisor -= (self.divisor + self.divisor)
            output = self.dividend // self.divisor
            output -= (output + output)
            if output < (-2 ** 31):
                output = (-2 ** 31)
        else:
            output = self.dividend // self.divisor
            if output > (2 ** 31 - 1):
                output = 2 ** 31 - 1
        return output


n = DivideTwoIntegers(7, -3)
print(n.DivideTwoIntegers())
