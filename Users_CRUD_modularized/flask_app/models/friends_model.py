# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database

# can replace friend with user
class Friend:
    def __init__(self, data):
        self.id = data['id']
        self.name1 = data['name1']
        self.name2 = data['name2']
        self.email_address = data['email_address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM table_crud;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('crud_table').query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append(cls(friend))
        return friends
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM table_crud WHERE id = %(id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        results = connectToMySQL('crud_table').query_db(query, data)
        return cls(results[0])


    @classmethod
    def create(cls, data):
        query = "INSERT INTO table_crud ( name1 , name2 , email_address , created_at, updated_at ) VALUES ( %(name1)s , %(name2)s , %(email_address)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('crud_table').query_db(query, data)


    @classmethod
    def update(cls, data):
        query = "UPDATE table_crud SET name1= %(name1)s, name2 = %(name2)s, email_address = %(email_address)s, created_at = NOW(), updated_at = NOW() WHERE id = %(id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('crud_table').query_db(query, data)

    @classmethod
    def delete(cls, data):
        # query = "SET SQL_SAFE_UPDATES = 0"
        query = "DELETE FROM table_crud WHERE id = %(id)s; "
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('crud_table').query_db(query, data)
    
    
