from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from flask_app.models import project

class Task:
    db = 'projectmanager'
    def __init__(self, data):
        self.id = data['id']
        self.task = data['task']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']
        self.project_id = data['project_id']

    @staticmethod
        def validate(tasks):
            isValid = True
            if len(tasks['task']) < 3:
                isValid = False
                flash("Task must be more than 3 characters")
            return isValid

    @classmethod
        def getAll(cls):
            query = 'SELECT * FROM tasks;'
            results = connectToMySQL(cls.db).query_db(query)
            tasks = []
            for row in results:
                tasks.append(cls(row))
            return tasks

    @classmethod
        def update(cls,data):
            query = 'UPDATE tasks SET task=%(task)s;'
            return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
        def delete(cls, data):
            query = 'DELETE FROM tasks WHERE id = %(id)s;'
            return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
        def save(cls,data):
            query = 'INSERT INTO tasks (task) VALUES (%(task)s);'
            return = connectToMySQL(cls.db).query_db(query, data)
