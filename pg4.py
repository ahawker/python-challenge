__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'

import urllib

URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={0}'

def pg4():
    """
    Loop through redirects until it yields the next project page.
    NEXT: http://www.pythonchallenge.com/pc/def/peak.html
    """
    nothing = '12345'
    while True:
        content = urllib.urlopen(URL.format(nothing)).read()
        if '.html' in content:
            return content
        nothing = content.split(' ')[-1]
