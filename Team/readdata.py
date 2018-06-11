# -*- coding: cp949 -*-
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse

Data = None

def LoadXMLFromFile():
    global Data1
    url = "http://data.ex.co.kr/exopenapi/business/representFoodServiceArea?serviceKey=P4TkNFl6W62jL6AhQK9P5JSevL2DDkQzusbTPn%2FctxbHMUGQT52dMIX4COLjw8YYSyAw5D5W%2Bh3ChjJsmRQJow%3D%3D&type=xml&numOfRows=199&pageSize=199&pageNo=1&startPage=1"
    savename = 'data.xml'

    data_1 = urllib.request.urlopen(url).read()
    text = data_1.decode('utf-8')

    req.urlretrieve(url, savename)

    xml = open(savename, "r", encoding="utf-8").read()
    Data1 = BeautifulSoup(xml, "html.parser")
    return Data1

def LoadXMLFromFile2():
    global Data2
    url = "http://data.ex.co.kr/exopenapi/business/representFoodServiceArea?serviceKey=P4TkNFl6W62jL6AhQK9P5JSevL2DDkQzusbTPn%2FctxbHMUGQT52dMIX4COLjw8YYSyAw5D5W%2Bh3ChjJsmRQJow%3D%3D&type=xml&numOfRows=200&pageSize=200&pageNo=2&startPage=2"
    savename = 'data.xml_2'

    data_2 = urllib.request.urlopen(url).read()
    text = data_2.decode('utf-8')

    req.urlretrieve(url, savename)

    xml = open(savename, "r", encoding="utf-8").read()
    Data2 = BeautifulSoup(xml, "html.parser")
    return Data2
