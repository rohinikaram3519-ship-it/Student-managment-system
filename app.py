from flask import Flask,render_template,request,redirect
import database

app = Flask(__name__)

@app.route('/')
def index():
    students = database.view()
    return render_template('index.html',students = students)

@app.route('/add',methods=['POST'])
def add():
    name = request.form['name']
    age = request.form['age']
    course = request.form['course']
    email = request.form['email']

    database.insert(name,age,course,email)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    database.delete(id)
    return redirect('/')

app.run(debug=True)