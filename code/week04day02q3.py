class Temperature:
    temp = 0

    def __init__(self, temp):
        self.temp = temp


    def convert_to_fahrenheit(self):
        result = float((9 * self.temp) / 5 + 32)
        return result

    def convert_to_celsius(self):
        result = float((self.temp - 32) * 5 / 9)
        return result


input_temp = float(input("Input temperature in celsius: "))
temp1 = Temperature(input_temp)
print(temp1.convert_to_fahrenheit())

input_temp = float(input("Input temperature in fahrenheit: "))
temp1 = Temperature(input_temp)
print(temp1.convert_to_celsius())
