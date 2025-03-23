from datetime import datetime
from werkzeug.security import generate_password_hash
from src import StartUp as mongo

class User:
    @staticmethod
    def create(email, password):
        return mongo.db.users.insert_one({
            'email': email,
            'password': generate_password_hash(password),
            'created_at': datetime.now()
        })

    @staticmethod
    def find_by_email(email):
        return mongo.db.users.find_one({'email': email})

    @staticmethod
    def find_by_id(_id):
        return mongo.db.users.find_one({'_id': _id})

    @staticmethod
    def delete_by_id(_id):
        return mongo.db.users.delete_one({'_id': _id})