import bz2
from bz2 import BZ2Decompressor
from lxml import etree
import io
import requests
import json


class Wikipedia:

    def __init__(self):
        print("test")

    def getWikipediaID(self, title):
        url = ("http://en.wikipedia.org/w/api.php?action=query&titles={}&format=json").format(title)
        response = json.loads(requests.get(url).text)
        for a in response["query"]["pages"].keys():
            return int(a)

    def getOffset(self, path, pageID):
        # Read the byte offsets from the index file
        page_offset = []
        last_offset = 0
        curr_off = 0
        found = False
        with open(path, 'rb') as f:
            for line in f:
                offset = line.decode().split(':', 2)
                # offset[2] = offset[2].replace("\n", "")
                if(int(offset[1]) == pageID):
                    last_offset = offset[0]
                    found = True

                if last_offset != offset[0] and found == True:
                    curr_off = offset[0]
                    break

        return [int(last_offset), int(curr_off)]

    def getByte(self, path, off0, off1):
        arr = None
        with open(path, 'rb') as f:
            f.seek(off0)
            arr = f.read(off1 - off0)
        return arr

    def getFullArticle(self, text):
        pageID = self.getWikipediaID(text)
        off = self.getOffset("index.txt", pageID)
        byte = self.getByte("enwiki-20210101-pages-articles-multistream.xml.bz2", off[0], off[1])
        return self.getArticle(byte, pageID)

    def getReadable(self, list_xml_el):
        return [el.text for el in list_xml_el]

    def getArticle(self, byte, pageID):
        bz2d = BZ2Decompressor()
        byte_string = bz2d.decompress(byte)
        doc = etree.parse(io.BytesIO(b'<root> ' + byte_string + b' </root>'))
        r = self.getReadable(doc.xpath("*/id"))
        index = r.index(str(pageID))
        r = self.getReadable(doc.xpath("*/revision/text"))[index]

        # print(r)
        article = r.find("'''")
        r = r[article:]
        articleE = r.find("==")
        r = r[:articleE]

        return r


