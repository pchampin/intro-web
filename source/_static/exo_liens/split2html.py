#!/usr/bin/env python3

#
# Ce script est utilisé pour générer chapitres.tar.gz,
# nécessaire pour la 2e partie de l'exercice.
#

from html.parser import HTMLParser
from json import dumps
from re import compile as regex

HEADER = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8"/>
    <title>Page HTML dont vous êtes le héros - n°{}</title>
  </head>
  <body>
    """

FOOTER = """
  </body>
</html>
"""

class MyParser(HTMLParser):

    nb = 1
    data = ""

    def handle_starttag(self, tag, _):
        if tag == "section":
            self.data = HEADER.format(self.nb)
        if self.data:
            self.data += "<{}>".format(tag)

    def handle_data(self, data):
        if self.data:
            self.data += data

    def handle_endtag(self, tag):
        if self.data:
            self.data += "</{}>".format(tag)
        if tag == "section":
            self.data += FOOTER
            filename = "chapitre{}.html".format(self.nb)
            print(filename)
            with open(filename, "w") as f:
                f.write(self.data)
            self.nb += 1
            self.data = ""
            

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        MyParser().feed(f.read())
        

