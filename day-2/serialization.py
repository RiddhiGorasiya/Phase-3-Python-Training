# Serialization

import json
L = [
    {
        "tradeid": 1, "symbol": "AAPL", "price": 150.0, "volume": 1234
    }, 
    {
        "tradeid": 2, "symbol": "GOOGL", "price": 2800.5, "volume": 567
    },
    {
        "tradeid": 3, "symbol": "MSFT", "price": 300.75, "volume": 890
    },
    {
        "tradeid": 4, "symbol": "AMZN", "price": 3400.0, "volume": 345
    },
    {
        "tradeid": 5, "symbol": "TSLA", "price": 700.25, "volume": 678
    }
]

with open('trades.json', 'w') as f:
    json.dump(L, f, indent=4)
    
# Deserialization

import json
students = '{"id": "01", "name": "Riddhi", "department": "Computer Science "}'
student_dict = json.loads(students)
print(student_dict)
print(student_dict['name'])  # Accessing name from the dictionary
print("Deserialization complete.")

# # Serialization and Deserialization tuple

t = ("T1234", "AAPL", 150.0)
with open('trade_tuple.json', 'w') as f:
    json.dump(t, f)

# Serialize and Deserialize an Open File Object Using Pickle

import pickle

# Serialize
data = {'name': 'John', 'age': 30}
with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)

# Deserialize
with open('data.pickle', 'rb') as file:
    serialized_data = file.read()
    file.seek(0)
    loaded_data = pickle.load(file)

print("Type of serialized data:", type(serialized_data))
print("\nDeserialized data:", loaded_data)
print("Type of deserialized data:", type(loaded_data))

