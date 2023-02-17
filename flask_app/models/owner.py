from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
class Owner:
    def __init__(self, data):
        self.id = data['id']
        # add other columns from this table
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
        @classmethod
        def get_all(cls):
            query = 'SELECT * FROM owners;'
            results = connectToMySQL(DATABASE).query_db(query)
            all_owners = [] 
            # checks if the query performed returned any results
            if results:
                # iterate through results (the list of dictionaries)
                for row in results:
                    owner = cls(row)
                    all_owners.append(owner) 
            return all_owners