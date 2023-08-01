#Exercise 4
weight=float(input("Enter your weight in(kg): "))
height=float(input("Enter your height in(m): "))
bmi=weight/(height**2)
print("Your BMI is:",round(bmi,2))
if bmi < 18.5:
    print('You are in the "Underweight" range')
elif 18.5 <= bmi <= 24.9:
    print('You are in the "Normal" range')
elif 25<=bmi<= 29.9:
    print('You are in the "Overweight" range')
else:
    print('You are in the "Obese" range')
