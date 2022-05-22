# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database


class User:
    def __init__(self, data):
        self.id = data['id']
        self.name1 = data['name1']
        self.name1 = data['name2']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM table_crud;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('crud_table').query_db(query)
        # Create an empty list to append our instances of friends
        users_tbl = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            users_tbl.append(cls(user1))
        return users_tbl

    @classmethod
    def save(cls, data):
        query = "INSERT INTO table_crud ( name1 , name1 , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('crud_table').query_db(query, data)
