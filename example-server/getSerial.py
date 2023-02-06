# Read the serial port data from the COM3 
import serial 
import csv
import time 

from pymongo import MongoClient
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb://localhost:27017"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
   if client is not None:
      print("Connected successfully!!!")
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['telemetry']
  
# This is added so that many files can reuse the function get_database()

   # Get the database
dbname = get_database()

# Create the collection name
collection_name = "telemetry_kt1accx"
    # Create a collection in the database
collection = dbname[collection_name]
    # Create a dictionary
data = {}
    # Create a list
data_list = []
    # Read the serial port data from the COM3
ser = serial.Serial('COM7', 921600)

schemas = {
    "timestamp": "",
    "K1 AccX": "",
    "K1 AccY": "",
    "K1 AccZ": "",
    "K1 MagX": "",
    "K1 MagY": "",
    "K1 MagZ": "",
    "K2 AccX": "",
    "K2 AccY": "",
    "K2 AccZ": "",
    "K2 MagX": "",
    "K2 MagY": "",
    "K2 MagZ": "",
    "WG1 StrainGauge": "",
    "ADC1": "",
    "ADC2": "",
    "ADC3": "",
    "ADC4": "",
}

while True:
    data = ser.readline()
    data = str(data)
    # Remove b' and \r \n from the data
    data = data.replace("b'", "")
    data = data.replace("\\r\\n'", "")
    #print(data)
    #print(data)
    # Split the data by comma
    #print(data)
    # Read the first
    if data[0:8] == "KT1AccX:":
        print("KT1AccX", data[9:15])
        # Insert the data into database
        timestamp = time.time()
        collection.insert_one({"timestamp": str(timestamp), "KT1AccX": data[9:15]})
"""
    if data[0:8] == "KT1AccY:":
        #print("KT1AccY:", data[8:15])
        schemas["K1 AccY"] = data[8:15]
    
    if data[0:8] == "KT1AccZ:":
        #print("KT1AccZ:", data[8:15])
        schemas["K1 AccZ"] = data[8:15]

    if data[0:8] == "KT1MagX:":
        print("KT1MagX:", data[8:15])
        schemas["K1 MagX"] = data[8:15]

    if data[0:8] == "KT1MagY:":
        print("KT1MagY:", data[8:15])
        schemas["K1 MagY"] = data[8:15]

    if data[0:8] == "KT1MagZ:":
        print("KT1MagZ:", data[8:15])
        schemas["K1 MagZ"] = data[8:15]

    if data[0:8] == "KT2AccX:":
        print("KT2AccX:", data[8:15])
        schemas["K2 AccX"] = data[8:15]

    if data[0:8] == "KT2AccY:":
        print("KT2AccY:", data[8:15])
        schemas["K2 AccY"] = data[8:15]

    if data[0:8] == "KT2AccZ:":
        print("KT2AccZ:", data[8:15])
        schemas["K2 AccZ"] = data[8:15]

    if data[0:8] == "KT2MagX:":
        print("KT2MagX:", data[8:15])
        schemas["K2 MagX"] = data[8:15]

    if data[0:8] == "KT2MagY:":
        print("KT2MagY:", data[8:15])
        schemas["K2 MagY"] = data[8:15]

    if data[0:8] == "KT2MagZ:":
        print("KT2MagZ:", data[8:15])
        schemas["K2 MagZ"] = data[8:15]

    if data[0:8] == "WG1STRAG:":
        print("WG1STRAG:", data[8:15])
        schemas["WG1 StrainGauge"] = data[8:15]

    if data[0:8] == "ADC:":
        print("ADC1:", data[8:15])
        schemas["ADC1"] = data[8:15]
    
    if data[0:8] == "ADC:":
        print("ADC2:", data[8:15])
        schemas["ADC2"] = data[8:15]

    if data[0:8] == "ADC:":
        print("ADC3:", data[8:15])
        schemas["ADC3"] = data[8:15]

    if data[0:8] == "ADC:":
        print("ADC4:", data[8:15])
        schemas["ADC4"].append(data[8:15])
            """
    # Insert the data into the collection
    
    #collection.insert_one(schemas)
    # Create a list
    #data_list.append(dbdata)