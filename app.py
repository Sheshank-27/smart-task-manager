from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():

    task_name = request.form['task']
    priority = request.form['priority']

    task = {
        "name": task_name,
        "priority": priority,
        "status": "Pending"
    }

    tasks.append(task)

    return redirect('/')

@app.route('/complete/<int:index>')
def complete_task(index):

    tasks[index]["status"] = "Completed"

    return redirect('/')

@app.route('/delete/<int:index>')
def delete_task(index):

    tasks.pop(index)

    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)