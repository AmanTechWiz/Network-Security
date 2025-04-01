from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://amantechwiz:iU4pJ5jiWpdBLNVW@cluster0.4axg2gb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)