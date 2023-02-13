import pymongo

# Players should have attributes for location AND
# Locations should have a list of entities in them (including Players at the current location)

# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Get the database and create it if it doesn't exist
db = client["den_quest"]
if "den_quest" not in client.list_database_names():
    db = client["den_quest"]


# Get the player collection and create it if it doesn't exist
player_collection = db["players"]
# Collection requires one record to be inserted to be created... How vexing
player_collection.create_index([("playerID", pymongo.ASCENDING)], unique=True)
# playerID must be unique
player = {
    "playerID": "9956",
    "name": "Jerry",
    "title": "mouse",
    "location": [0, 0, 0],
    "experience": 0
}
existing_player = player_collection.find_one({"name": "Jerry"})
if not existing_player:
    result = player_collection.insert_one(player)
    print("Inserted player: ", result)
else:
    print("Player already exists");

# Get the location collection and create it if it doesn't exist

location_collection = db["locations"]
location_collection.create_index([("coordinates", pymongo.ASCENDING)], unique=True)
location = {
    "coordinates": [0, 0, 0],
    "description": "",
    "entities": [9956, ]
}

existing_location = location_collection.find_one({"coordinates": [0, 0, 0]})
if not existing_location:
    result = location_collection.insert_one(location)
else:
    print("Location already exists");

# Query the players collection
players = player_collection.find()
for player in players:
    print("Player: ", player)

# Query the locations collection

locations = location_collection.find()
for location in locations:
    print("Location: ", location)
