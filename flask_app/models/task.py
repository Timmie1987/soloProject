from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Task:
    db = 'projectmanager'
    def __init__(self, data):
        self.id = data['id']
        self.task = data['task']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']
        self.project_id = data['project_id']


    @classmethod
    def getAllByProject(cls, data):
        query = 'SELECT * FROM tasks WHERE project_id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
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
        query = 'INSERT INTO tasks (task, user_id, project_id) VALUES (%(task)s, %(user_id)s, %(project_id)s);'
        return  connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_task(tasks):
        isValid = True
        if len(tasks['task']) < 3:
            isValid = False
            flash("Task must be more than 3 characters", "tasks")
        return isValid