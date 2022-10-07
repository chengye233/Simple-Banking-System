class Tax:
    def __init__(self, income):
        self.income = income
        percent = 0
        calculated_tax = 0
        if 15528 <= self.income <= 42707:
            percent = 15
            calculated_tax = round(self.income * 0.15)
        elif 42708 <= self.income <= 132406:
            percent = 25
            calculated_tax = round(self.income * 0.25)
        elif 132407 <= self.income:
            percent = 28
            calculated_tax = round(self.income * 0.28)
        self.percent = percent
        self.calculated_tax = calculated_tax

    def output_tax(self):
        print(f'The tax for {self.income} is {self.percent}%. That is {self.calculated_tax} dollars!')


# tax = Tax(int(input()))
# tax.output_tax()

print(":.4f".format(3.14159265358979))
print("{1} {1} {1}".format(1, 2, 3))
# print("{1} is a {kind}".format(kind="fruit", "grapefruit"))
print("{city} is the capital of {country}".format(country="Portugal",
                                                  city="Lisbon"))


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self, count):
        return "woof " * count

    def greet(person, self):
        print("wags tail")

    def play():
        print("throw a stick!")

    def sleep(self):
        print("zzz")
