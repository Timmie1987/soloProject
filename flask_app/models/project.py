from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Project:
    db = 'projectmanager'
    def __init__(self, data):
        self.id = data['id']
        self.client = data['client']
        self.jobName = data['jobName']
        self.projectNumber = data['projectNumber']
        self.projectManager = data['projectManager']
        self.projectEngineer = data['projectEngineer']
        self.projectDesigner = data['projectDesigner']
        self.caddLead = data['caddLead']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM project;"
        results = connectToMySQL(cls.db).query_db(query)
        allprojects = []
        for row in results:
            allprojects.append(cls(row))
        return allprojects

    @classmethod
    def getOne(cls,data):
        query = "SELECT * FROM project WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def update(cls,data):
        query = 'UPDATE project SET client=%(client)s, jobName=%(jobName)s, projectNumber=%(projectNumber)s, projectManager=%(projectManager)s, projectEngineer=%(projectEngineer)s, projectDesigner=%(projectDesigner)s, caddLead=%(caddLead)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM project WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def save(cls,data):
        query = 'INSERT INTO project (client, jobName, projectNumber, projectManager, projectEngineer, projectDesigner, caddLead, user_id) VALUES (%(client)s, %(jobName)s, %(projectNumber)s, %(projectManager)s, %(projectEngineer)s, %(projectDesigner)s, %(caddLead)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate(project):
        isValid = True
        if len(project['client']) < 3:
            isValid = False
            flash("Client name must be at least 3 characters", "project")
        if len(project['jobName']) < 3:
            isValid = False
            flash("Job name must be at least 3 characters", "project")
        if len(project['projectNumber']) != 5:
            isValid = False
            flash("Invalid project number", "project")
        if len(project['projectManager']) < 3:
            isValid = False
            flash("Project manager must be at least 3 characters", "project")
        if len(project['projectEngineer']) < 3:
            isValid = False
            flash("Project engineer must be at least 3 characters", "project")
        if len(project['caddLead']) < 3:
            isValid = False
            flash("CADD Lead must be at least 3 characters", "project")
        return isValid


    

        