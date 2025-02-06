class BasicCalculator:

    def add(self, num1, num2):
        if ((isinstance(num1, int) or isinstance(num1, float)) and
                (isinstance(num2, int) or isinstance(num2, float))):
            return num1 + num2
        return None

    def subtract(self, num1, num2):
        if ((isinstance(num1, int) or isinstance(num1, float)) and
                (isinstance(num2, int) or isinstance(num2, float))):
            return num1 - num2
        return None

    def multiply(self, num1, num2):
        if ((isinstance(num1, int) or isinstance(num1, float)) and
                (isinstance(num2, int) or isinstance(num2, float))):
            return num1 * num2
        return None

    def divide(self, num1, num2):
        if ((isinstance(num1, int) or isinstance(num1, float)) and
                (isinstance(num2, int) or isinstance(num2, float))):
            return num1 / num2
        return None


if __name__ == '__main__':
    basic_calculator = BasicCalculator()
    #num1 = int(input("Zadej první číslo: "))
    #num2 = int(input("Zadej druhé číslo: "))
    num1 = 5
    num2 = 0
    print(f"{num1} + {num2} = {basic_calculator.divide(num1, num2)}")
