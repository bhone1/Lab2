def main():
    display_main_menu()
    temp = get_user_input()
    print(calc_average_temperature(temp))
    print(calc_min_max_temperature(temp))
    print("Median : ")
    print(calc_median_temperature(temp))


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
    return sum(tempr_list) / len(tempr_list)

def calc_min_max_temperature(tempr_list):
    sort_temperature(tempr_list)
    min = tempr_list[0]
    max = tempr_list[-1]
    return [min, max]

def sort_temperature(list):
    list.sort()

def calc_median_temperature(list):
    list.sort()
    length = len(list)
    if length % 2 != 0:
        return list[int((length - 1) / 2)]
    else:
        #last_index = length - 1
        #median1 = list[last_index // 2]
        #median2 = list[(last_index // 2) + 1]
        median1 = list[int((length - 1) / 2)]
        median2 = (list[int((length - 1) / 2) + 1]) / 2
        return (median1 + median2) / 2

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