# -*- coding: cp949 -*-
from readdata import *
from tkinter import *
from tkinter import font
from xml.etree.ElementTree import parse
from xml.etree.ElementTree import Element, SubElement

import xml.etree.ElementTree as ET

doc = parse("Data1.xml")
Data1 = doc.getroot()

window = Tk()
window.title("휴게소 대표 음식")
window.geometry("450x800+750+200")

def CreateTitleLabel():
    title = "[휴게소 대표음식]"
    titlefont = font.Font(window, size=20, weight='bold', family='Consolas')
    ltitle = Label(window, font=titlefont, text=title)
    ltitle.pack()
    ltitle.place(x=20, y=30)

def CreateAddLabel():
    CreateNameLabel()
    CreatePriceLabel()
    CreateFoodLabel()

def CreateNameLabel():
    global NameLabel
    TempFont = font.Font(window, size=10,weight='bold', family = 'Consolas')
    NameLabel = Entry(window, font = TempFont, width = 10, borderwidth = 12, relief = 'ridge')
    NameLabel.pack()
    NameLabel.place(x=10, y=80)

def CreateFoodLabel():
    global FoodLabel
    TempFont = font.Font(window, size=10,weight='bold', family = 'Consolas')
    FoodLabel = Entry(window, font = TempFont, width = 10, borderwidth = 12, relief = 'ridge')
    FoodLabel.pack()
    FoodLabel.place(x=110, y=80)

def CreatePriceLabel():
    global PriceLabel
    TempFont = font.Font(window, size=10,weight='bold', family = 'Consolas')
    PriceLabel = Entry(window, font = TempFont, width = 10, borderwidth = 12, relief = 'ridge')
    PriceLabel.pack()
    PriceLabel.place(x=210, y=80)

def CreateDelLabel():
    global DelLabel
    TempFont = font.Font(window, size=10, weight='bold', family='Consolas')
    DelLabel = Entry(window, font=TempFont, width=26, borderwidth=12, relief='ridge')
    DelLabel.pack()
    DelLabel.place(x=10, y=200)

def CreateDelButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    DelButton = Button(window, font=TempFont, borderwidth=10, text="삭제", command=DelButtonAction)
    DelButton.pack()
    DelButton.place(x=330, y=200)

def CreateInputLabel():
    global InputLabel
    TempFont = font.Font(window, size = 10, weight = 'bold', family = 'Consolas')
    InputLabel = Entry(window, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=10,y=140)

def CreateSearchButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font = TempFont, borderwidth = 10, text = "검색", command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=140)

def CreateAddButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    AddButton = Button(window, font = TempFont, borderwidth = 10, text = "추가", command=AddButtonAction)
    AddButton.pack()
    AddButton.place(x=330, y=80)

def CreateChangeButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    AddButton = Button(window, font = TempFont, borderwidth = 10, text = "변경", command=ChangeButtonAction)
    AddButton.pack()
    AddButton.place(x=250, y=200)

def CreateRenderText():
    global RenderText
    RenderTextScrollbar = Scrollbar(window)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=370,y=190)

    TempFont = font.Font(window, size = 10, family = 'Consolas')
    RenderText = Text(window, width = 49, height = 27, borderwidth = 8, relief = 'ridge',
                      yscrollcommand = RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10,y=250)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side = RIGHT, fill = Y)
    RenderText.configure(state='disabled')

def CreatePrintListButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, borderwidth=10, text="전체 출력", command=PrintList)
    SearchButton.pack()
    SearchButton.place(x=290, y= 20)

def DelButtonAction():
    global DelLabel, RenderText, window
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)

    keyword = str(DelLabel.get())
    DeleteName(keyword)
    RenderText.configure(state='disabled')
    DelLabel.delete(0, END)


def AddButtonAction():
    global NameLabel, RenderText, window, FoodLabel, PriceLabel
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)

    Name = str(NameLabel.get())
    Food = str(FoodLabel.get())
    Price = str(PriceLabel.get())

    switch = 0
    for location in Data1.findall("list"):
        if  Name in location.findtext("serviceAreaName"):
            RenderText.insert(INSERT, "삐빅! 중복입니다.")
            switch = 1

    if switch == 0:
        New = Element("list")
        NewName = Element("serviceAreaName")
        NewName.text = Name
        New.append(NewName)
        NewFood = Element("batchMenu")
        NewFood.text = Food
        New.append(NewFood)
        NewPrice = Element("salePrice")
        NewPrice.text = Price
        New.append(NewPrice)
        RenderText.insert(INSERT, Name)
        RenderText.insert(INSERT, "휴게소 추가 완료.")
        Data1.append(New)

    RenderText.configure(state = 'disabled')

    NameLabel.delete(0,END)
    FoodLabel.delete(0,END)
    PriceLabel.delete(0,END)

    doc.write("Data1.xml", encoding="utf-8", xml_declaration=True)

def ChangeButtonAction():
    global oldLabel, newLabel
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)

    oldLabel = str(InputLabel.get())
    newLabel = str(DelLabel.get())

    switch = 0
    for location in Data1.findall("list"):
        if oldLabel == location.findtext("serviceAreaName"):
            old = location.find("batchMenu")
            location.remove(old)
            New = Element("batchMenu")
            New.text = newLabel
            location.append(New)

            RenderText.insert(INSERT, "대표음식 변경 완료")
            switch = 1

    if switch == 0:
        RenderText.insert(INSERT, "그런 휴게소는 없습니다.")

    RenderText.configure(state = 'disabled')

    InputLabel.delete(0, END)
    DelLabel.delete(0, END)
    doc.write("Data1.xml", encoding="utf-8", xml_declaration=True)

def SearchButtonAction():
    global InputLabel, RenderText,window
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)

    #iSearchIndex = str(SearchListBox.curselection())

    keyword = str(InputLabel.get())
    SearchLibName(keyword)
    #SearchLibAddress(keyword)

    #RenderText.insert(INSERT, InputLabel.get())

    RenderText.configure(state = 'disabled')
    InputLabel.delete(0,END)

def PrintList():

    global Data1, Data2, RenderText

    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)

    i=0

    for location in Data1.findall("list"):
        i += 1
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i)
        RenderText.insert(INSERT, "]")

        RenderText.insert(INSERT, chr(10))
        RenderText.insert(INSERT, "휴게소명 : ")
        RenderText.insert(INSERT, location.findtext("serviceAreaName"))
        RenderText.insert(INSERT, "휴게소 ")
        RenderText.insert(INSERT, chr(10))
        try:
            RenderText.insert(INSERT, "대표음식 : ")
            RenderText.insert(INSERT, location.findtext("batchMenu"))
            RenderText.insert(INSERT, chr(10))
        except:
            RenderText.insert(INSERT, chr(10))
            pass
        try:
            RenderText.insert(INSERT, "가격     : ")
            RenderText.insert(INSERT, location.findtext("salePrice"))
            RenderText.insert(INSERT, chr(10))
        except:
            RenderText.insert(INSERT, chr(10))
            pass
        try:
            RenderText.insert(INSERT, "위치     : ")
            RenderText.insert(INSERT, location.findtext("routeName"))
            RenderText.insert(INSERT, chr(10))
            RenderText.insert(INSERT, "방향     : ")
            RenderText.insert(INSERT, location.findtext("direction"))
            RenderText.insert(INSERT, chr(10))
        except:
            RenderText.insert(INSERT, chr(10))
    RenderText.configure(state='disabled')

def DeleteName(keyword):
    global Data1, RenderText

    for location in Data1.findall("list"):
        if keyword in location.findtext("serviceAreaName"):
            Data1.remove(location)
            RenderText.insert(INSERT, keyword)
            RenderText.insert(INSERT, "휴게소 삭제 완료")

    doc.write("Data1.xml", encoding="utf-8", xml_declaration=True)

def SearchPrice(keyword):
    global Data1, RenderText

    i = 0

    for location in Data1.findall("list"):
        if keyword in location.findtext("salePrice"):
            i = i + 1
    if i != 0:
        RenderText.insert(INSERT, " - 가격 검색 결과 - ")
        RenderText.insert(INSERT, chr(10))
        RenderText.insert(INSERT, " 총 = ")
        RenderText.insert(INSERT, i)
        RenderText.insert(INSERT, " 건 ")
        RenderText.insert(INSERT, chr(10))

    for location in Data1.findall("list"):
        if keyword in location.findtext("salePrice"):
            RenderText.insert(INSERT, chr(10))
            RenderText.insert(INSERT, "휴게소명 : ")
            RenderText.insert(INSERT, location.findtext("serviceAreaName"))
            RenderText.insert(INSERT, "휴게소 ")
            RenderText.insert(INSERT, chr(10))
            try:
                RenderText.insert(INSERT, "대표음식 : ")
                RenderText.insert(INSERT, location.findtext("batchMenu"))
                RenderText.insert(INSERT, chr(10))
            except:
                RenderText.insert(INSERT, chr(10))
                pass
            try:
                RenderText.insert(INSERT, "가격     : ")
                RenderText.insert(INSERT, location.findtext("salePrice"))
                RenderText.insert(INSERT, chr(10))
            except:
                RenderText.insert(INSERT, chr(10))
                pass
def SearchLibName(keyword):
    global Data1, RenderText
    i=0

    for location in Data1.findall("list"):
        if keyword in location.findtext("serviceAreaName"):
            i = i+1
    if i != 0:
        RenderText.insert(INSERT, " - 휴게소명 검색 결과 - ")
        RenderText.insert(INSERT, chr(10))
        RenderText.insert(INSERT, " 총 = ")
        RenderText.insert(INSERT, i)
        RenderText.insert(INSERT, " 건 ")
        RenderText.insert(INSERT, chr(10))

    for location in Data1.findall("list"):
        if keyword in location.findtext("serviceAreaName"):

            RenderText.insert(INSERT, chr(10))
            RenderText.insert(INSERT, "휴게소명 : ")
            RenderText.insert(INSERT, location.findtext("serviceAreaName"))
            RenderText.insert(INSERT, "휴게소 ")
            RenderText.insert(INSERT, chr(10))
            try:
                RenderText.insert(INSERT, "대표음식 : ")
                RenderText.insert(INSERT, location.findtext("batchMenu"))
                RenderText.insert(INSERT, chr(10))
            except:
                RenderText.insert(INSERT, chr(10))
                pass
            try:
                RenderText.insert(INSERT, "가격     : ")
                RenderText.insert(INSERT, location.findtext("salePrice"))
                RenderText.insert(INSERT, chr(10))
            except:
                RenderText.insert(INSERT, chr(10))
                pass

            i += 1

def SearchLibAddress(keyword):
    global Data1, RenderText
    i = 0
    for location in Data1.findall("list"):
        if keyword in location.findtext("routeName"):
            i = i + 1
    if i != 0:
        RenderText.insert(INSERT, " - 노선 검색 결과 - ")
        RenderText.insert(INSERT, chr(10))
        RenderText.insert(INSERT, " 총 = ")
        RenderText.insert(INSERT, i)
        RenderText.insert(INSERT, " 건 ")
        RenderText.insert(INSERT, chr(10))

    for location in Data1.findall("list"):
        if keyword in location.findtext("routeName"):
            RenderText.insert(INSERT, chr(10))
            RenderText.insert(INSERT, "휴게소명 : ")
            RenderText.insert(INSERT, location.findtext("serviceAreaName"))
            RenderText.insert(INSERT, "휴게소 ")
            RenderText.insert(INSERT, chr(10))
            try:
                RenderText.insert(INSERT, "대표음식 : ")
                RenderText.insert(INSERT, location.findtext("batchMenu"))
                RenderText.insert(INSERT, chr(10))
            except:
                RenderText.insert(INSERT, chr(10))
                pass
            try:
                RenderText.insert(INSERT, "가격     : ")
                RenderText.insert(INSERT, location.findtext("salePrice"))
                RenderText.insert(INSERT, chr(10))
            except:
                RenderText.insert(INSERT, chr(10))
                pass

            i += 1

CreateTitleLabel()
CreateAddLabel()
CreateDelLabel()
CreateInputLabel()
CreateSearchButton()
CreateAddButton()
CreateDelButton()
CreatePrintListButton()
CreateChangeButton()
CreateRenderText()

window.mainloop()