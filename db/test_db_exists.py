import pymongo

db_name = 'demographics'
test_client = pymongo.MongoClient('mongodb://localhost:27017/')
test_db = test_client[db_name]

col_name = 'coach'
test_col = test_db['col_name']

test_dict = { "surname": "Adamyan", "address": "Meliq Adamyan 1",
             "city": "Yerevan" }

pl = test_col.insert_one(test_dict)

print(pl.inserted_id)