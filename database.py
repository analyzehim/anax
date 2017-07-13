
from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client['local']

collection = db['wiki']
collection.insert({"id":1, "data":'value'})

cursor = collection.find({})
for document in cursor:
        print(document)

'''

import sqlite3
def init_db():
        conn = sqlite3.connect('C:\\Users\\raev_e\\Downloads\\example.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS wiki (link text, data text, count int)')
        return c,conn

def check_db(c, link):
        c.execute('SELECT * FROM wiki WHERE wiki.link = "{0}"'.format(link))
        return not(c.fetchone() == None)


def add_db(c, conn, link, wiki_set):
        c.execute('INSERT INTO wiki VALUES ( "{0}", "{1}", "{2}" )'.format(link, wiki_set, len(wiki_set)))
        conn.commit()
        return

def get_all(c):
        c.execute('SELECT * FROM wiki')
        return c

def close_db(conn):
        conn.close()

(c, conn) = init_db()
c = get_all(c)
for i in c:
        print i
'''