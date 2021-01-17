import bz2
from bz2 import BZ2Decompressor
from lxml import etree
import io

PATH_XML_WIKI = ""
PATH_INDEX_WIKI = ""


def getOffset(path, pageID):
    # Read the byte offsets from the index file
    page_offset = []
    last_offset = None
    previous = None
    curr_off = None
    with open(path, 'rb') as f:
        for line in f:
            offset = line.decode().split(':', 1)
            offset = line.decode().split(':', 2)
            offset[2] = offset[2].replace("\n", "")
            if last_offset != offset[0]:
                previous = last_offset
                last_offset = offset[0]
            if(int(offset[1]) == pageID):
                curr_off = offset[0]
                break

    return [int(previous), int(curr_off)]


def getByte(path, off0, off1):
    arr = None
    with open(path, 'rb') as f:
        f.seek(off0)
        arr = f.read(off1 - off0)
    return arr


def main():
    off = getOffset("index2.txt", 44702752)
    byte = getByte("enwiki-20210101-pages-articles-multistream22.xml-p44496246p44788941.bz2", off[0], off[1])
    getArticle(byte)


def _get_text(list_xml_el):
    return [el.text for el in list_xml_el]


def getArticle(byte):
    bz2d = BZ2Decompressor()
    byte_string = bz2d.decompress(byte)
    doc = etree.parse(io.BytesIO(b'<root> ' + byte_string + b' </root>'))


if __name__ == "__main__":
    main()
