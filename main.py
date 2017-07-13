import pickle, time
timestamp = time.time()
f = open("C:\\Users\\raev_e\\Downloads\\dump_back", "rb")
print "OPEN", time.time() - timestamp
timestamp = time.time()
wiki_dict = pickle.load(f)
print "LOAD", time.time() - timestamp
f.close()
print len(wiki_dict)

max_links = 0

for key in wiki_dict:
    if len(wiki_dict[key]) > max_links:
        max_links = len(wiki_dict[key])
        max_key = key
        print max_links, max_key
