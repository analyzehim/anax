#!/usr/bin/python
# -*- coding: utf8 -*-
import requests
import time
from bs4 import BeautifulSoup
import md5
import pickle
import random

def getProxies():
    f = open("proxy", "r")
    proxy_url = f.read()
    f.close()

    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }
    return proxies

special_parts = ("/wiki/Template_talk:",
                 "/wiki/Book:",
                 "/wiki/Help:",
                 "/wiki/Special:",
                 "/wiki/Main_Page",
                 "/wiki/Portal:",
                 "/wiki/Category:",
                 "/wiki/Wikipedia:",
                 "/wiki/File:",
                 "/wiki/Talk:",
                 "/wiki/Template:",
                 "wiki/User:",
                 "wiki/ISO_")

def checkMode():
    try:
            requests.get('https://www.ya.ru')
            return False
    except:
            return True

def check_link(link):
    if link[:6] == '/wiki/':
        for part in special_parts:
            if part in link:
                return False
        return True
    return False

def get_urls(URL, proxy_flag, proxies):
    wiki_url = "https://en.wikipedia.org"
    link_set = set()
    if proxy_flag:
        r = requests.post(URL, proxies=proxies)
    else:
        r = requests.post(URL)

    text = r.text
    soup = BeautifulSoup(text, 'html.parser')
    for link_a in soup.find_all('a'):
        try:
            link = str(link_a.get('href'))

            if check_link(link):
                link_set.add(wiki_url + link)
        except UnicodeEncodeError:
            pass
            #add log print "Error with ",link.get('href')
    return link_set


