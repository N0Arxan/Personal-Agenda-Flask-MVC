from datetime import datetime, timedelta

import pymongo

from src import StartUp as mongo

class Event:
    @staticmethod
    def create(user_id, title,detail, event_date):
        return mongo.db.events.insert_one({
            'user_id': user_id,
            'title': title,
            'detail': detail,
            'is_done': False,
            'event_date': event_date,
            'created_at': datetime.now()
        })


    @staticmethod
    def find_by_user_id(user_id):
        return mongo.db.events.find({'user_id': user_id}).sort([
            ("is_done", pymongo.ASCENDING),
            ("event_date", pymongo.ASCENDING)
        ])

    @staticmethod
    def delete_by_user_id_and_id(user_id, event_id):
        return mongo.db.events.delete_one({'user_id': user_id, '_id': event_id})


    @staticmethod
    def complete_event(user_id, event_id):
        return mongo.db.events.update_one({'user_id': user_id, '_id': event_id}, {'$set': {'is_done':True}})


    '''
    function not implemented todo stuff in the future
    '''
    @staticmethod
    def get_tomorrows_events():
        tomorrow = datetime.now() + timedelta(days=1)
        return mongo.db.events.find({
            'event_date': {
                '$gte': tomorrow.replace(hour=0, minute=0, second=0),
                '$lt': tomorrow.replace(hour=23, minute=59, second=59)
            },
            'reminder_sent': False
        })