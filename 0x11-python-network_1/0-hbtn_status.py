#!/usr/bin/python3
""" 0. script to fetch web content and print out. """

import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()

        print("Body response:\n\t- type: %s\n\t- content: %s\n
        \t- utf8 content: %s".format(type(html), html, html.decode('utf-8')))
