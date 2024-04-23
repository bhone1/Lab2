def calculate_bmi(weight, height):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height**2)
    print(f"BMI : {bmi}")
    if bmi < 18.5:
        print("Under Weight")
    elif bmi >= 18.5 and bmi <= 25.0:
        print("Normal Weight")
    else:
        print("Over Weight")

calculate_bmi(57, 1.73)