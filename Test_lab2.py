import lab2 as lab2
print("Test lab2")

def test_min_max():
    test_input = [10, 2, 38, 23, 38, 23, 21]
    assert(lab2.calc_min_max_temperature(test_input) == [2,38])

def test_calc_avg():
    test_input = [10, 2, 38, 23, 38, 23, 21]
    assert(lab2.calc_average_temperature(test_input) == 22.14)

def test_calc_median():
    test_input = [10, 2, 38, 23, 38, 23, 21]
    assert(lab2.calc_median_temperature(test_input) == 23)