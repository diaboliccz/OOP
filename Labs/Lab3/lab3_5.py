record_collection = {
  2548: {
    'albumTitle': 'Slippery When Wet',
    'artist': 'Bon Jovi',
    'tracks': ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
    'albumTitle': '1999',
    'artist': 'Prince',
    'tracks': ['1999', 'Little Red Corvette']
  },
  1245: {
    'artist': 'Robert Palmer',
    'tracks': []
  },
  5439: {
    'albumTitle': 'ABBA Gold'
  }
}

def update_records(record, id, property, value):
    if id in record:
        if value == '':
            if property in record[id]:
                del record[id][property]
        else:
            if property != 'tracks':
                record[id][property] = value
            else:
                if property not in record[id]:
                    record[id]['tracks'] = []
                record[id][property].append(value)
    
    return record
update_records(record_collection, 5349, "artist", "")
for key, value in record_collection.items():
    print(key, end = ' ')
    print(value)
