from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
class Dog:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.age = data['age']
        self.breed = data['breed']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.owner_id = data['owner_id']
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dogs;'
        results = connectToMySQL(DATABASE).query_db(query)
        all_dogs = [] 
        # checks if the query performed returned any results
        if results:
            # iterate through results (the list of dictionaries)
            for row in results:
                dog = cls(row)
                all_dogs.append(dog) 
        return all_dogs
    
    @classmethod
    def get_one(cls, data):
        print("DATA = ", data)
        query = """
        SELECT * FROM dogs
        WHERE id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            dog = cls(results[0])
            return dog
        return False


    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO dogs (name, age, breed) 
        VALUES (%(name)s, %(age)s, %(breed)s);
        """
        new_dog_id = connectToMySQL(DATABASE).query_db(query, data)
        return new_dog_id

    @classmethod
    def update(cls, data):
        query ="""
        UPDATE dogs
        SET name = %(name)s, age = %(age)s, breed = %(breed)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)