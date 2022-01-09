#PYTHON BMI CALCULATOR
height = input("input your height in Meters: ")
weight = input("input your wieght in Kilograms: ")

BMI = int(weight) / float(height) ** 2

print(BMI)

bmi_as_int = int(BMI)
print(bmi_as_int)
