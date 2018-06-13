# -*- coding: cp949 -*-
from readdata import *
from tkinter import *
from tkinter import font
from xml.etree.ElementTree import parse

import xml.etree.ElementTree as ET

doc = parse("Data1.xml")
Data1 = doc.getroot()

window = Tk()
window.title("휴게소 대표 음식")
window.geometry("600x600+750+200")

def CreateTitleLabel():
    title = "[휴게소 대표음식]"
    titlefont = font.Font(window, size=20, weight='bold', family='Consolas')
    ltitle = Label(window, font=titlefont, text=title)
    ltitle.pack()
    ltitle.place(x=20, y=30)

def CreateAddLabel():
    global AddLabel
    TempFont = font.Font(window, size=15,weight='bold', family = 'Consolas')
    AddLabel = Entry(window, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')

    AddLabel.pack()
    AddLabel.place(x=10, y=80)

def CreateDelLabel():
    global DelLabel
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    DelLabel = Entry(window, font=TempFont, width=26, borderwidth=12, relief='ridge')
    DelLabel.pack()
    DelLabel.place(x=10, y=200)
def CreateDelButton():
    
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
    SearchButton.place(x=330, y=140)

def CreateAddButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    AddButton = Button(window, font = TempFont, borderwidth = 10, text = "추가", command=AddButtonAction)
    AddButton.pack()
    AddButton.place(x=330, y=80)

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

    RenderText.configure(state='disabled')
    DelLabel.delete(0, END)

def AddButtonAction():
    global AddLabel, RenderText, window
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)

    keyword = str(AddLabel.get())

    RenderText.configure(state = 'disabled')
    AddLabel.delete(0,END)

def SearchButtonAction():
    global InputLabel, RenderText,window
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)

    #iSearchIndex = str(SearchListBox.curselection())

    keyword = str(InputLabel.get())

    SearchLibName(keyword)
    SearchLibAddress(keyword)

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


    RenderText.configure(state='disabled')

def DeleteName(keyword):
    global Data1, RenderText

    for location in Data1.findall("list"):
        if keyword in location.findtext("serviceAreaName"):
            Data1.remove(location)

    doc.write("Data1.xml", encoding="utf-8", xml_declaration=True)


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
CreateAddLabel()
CreateDelLabel()
CreateInputLabel()
CreateSearchButton()
CreateAddButton()
CreatePrintListButton()
CreateRenderText()

window.mainloop()