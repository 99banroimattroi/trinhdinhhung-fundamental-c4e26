print("       BMI Calculator (Body Mass Index)")

height = float(input("Enter your height (cm): "))   
weight = float(input("Enter your weight (kg): "))

x = 0.01*height
BMI = weight/(x*x)

print("                   Result")

if  BMI < 16:
    print("severely underweight")
elif BMI < 18.5:
    print("underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("overweight")
else:
    print("obese")
