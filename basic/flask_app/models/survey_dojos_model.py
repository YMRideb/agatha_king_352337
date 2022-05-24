from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


class DOJO:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM survey_dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        sd_table1 = []
        # Iterate over the db results and create instances of friends with cls.
        for row in results:
            sd_table1.append(cls(row))
        return sd_table1

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM survey_dojos;"
        # data is a dictionary that will be passed into the save method from server.py
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])

    @classmethod
    def create(cls, data):
        query = "INSERT INTO survey_dojos (name, location, language, comments) VALUES ( %(name)s, %(location)s, %(language)s, %(comments)s);"

        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE survey_dojos SET name= %(name)s, location = %(location)s, language = %(language)s, comments = %(comments)s, WHERE id = %(id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        # query = "SET SQL_SAFE_UPDATES = 0"
        query = "DELETE FROM survey_dojos WHERE id = %(id)s; "
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DATABASE).query_db(query, data)
