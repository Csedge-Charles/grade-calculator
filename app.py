from flask import Flask, render_template, request, url_for
import func

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def hello():
    if request.method == 'POST':

        grade1 = request.form['firstrow']
        grade2 = request.form['secondrow']
        grade3 = request.form['thirdrow']
        grade4 = request.form['fourthrow']
        grade5 = request.form['fifthrow']
        grade6 = request.form['sixthrow']
        
        weight1 = request.form['firstweight']
        weight2 = request.form['secondweight']
        weight3 = request.form['thirdweight']
        weight4 = request.form['fourthweight']
        weight5 = request.form['fifthweight']
        weight6 = request.form['sixthweight']

        if grade1 == '':
            grade1 = 0
        if grade2 == '':
            grade2 = 0
        if grade3 == '':
            grade3 = 0
        if grade4 == '':
            grade4 = 0
        if grade5 == '':
            grade5 = 0
        if grade6 == '':
            grade6 = 0
        if weight1 == '':
            weight1 = 0
        if weight2 == '':
            weight2 = 0
        if weight3 == '':
            weight3 = 0
        if weight4 == '':
            weight4 = 0
        if weight5 == '':
            weight5 = 0
        if weight6 == '':
            weight6 = 0
        
        grade1 = float(grade1)
        grade2 = float(grade2)
        grade3 = float(grade3)
        grade4 = float(grade4)
        grade5 = float(grade5)
        grade6 = float(grade6)

        weight1 = float(weight1)
        weight2 = float(weight2)
        weight3 = float(weight3)
        weight4 = float(weight4)
        weight5 = float(weight5)
        weight6 = float(weight6)


        
        final_grade = func.grade_calculator(grade1, weight1, grade2, weight2, grade3, weight3, grade4, weight4, grade5, weight5, grade6, weight6, 0, 0)
        laughing = False
        letter = ''
        if final_grade == 100:
            letter = 'A+'
        if final_grade >= 93 and final_grade < 100:
            letter = 'A'
        
        if final_grade >= 90 and final_grade < 93:
            letter = 'A-'
        if final_grade >= 87 and final_grade < 90:
            letter = 'B+'
        if final_grade >= 83 and final_grade < 87:
            letter = 'B'
        if final_grade >= 80 and final_grade < 83:
            letter = 'B-'
            
        if final_grade >= 77 and final_grade < 80:
            letter = 'C+'
        if final_grade >= 73 and final_grade < 77:
            letter = 'C'
        if final_grade >= 70 and final_grade < 73:
            letter = 'C-'

        if final_grade >= 67 and final_grade < 70:
            letter = 'D+'
        if final_grade >= 63 and final_grade < 67:
            letter = 'D'
        if final_grade >= 60 and final_grade < 63:
            letter = 'D-'
            
        if final_grade < 60:
            letter = 'F'
        
        if final_grade < 80:
            laughing = True
            
        
    
        
        return render_template('index.html', result=str(final_grade) + '%', letter=letter, laugh=laughing)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=82, debug=True)