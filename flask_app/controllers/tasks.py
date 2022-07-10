from flask import redirect,session,request
from flask_app import app
from flask_app.models.project import Project
from flask_app.models.user import User
from flask_app.models.task import Task

@app.route('/create/task',methods=['POST'])
def createtask():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Task.validate(request.form):
        return redirect('/project/<int:id>')
    data = {
        "task": request.form["task"],
        "user_id": session["user_id"]
    }
    Task.save(data)
    return redirect('/project/<int:id>')

@app.route('/destroy/task/<int:id>')
def completetask(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Task.destroy(data)
    return redirect('/project/<int:id>')