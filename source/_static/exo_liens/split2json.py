#!/usr/bin/env python3

#
# Ce script est utilisé pour générer les version JSON des chapitres,
# nécessaire dans le cours Programmation Web Client Riche
#

from html.parser import HTMLParser
from json import dump
from re import compile as regex

NEWLINE = regex("\n *")

class MyParser(HTMLParser):

    nb = 1
    current = None
    data = ""

    def handle_starttag(self, tag, _):
        if tag == "section":
            self.current = { "txt": "", "links": [] }
        self.data = ""

    def handle_data(self, data):
        self.data += data

    def handle_endtag(self, tag):
        if tag == "p":
            self.current["txt"] = NEWLINE.sub(" ", self.data)
        elif tag == "li":
            linkno = self.data.rsplit(" ", 1)[-1]
            self.current["links"].append({
                "txt": self.data,
                "link": "#{}".format(linkno),
            })
        elif tag == "section":
            filename = "chapitre{}.json".format(self.nb);
            print(filename)
            with open(filename, "w") as f:
                dump(self.current, f, indent="    ")
            self.nb += 1
            
            

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        MyParser().feed(f.read())
        

