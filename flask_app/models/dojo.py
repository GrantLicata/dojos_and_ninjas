
"""
#REMINDERS
1. The data coming from the database is in a dictionary format and turned into an object instance (model) we access throughout the application.

#TO-DO:
1. Update the initialization attributes to fit data coming from the server.
2. Build out new queries and update the data in the template ones.
"""

from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self ,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        data = []
        for dojo in results:
            data.append( cls(dojo) )
        return data

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW() , NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)