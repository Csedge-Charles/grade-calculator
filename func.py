def two_decimal_places(x):
    return (round(x * 100))/100



def grade_calculator(grade_1, weight_1, grade_2, weight_2, grade_3, weight_3, grade_4, weight_4, grade_5, weight_5, grade_6, weight_6, grade_7, weight_7):
    return two_decimal_places(((weight_1 * grade_1) + (weight_2 * grade_2) + (weight_3 * grade_3) + (weight_4 * grade_4)  + (weight_5 * grade_5) + (weight_6 * grade_6) + (weight_7 * grade_7)) / (weight_1 + weight_2 + weight_3 + weight_4 + weight_5 + weight_6 + weight_7))


def gpa(grade1, grade2, grade3, grade4, grade5, grade6, grade7, grade8, grade9, grade10):
    grade_list = [grade1, grade2, grade3, grade4, grade5, grade6, grade7, grade8, grade9, grade10]
    overall = 0
    amount = 0
    for i in grade_list:
        if i == 'A' or i == 'A+':
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
        

def weighted(gradelist, weightlist):
    amount = 0
    overall = 0
    for i in range(len(gradelist)):
        if 'P' in weightlist[i]:
            overall += 1
        if weightlist[i] == 'Honors':
            overall += 0.5
        
        i = gradelist[i]
        
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

def string(main):
    #turns list into string
    final = ''
    for i in main:
        final += i
    return final

def checker(email):
    email = list(email)
    if '@' in email:
        
        if email[0] != '@' and email[-5] != '@':
        
            if email[-4] == '.' and email[-3] == 'o' and email[-2] == 'r' and email[-1] == 'g':
                return True
            if email[-4] == '.' and email[-3] == 'c' and email[-2] == 'o' and email[-1] == 'm':
                return True
            if email[-4] == '.' and email[-3] == 'g' and email[-2] == 'o' and email[-1] == 'v':
                return True
            if email[-4] == '.' and email[-3] == 'n' and email[-2] == 'e' and email[-1] == 't':
                return True
            if email[-4] == '.' and email[-3] == 'e' and email[-2] == 'd' and email[-1] == 'u':
                return True
            
    return False


            

