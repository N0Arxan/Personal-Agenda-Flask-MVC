"""
run this code to have a sample data on application
"""


from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta , date ,time
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client[Config.DATABASE]

users = [
    {"email": "user1@example.com", "password": generate_password_hash("password1"), "created_at": datetime.now()},
    {"email": "user2@example.com", "password": generate_password_hash("password2"), "created_at": datetime.now()},
    {"email": "user3@example.com", "password": generate_password_hash("password3"), "created_at": datetime.now()}
]

user_ids = db.users.insert_many(users).inserted_ids
print(user_ids)

events = []
for user_id in user_ids:
    for i in range(0, 8):
        events.append({
            "user_id": user_id,
            "title": f"Event {i}",
            "detail": f"Detail for event {i}",
            "is_done": False,
            "event_date": datetime.combine(date.today() + timedelta(days=i), time.min),
            "created_at": datetime.now()
        })

db.events.insert_many(events)

client.close()

print("Inserted 3 users and 30 events successfully!")

