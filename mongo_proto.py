from pymongo import MongoClient


def init_db():
    client = MongoClient('localhost', 27017)
    db = client['local']
    collection = db['wiki']
    return collection, collection

def check_db(collection, link):
    c = collection.find({"link": link})
    if c.count() == 0:
        return False
    return True

def add_db(c, conn, link, wiki_set):
    c.insert({"link": link, "count": len(wiki_set), "data": list(wiki_set)})
    return

def close_db(conn):
    return
