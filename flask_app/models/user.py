from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import project
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = 'projectmanager'
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.company = data['company']
        self.email = data['email']
        self.password = data['password']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.project = None

        def fullName(self):
            return f'{self.firstName} {self.lastName}'

        @staticmethod
        def validate(user):
            isValid = True
            query = 'SELECT * FROM user WHERE email = %(email)s;'
            results = connectToMySQL(User.db).query_db(query, user)
            if len(results) >= 1:
                isValid = False
                flash("That email is already taken")
            if not EMAIL_REGEX.match(user['email']):
                isValid = False
                flash("Invalid email")
            if len(user['firstName']) < 3:
                isValid = False
                flash("First name must be more than 3 characters")
            if len(user['lastName']) < 3:
                isValid = False
                flash("Last name must be more than 3 characters")
            if len(user['password']) < 8:
                isValid = False
                flash("Password must be more than 8 characters")
            if user['password'] != user['confirm']:
                isValid = False
                flash('Passwords do not match')
            return isValid

        @classmethod
        def getAll(cls):
            query = 'SELECT * FROM user;'
            results = connectToMySQL(cls.db).query_db(query)
            user = []
            for row in results:
                user.append(cls(row))
            return user

        @classmethod
        def getOne(cls,data):
            query = "SELECT * FROM user WHERE id = %(id)s;"
            results = connectToMySQL(cls.db).query_db(query, data)
            if len(results) < 1:
                return False
            return cls(results[0])

        @classmethod
        def getEmail(cls,data):
            query = "SELECT * FROM user WHERE email = %(email)s;"
            results = connectToMySQL(cls.db).query_db(query, data)
            if len(results) < 1:
                return False
            return cls(results[0])

        @classmethod
        def save(cls,data):
            query = 'INSERT INTO user (firstName, lastName, company, email, password) VALUES (%(firstName)s, %(lastName)s, %(company)s, %(email)s, %(password)s);'
            return = connectToMySQL(cls.db).query_db(query, data)


