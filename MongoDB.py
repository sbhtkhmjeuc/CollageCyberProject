import pymongo
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://sbhtkhmjeuc:***@cluster0.a52tjwe.mongodb.net/?retryWrites=true&w=majority")

db = client.CollageCyberProject
collection = db.CMDCommmands
document = {
    "commnd": "whoami"
}
result = collection.insert_one(document)
print("Inserted document ID:", result.inserted_id)

collectionDNS = db.DNSRequests
documentDNS = {
    "request": "https://google.com"
}
resultDNS = collectionDNS.insert_one(documentDNS)
print("Inserted document ID:", resultDNS.inserted_id)
