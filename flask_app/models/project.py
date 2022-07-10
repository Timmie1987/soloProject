from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Project:
    db = 'projectmanager'
    def __init__(self, data):
        self.id = data['id']
        self.client = data['firstName']
        self.projectNumber = data['lastName']
        self.projectManager = data['company']
        self.projectEngineer = data['email']
        self.projectDesigner = data['password']
        self.caddLead = data['caddLead']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']

    @staticmethod
        def validate(project):
            isValid = True
            if len(project['client']) < 3:
                isValid = False
                flash("Client name must be at least 3 characters")
            if len(project['jobName']) < 3:
                isValid = False
                flash("Job name must be at least 3 characters")
            if len(project['projectNumber']) != 5:
                isValid = False
                flash("Invalid project number")
            if len(project['projectManager']) < 3:
                isValid = False
                flash("Project manager must be at least 3 characters")
            if len(project['projectEngineer']) < 3:
                isValid = False
                flash("Project engineer must be at least 3 characters")
            if len(project['caddLead']) < 3:
                isValid = False
                flash("CADD Lead must be at least 3 characters")
            return isValid

    @classmethod
        def getAll(cls):
            query = 'SELECT * FROM project;'
            results = connectToMySQL(cls.db).query_db(query)
            project = []
            for row in results:
                project.append(cls(row))
            return project

    @classmethod
        def getOne(cls,data):
            query = "SELECT * FROM project WHERE id = %(id)s;"
            results = connectToMySQL(cls.db).query_db(query, data)
            if len(results) < 1:
                return False
            return cls(results[0])

    @classmethod
        def update(cls,data):
            query = 'UPDATE project SET client=%(client)s, jobName=%(jobName)s, projectNumber=%(projectNumber)s, projectManager=%(projectManager)s, projectEngineer=%(projectEngineer)s, projectDesigner=%(projectDesigner)s, caddLead=%(caddLead)s;'
            return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
        def delete(cls, data):
            query = 'DELETE FROM project WHERE id = %(id)s;'
            return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
        def save(cls,data):
            query = 'INSERT INTO project (client, jobName, projectNumber, projectManager, projectEngineer, projectDesigner, caddLead) VALUES (%(client)s, %(jobName)s, %(projectNumber)s, %(projectManager)s, %(projectEngineer)s, %(projectDesigner)s, %(caddLead)s);'
            return = connectToMySQL(cls.db).query_db(query, data)

    @classmethod
        def projectUser(cls, data):
            query = 'SELECT * FROM project LEFT JOIN user on project.user_id = user.id WHERE project.id = %(id)s;'
            results = connectToMySQL(cls.db).query_db(query, data)
            for row in results:
                project = cls(row)
                userData = {
                    'id': row['user.id'],
                    'firstName': row['firstName'],
                    'lastName': row['lastName'],
                    'company': row['company'],
                    'email': row['email'],
                    'password': row['password'],
                    'createdAt': row['user.createdAt'],
                    'updatedAt': row['user.updatedAt']
                }
                project.user = user.User(userData)
            return project
    

        