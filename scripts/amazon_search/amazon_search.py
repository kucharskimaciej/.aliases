#!/usr/bin/python3.4

import pyperclip
import os
import webbrowser
import requests
import re
import bs4

search_page = 'http://google.com'
search_prefix = '/search?q='
search_suffix = ' site:amazon.com'

max_open = 3

def search(query):
    search_query = ('').join([search_page, search_prefix, query, search_suffix])

    res = requests.get(search_query)
    res.raise_for_status()

    DOM = bs4.BeautifulSoup(res.text, 'lxml')
    found_links = DOM.select("#ires .r a")

    return [link.get('href') for link in found_links]

def open_browser(urls=[]):
    for url in urls[:min(len(urls), max_open)]:
        webbrowser.open(search_page + url)

if __name__ == '__main__':
    import sys

    args = sys.argv[1:]
    if len(args) > 1:
        query = (' ').join(args)
    else:
        query = pyperclip.paste()

    urls = search(query)
    open_browser(urls)

    sys.exit()
