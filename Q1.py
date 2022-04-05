class Calculator:

    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        self.result = 0

    #Addition of  2 numbers
    def adder(self):
        self.result = self.input1 + self.input2
        print("{} + {} is {:.2f}".format(self.input1, self.input2, self.result))

    #Subtraction of 2 numbers
    def subtractor(self):
        self.result = self.input1 - self.input2
        print("{} - {} is {:.2f}".format(self.input1, self.input2, self.result))

    #Multiplication of 2 numbers
    def multiplier(self):
        self.result = self.input1 * self.input2
        print("{} X {} is {:.2f}".format(self.input1, self.input2, self.result))

    #Dividision of 2 numbers
    # If second input(divisor) is 0 , then print an error message
    def divider(self):
        if self.input2 == 0:
            print("Cannot be divided by 0")
        else:
            self.result = self.input1 / self.input2
            print("{} / {} is {:.2f}".format(self.input1, self.input2, self.result))

    #reset to 0
    def clear(self):
        self.input1 = 0
        self.input2 = 0
        self.result = 0
        print("Values have been reset to 0")

#prompt user to key in 2 numbers
input1 = float(input("Enter the first number to be calculated: "))
input2 = float(input("Enter the second number to be calculated: "))

Calculator = Calculator(input1, input2)

#perform the functions defined in the class
Calculator.adder()
Calculator.subtractor()
Calculator.multiplier()
Calculator.divider()
Calculator.clear()