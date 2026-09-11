import json

with open('example.json','r') as f:
    data = json.load(f)

print(data)

data = {'name':'John','age':30,'city':'New York'}
with open('test.json','w') as f:
    json.dump(data, f, indent=4)
