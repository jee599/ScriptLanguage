#-*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import urllib.request
from xml.etree.ElementTree import parse
def LoadXML1():
    global Data1
    url = "http://data.ex.co.kr/exopenapi/business/representFoodServiceArea?serviceKey=P4TkNFl6W62jL6AhQK9P5JSevL2DDkQzusbTPn%2FctxbHMUGQT52dMIX4COLjw8YYSyAw5D5W%2Bh3ChjJsmRQJow%3D%3D&type=xml&numOfRows=199&pageSize=199&pageNo=1&startPage=1"

    #tree = ET.ElementTree(file= urllib.request.urlopen(url))
    tree = parse("Data1.xml")
    Data1 = tree.getroot()

    return Data1


def LoadXML2():
    global Data2

    url = "http://data.ex.co.kr/exopenapi/business/representFoodServiceArea?serviceKey=P4TkNFl6W62jL6AhQK9P5JSevL2DDkQzusbTPn%2FctxbHMUGQT52dMIX4COLjw8YYSyAw5D5W%2Bh3ChjJsmRQJow%3D%3D&type=xml&numOfRows=200&pageSize=200&pageNo=2&startPage=2"

    tree = ET.ElementTree(file=urllib.request.urlopen(url))
   # tree.write("Data2.xml")
    tree = parse("Data2.xml")
    Data2 = tree.getroot()

    return Data2