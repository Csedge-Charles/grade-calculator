def two_decimal_places(x):
    return (round(x * 100))/100



def grade_calculator(grade_1, weight_1, grade_2, weight_2, grade_3, weight_3, grade_4, weight_4, grade_5, weight_5, grade_6, weight_6, grade_7, weight_7):
    return two_decimal_places(((weight_1 * grade_1) + (weight_2 * grade_2) + (weight_3 * grade_3) + (weight_4 * grade_4)  + (weight_5 * grade_5) + (weight_6 * grade_6) + (weight_7 * grade_7)) / (weight_1 + weight_2 + weight_3 + weight_4 + weight_5 + weight_6 + weight_7))


