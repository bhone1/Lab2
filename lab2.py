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
    user_input_list = [float(x) for x in user_input_list]
    return user_input_list


def calc_average_temperature(tempr_list):
    return sum(tempr_list) / len(tempr_list)

def calc_min_max_temperature(tempr_list):
    tempr_list = sort_temperature(tempr_list)
    min = tempr_list[0]
    max = tempr_list[-1]
    return [min, max]

def sort_temperature(list):
    list.sort()
    return list

def calc_median_temperature(list):
    list.sort()
    length = len(list)
    if length % 2 != 0:
        return list[int((length - 1) / 2)]
    else:
        #last_index = length - 1
        #median1 = list[last_index // 2]
        #median2 = list[(last_index // 2) + 1]
        median1 = list[int(length / 2) - 1]
        median2 = list[int(length / 2)]
        return (median1 + median2) / 2




if __name__ == "__main__":
    main()