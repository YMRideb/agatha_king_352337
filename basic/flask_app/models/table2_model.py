from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM table2;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        table2_list = []
        # Iterate over the db results and create instances of friends with cls.
        for row in results:
            table2_list.append(cls(row))
        return table2_list

    # @classmethod
    # def get_ninjas_in_dojo(cls, data):
    #     query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
    #     # data is a dictionary that will be passed into the save method from server.py
    #     results = connectToMySQL(DATABASE).query_db(query, data)
    #     dojo_ninja_list = []
    #     for row in results:
    #         dojo_ninja_list.append(cls(row))
    #     return dojo_ninja_list

    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas ( first_name, last_name, age, dojo_id ) VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DATABASE).query_db(query, data)

    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age= %(age)s, created_at = NOW(), updated_at = NOW() WHERE id = %(id)s;"
    #     # data is a dictionary that will be passed into the save method from server.py
    #     return connectToMySQL(DATABASE).query_db(query, data)

    # @classmethod
    # def delete(cls, data):
    #     # query = "SET SQL_SAFE_UPDATES = 0"
    #     query = "DELETE FROM ninjas WHERE id = %(id)s; "
    #     # data is a dictionary that will be passed into the save method from server.py
    #     return connectToMySQL(DATABASE).query_db(query, data)
