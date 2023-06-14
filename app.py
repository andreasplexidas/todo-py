from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson import ObjectId

# Σύνδεση στη MongoDB
client = MongoClient("mongodb://mongodb:27017")
db = client.todo_app
tasks = db.tasks

app = Flask(__name__)

@app.route('/')
def index():
    # Ανάκτηση όλων των εργασιών από τη βάση δεδομένων
    todos = tasks.find()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_task():
    # Λήψη του νέου task από τη φόρμα
    task_description = request.form.get('task_description')
    
    # Προσθήκη του task στη βάση δεδομένων
    task_id = tasks.insert_one({'description': task_description}).inserted_id
    
    return redirect('/')

@app.route('/delete/<string:task_id>')
def delete_task(task_id):
    # Διαγραφή του task με βάση το ID
    tasks.delete_one({'_id': ObjectId(task_id)})
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
