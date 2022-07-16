from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.project import Project
from flask_app.models.user import User
from flask_app.models.task import Task

@app.route('/new/project')
def newproject():
    if 'user_id' not in session:
        return redirect('/logout')
    user_data = {
        "id":session['user_id']
    }
    return render_template("newproject.html",user=User.getOne(user_data))

@app.route('/create/project',methods=['POST'])
def createproject():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Project.validate(request.form):
        return redirect('/new/project')
    data = {
        "client": request.form["client"],
        "jobName": request.form["jobName"],
        "projectNumber": request.form["projectNumber"],
        "projectManager": request.form["projectManager"],
        "projectEngineer": request.form["projectEngineer"],
        "projectDesigner": request.form["projectDesigner"],
        "caddLead": request.form["caddLead"],
        "user_id": session["user_id"]
    }
    Project.save(data)
    return redirect('/dashboard')

@app.route('/edit/project/<int:id>')
def editproject(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    print(Project.getOne(data).jobName)
    return render_template("editproject.html",edit=Project.getOne(data),user=User.getOne(user_data))

@app.route('/update/project',methods=['POST'])
def updateproject():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Project.validate(request.form):
        return redirect('/dashboard')
    data = {
        "client": request.form["client"],
        "jobName": request.form["jobName"],
        "projectNumber": request.form["projectNumber"],
        "projectManager": request.form["projectManager"],
        "projectEngineer": request.form["projectEngineer"],
        "projectDesigner": request.form["projectDesigner"],
        "caddLead": request.form["caddLead"],
        "id": request.form['id']
    }
    Project.update(data)
    return redirect('/dashboard')

@app.route('/project/<int:id>')
def showproject(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("showproject.html",project=Project.getOne(data),user=User.getOne(user_data),tasks=Task.getAllByProject(data))

@app.route('/destroy/project/<int:id>')
def completeproject(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Project.delete(data)
    return redirect('/dashboard')