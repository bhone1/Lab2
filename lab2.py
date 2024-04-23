def main():
    calculate_bmi(1,1)


def display_main_menu():
    print("Enter some numbers separated by commas(e.g. 5, 67, 32)")

def get_user_input():
    user_input = input()
    #split the string into a list
    user_input_list = user_input.split(",")
    for i in range(len(user_input_list)):
        user_input_list[i] = float(user_input_list[i])
    return user_input_list




def calc_average_temperature(tempr_list):
    for x in tempr_list:
        total += x
    return total / len(tempr_list)

def calc_min_max_temperature(tempr_list):
    sort_temperature()
    min = tempr_list[0]
    max = tempr_list[-1]
    return [min, max]

def sort_temperature(list):
    list.sort()

def calc_median_temperature(list):
    return 1

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





if __name__ == "__main__":
    main()