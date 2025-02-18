from flask import Flask, render_template, request, url_for, redirect
import func

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def homepage():
    if request.method == 'POST':
        if request.form['gradegpa'] == 'Sign In':
            return redirect('/email', code=302)       
        if request.form['gradegpa'] == 'Grade Calculator':
            return redirect('/Grade-Calculator', code=302)
        if request.form['gradegpa'] == 'GPA Calculator':
            return redirect('/gpa', code=302)

    return render_template('index.html', sign=True)



@app.route('/Grade-Calculator', methods=['POST', 'GET'])

def hello():
    if request.method == 'POST':
        if request.form['submit'] == 'Back':
            return redirect('/home', code=302)
        if request.form['submit'] == 'GPA Calculator':
            return redirect('/gpa', code=302)
        if request.form['submit'] == 'Grade Calculator':
            return render_template('gradecalc.html')
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
        
        value1 = grade1
        value2 = weight1
        value3 = grade2
        value4 = weight2
        value5 = grade3
        value6 = weight3
        value7 = grade4
        value8 = weight4
        value9 = grade5
        value10 = weight5
        value11 = grade6
        value12 = weight6

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
            
        
    
        
        return render_template('gradecalc.html', result=str(final_grade) + '%', letter=letter, laugh=laughing,
                               value1=value1, value2=value2, value3=value3, value4=value4, value5=value5,
                               value6=value6, value7=value7, value8=value8, value9=value9, value10=value10, value11=value11,
                               value12=value12)
    return render_template('gradecalc.html')

@app.route('/gpa', methods=['POST', 'GET'])
def gpa():

    if request.method == 'POST':
        if request.form['submit'] == 'Back':
            return redirect('/home', code=302)
        if request.form['submit'] == 'Grade Calculator':
            return redirect('/Grade-Calculator', code=302)
        if request.form['submit'] == 'GPA Calculator':
            return render_template('gpa.html')
        grade1 = str(request.form['firstrow'])
        value1 = grade1
        grade2 = str(request.form['secondrow'])
        value2 = grade2
        grade3 = str(request.form['thirdrow'])
        value3 = grade3
        grade4 = str(request.form['fourthrow'])
        value4 = grade4
        grade5 = str(request.form['fifthrow'])
        value5 = grade5
        grade6 = str(request.form['sixthrow'])
        value6 = grade6
        grade7 = str(request.form['seventhrow'])
        value7 = grade7
        grade8 = str(request.form['eighthrow'])
        value8 = grade8
        grade9 = str(request.form['ninethrow'])
        value9 = grade9
        grade10 = str(request.form['tenthrow'])
        value10 = grade10
        
        
        weight1 = str(request.form['weight1'])
        weight2 = str(request.form['weight2'])
        weight3 = str(request.form['weight3'])
        weight4 = str(request.form['weight4'])
        weight5 = str(request.form['weight5'])
        weight6 = str(request.form['weight6'])
        weight7 = str(request.form['weight7'])
        weight8 = str(request.form['weight8'])
        weight9 = str(request.form['weight9'])
        weight10 = str(request.form['weight10'])
        
        weight_list = [weight1, weight2, weight3, weight4, weight5,
                       weight6, weight7, weight8, weight9, weight10]
        
        grade_list = [grade1, grade2, grade3, grade4, grade5,
                      grade6, grade7, grade8, grade9, grade10]
        weighted_gpa = func.weighted(grade_list, weight_list)
        
        laugh = False
        final = func.gpa(grade1, grade2, grade3, grade4, grade5, grade6, grade7, grade8, grade9, grade10)
        if final < 3.5:
            laugh = True
        return render_template('gpa.html', gpa=str(final), laugh=laugh,
                        value1=value1, value2=value2, value3=value3, value4=value4, value5=value5, value6=value6,
                         value7=value7, value8=value8, value9=value9, value10=value10, weighted=weighted_gpa)
    else:
        return render_template('gpa.html')
    
    

@app.route('/email', methods=['POST', 'GET'])

def email():
    if request.method == 'POST':
        autofill = ''
        if request.form['email'] == 'admin@gradepro.org':
            return redirect('/password', code=302)
        if request.form['submit'] == 'Create account':
            return redirect('/create-account', code=302)
        return render_template('email.html', reject='Email does not exist', email=request.form['email'])
    
    return render_template('email.html', reject='')

@app.route('/create-account', methods=['GET', 'POST'])


def create():
    if request.method == 'POST':
        global username
        global email
        global password
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if func.checker(email):
            return redirect('/email-success', code=302)
        else:
            return render_template('create.html', wrong='Invalid email address', email=email, password=password, username=username)
    return render_template('create.html', wrong='')



@app.route('/email-success', methods=['POST', 'GET'])

def success():
    if request.method == 'POST':
        if request.form['submit'] == 'Create account':
            return redirect('/create-account', code=302)
        if request.form['email'] == email:
            return redirect('/password', code=302)
        return render_template('email.html', reject='Email does not exist', email=request.form['email'])
    return render_template('email.html', reject='')
        
    

@app.route('/password', methods=['POST', 'GET'])

def password():
    if request.method == 'POST':
        if request.form['password'] == 'htmlcssflask':
            global username
            username = 'Admin'
            return redirect('/home', code=302)
        if request.form['password'] == password:
            return redirect('/home', code=302)
        else:
            return render_template('password.html', wrong='Password incorrect', reset=request.form['password'])
    return render_template('password.html', wrong='')

@app.route('/home', methods=['POST', 'GET'])

def home():
    if request.method == 'POST':
        if request.form['gradegpa'] == 'Grade Calculator':
            return redirect('/Grade-Calculator', code=302)
        if request.form['gradegpa'] == 'GPA Calculator':
            return redirect('/gpa', code=302)
        if request.form['gradegpa'] == 'Sign out':
            return redirect('/email', code=302)
    return render_template('index.html', sign=False, user=username)






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=82, debug=True)