from pymongo import MongoClient


client = MongoClient(host="localhost", port=27018, username="root", password="example")

db = client.tutorial

print(db.name)
print(db.users)
for user in db.users.find():
    print(user)

res = db.users.insert_one({"username": "vpalex999"})
print(str(res.inserted_id))
