#PYTHON BMI CALCULATOR
height = int(input("input your height in Meters: "))
weight = int(input("input your weight in Kilograms: "))

bmi = round((weight/height ** 2))

if bmi < 18.5:
    print(f"your bmi is {bmi}, you are underweight")
elif bmi < 25:
    print(f"your bmi is {bmi}, you are normal weight")
elif bmi < 30:
    print(f"your bmi is {bmi}, you are normal overweight")
elif bmi < 35:
    print(f"your bmi is {bmi}, you are normal obese")
else:
    print(f"your bmi is {bmi}, you are clinically normal obese")
