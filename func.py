def two_decimal_places(x):
    return (round(x * 100))/100



def grade_calculator(grade_1, weight_1, grade_2, weight_2, grade_3, weight_3, grade_4, weight_4, grade_5, weight_5, grade_6, weight_6, grade_7, weight_7):
    return two_decimal_places(((weight_1 * grade_1) + (weight_2 * grade_2) + (weight_3 * grade_3) + (weight_4 * grade_4)  + (weight_5 * grade_5) + (weight_6 * grade_6) + (weight_7 * grade_7)) / (weight_1 + weight_2 + weight_3 + weight_4 + weight_5 + weight_6 + weight_7))


def gpa(grade1, grade2, grade3, grade4, grade5, grade6, grade7, grade8, grade9, grade10):
    grade_list = [grade1, grade2, grade3, grade4, grade5, grade6, grade7, grade8, grade9, grade10]
    overall = 0
    amount = 0
    for i in grade_list:
        if i == 'A':
            amount += 1
            overall += 4.0
        if i == 'A-':
            amount += 1
            overall += 3.7
        if i == 'B+':
            amount += 1
            overall += 3.3
        if i == 'B':
            amount += 1
            overall += 3.0
        if i == 'B-':
            amount += 1
            overall += 2.7
        if i == 'C+':
            amount += 1
            overall += 2.3
        if i == 'C':
            amount += 1
            overall += 2.0
        if i == 'C-':
            amount += 1
            overall += 1.7
        if i == 'D+':
            amount += 1
            overall += 1.0
        if i == 'D':
            amount += 1
            overall += 1.0
        if i == 'D-' or i == 'F':
            amount += 1
            overall += 0
    return two_decimal_places(overall/amount)
        
        
        
