#!/usr/bin/env python3

#
# Ce script est utilisé pour générer les version JSON des chapitres,
# nécessaire dans le cours Programmation Web Client Riche
#

from html.parser import HTMLParser
from json import dump
from re import compile as regex

def makelink(n):
    return "chapitre{}.json".format(n)

NEWLINE = regex("\n *")

class MyParser(HTMLParser):

    nb = 0
    current = None
    data = ""

    def dump_json(self):
        if self.current:
            filename = makelink(self.nb)
            print(filename)
            with open(filename, "w") as f:
                dump(self.current, f, indent="    ")
        self.nb += 1

    def handle_starttag(self, tag, _):
        if tag == "section":
            self.dump_json()
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
                "link": makelink(linkno),
            })
            

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        MyParser().feed(f.read())
        

