
"""
#REMINDERS
1. The data coming from the database is in a dictionary format and turned into an object instance (model) we access throughout the application.

#TO-DO:
1. Update the initialization attributes to fit data coming from the server.
2. Build out new queries and update the data in the template ones.
"""

from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self ,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = data['dojo_id']

    @classmethod
    def get_all(cls):
        query = "SELECT ninjas.id, first_name, last_name, age, ninjas.created_at, ninjas.updated_at, dojo_id FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        data = []
        for ninja in results:
            data.append(cls(ninja))
        return data

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at) VALUES (%(first_name)s , %(last_name)s , %(age)s , NOW() , NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, updated_at = NOW() WHERE id = %(id)s;"
        print(query)
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)