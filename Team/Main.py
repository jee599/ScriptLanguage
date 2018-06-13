# -*- coding: cp949 -*-
from readdata import *
from tkinter import *
from tkinter import font
import xml.etree.ElementTree as ET

Data1 = LoadXML1()
Data2 = LoadXML2()

window = Tk()
window.title("휴게소 대표 음식")
window.geometry("600x600+750+200")

def CreateTitleLabel():
    title = "[휴게소 대표음식]"
    titlefont = font.Font(window, size=20, weight='bold', family='Consolas')
    ltitle = Label(window, font=titlefont, text=title)
    ltitle.pack()
    ltitle.place(x=5, y=10)

def CreateSearchListBox():
    global SearchListBox
    TempFont = font.Font(window, size=15,weight='bold', family = 'Consolas')
    SearchListBox = Listbox(window, font = TempFont, activestyle = 'none',
                            width = 20, height = 2, borderwidth = 8, relief = 'ridge')

    SearchListBox.pack()
    SearchListBox.place(x=10, y=70)

def CreateInputLabel():
    global InputLabel
    TempFont = font.Font(window, size = 15, weight = 'bold', family = 'Consolas')
    InputLabel = Entry(window, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=10,y=140)

def CreateSearchButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font = TempFont, borderwidth = 10, text = "검색", command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=350, y=140)

def CreateAddButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    AddButton = Button(window, font = TempFont, borderwidth = 10, text = "추가", command=SearchButtonAction)
    AddButton.pack()
    AddButton.place(x=350, y=80)

def CreateRenderText():
    global RenderText
    RenderTextScrollbar = Scrollbar(window)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=370,y=190)

    TempFont = font.Font(window, size = 10, family = 'Consolas')
    RenderText = Text(window, width = 49, height = 27, borderwidth = 8, relief = 'ridge',
                      yscrollcommand = RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10,y=195)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side = RIGHT, fill = Y)
    RenderText.configure(state='disabled')


def CreatePrintListButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, borderwidth=10, text="전체 출력", command=PrintList)
    SearchButton.pack()
    SearchButton.place(x=350, y=28)

def SearchButtonAction():
    global SearchListBox, InputLabel, RenderText,window
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)

    iSearchIndex = str(SearchListBox.curselection())

    keyword = str(InputLabel.get())
    SearchLibName(keyword)
    SearchLibAddress(keyword)
    SearchPrice(keyword)

    #RenderText.insert(INSERT, InputLabel.get())

    RenderText.configure(state = 'disabled')
    InputLabel.delete(0,END)

def PrintList():
    global Data1, Data2, RenderText
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    i=0
    for location in Data1.findall("list"):
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
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
        RenderText.insert(INSERT, "위치     : ")
        RenderText.insert(INSERT, location.findtext("routeName"))
        RenderText.insert(INSERT, chr(10))
        RenderText.insert(INSERT, "방향     : ")
        RenderText.insert(INSERT, location.findtext("direction"))
        RenderText.insert(INSERT, chr(10))

        i += 1

    if (i >= 99):
        for location in Data2.findall("list"):
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")

            RenderText.insert(INSERT, chr(10))
            RenderText.insert(INSERT, "휴게소명    : ")
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
                RenderText.insert(INSERT, "가격    : ")
                RenderText.insert(INSERT, location.findtext("salePrice"))
                RenderText.insert(INSERT, chr(10))
            except:
                RenderText.insert(INSERT, chr(10))
                pass
            RenderText.insert(INSERT, "위치    : ")
            RenderText.insert(INSERT, location.findtext("routeName"))
            RenderText.insert(INSERT, chr(10))
            RenderText.insert(INSERT, "방향    : ")
            RenderText.insert(INSERT, location.findtext("direction"))
            RenderText.insert(INSERT, chr(10))

            i += 1

    RenderText.configure(state='disabled')

def SearchPrice(keyword):
    global Data1, RenderText
    i = 0
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
CreateSearchListBox()
CreateInputLabel()
CreateSearchButton()
CreateAddButton()
CreatePrintListButton()
CreateRenderText()

window.mainloop()