def courseEntity(item)  -> dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "dates":item["date"],
        "description":item["description"],
        "domain":item["domain"],
        "chapters":item["chapters"],
    }

def courseEntityntity(entity) -> list:
    return [courseEntity(item) for item in entity]
#Best way

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]