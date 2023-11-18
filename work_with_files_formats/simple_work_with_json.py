import json

nicknames = {
    'user1': '@boss',
    'user2': '@terminator',
    'user3': '@killer',
    'user4': '@Stepa2007',
    'user5': '@nagibaTOR_007'
}

with open('test1.json', 'w') as jsonfile:
    json.dump(nicknames, fp=jsonfile, indent=4, ensure_ascii=False)
    print(json.dumps(nicknames, indent=4))

print()

with open('test1.json', 'r') as jsonfile:
    json_object = json.load(jsonfile)
    print(json_object)
