from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for row in results:
            dojos.append(cls(row))
        return dojos
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos;"
        # data is a dictionary that will be passed into the save method from server.py
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name) VALUES ( %(name)s);"

        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE dojos SET name= %(name)s, created_at = NOW(), updated_at = NOW() WHERE id = %(id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        # query = "SET SQL_SAFE_UPDATES = 0"
        query = "DELETE FROM dojos WHERE id = %(id)s; "
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DATABASE).query_db(query, data)
