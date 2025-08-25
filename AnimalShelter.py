from pymongo import MongoClient
from bson.objectid import ObjectId
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self):
        USER = 'aacuser'
        PASS = '1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 33107
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            sData = self.database.animals.find(data)  # data should be dictionary            
        else:
            sData = self.database.animals.find({})
        return sData
    
#Create method to implement the U in CRUD.
    def update(self, updateD):
        if updateD is not None:
            result = self.database.animals.update_one(updateD)
        else:
            return ""
        return result
    
#Create method to implement the D in CRUD
    def delete(self, deleteD):
        if deleteD is not None:
            result = self.database.animals.delete_one(deleteD)
        else:
            return ""
        return result