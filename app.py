from flask import Flask, render_template, request, url_for
import func

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def hello():
    if request.method == 'POST':
        grade1 = float(request.form['firstrow'])
        grade2 = float(request.form['secondrow'])
        grade3 = float(request.form['thirdrow'])
        grade4 = float(request.form['fourthrow'])
        grade5 = float(request.form['fifthrow'])
        grade6 = float(request.form['sixthrow'])
        
        weight1 = float(request.form['firstweight'])
        weight2 = float(request.form['secondweight'])
        weight3 = float(request.form['thirdweight'])
        weight4 = float(request.form['fourthweight'])
        weight5 = float(request.form['fifthweight'])
        weight6 = float(request.form['sixthweight'])
        
        final_grade = func.grade_calculator(grade1, weight1, grade2, weight2, grade3, weight3, grade4, weight4, grade5, weight5, grade6, weight6, 0, 0)
        
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
            
        
    
        
        return render_template('index.html', result=str(final_grade) + '%', letter=letter)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)