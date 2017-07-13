from proto import *
from mongo_proto import *





first_url = "https://en.wikipedia.org/wiki/United_States"
(c, conn) = init_db()

timestamp = time.time()
proxy_flag = checkMode()
proxies = ''
if proxy_flag:
    proxies = getProxies()


links_set = get_urls(first_url, proxy_flag, proxies)
if not check_db(c, first_url):
    add_db(c, conn, first_url, links_set)

count = 0

while True:
    count += 1
    if count % 100 ==0:
        print count
    URL = random.sample(links_set, 1)[0]
    if check_db(c, URL):
        print count, "Already exists ", URL
        continue
    else:
        urls = get_urls(URL, proxy_flag, proxies)
        links_set = links_set|urls
        add_db(c, conn, URL, links_set)
        #print count, "Added ", URL

close_db(conn)
