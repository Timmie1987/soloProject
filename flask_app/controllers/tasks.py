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
        return redirect(f'/project/{request.form["project_id"]}')
    data = {
        "task": request.form["task"],
        "user_id": session["user_id"],
        "project_id": request.form["project_id"]
    }
    Task.save(data)
    return redirect(f'/project/{request.form["project_id"]}')

@app.route('/destroy/task/<int:task_id>/project/<int:project_id>')
def completetask(task_id, project_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":task_id
    }
    Task.delete(data)
    return redirect(f'/project/{project_id}')