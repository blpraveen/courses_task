def chapterEntity(item)  -> dict:
    return {
        "name":item["name"],
        "text":item["text"]
    }

def courseEntityntity(entity) -> list:
    return [chapterEntity(item) for item in entity]
#Best way

def serializeChapterDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeChapterList(entity) -> list:
    return [serializeChapterDict(a) for a in entity]