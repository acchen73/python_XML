# -*- coding:utf8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom

#DOMTree = xml.dom.minidom.parse("movie.xml")
#collection = DOMTree.documentElement
#if collection.hasAttribute("shelf"):
    #print("Root element : %s" % collection.__getattribute__("shelf"))


DOMTree = xml.dom.minidom.parse("class.xml")
NewDataSet = DOMTree.documentElement
if NewDataSet.hasAttribute("xmlns"):
    print("Root element : %s" % NewDataSet.getAttribute("xmlns"))
#獲取table中的數值
table = NewDataSet.getElementsByTagName("Table1")
#z = 0
#印出每個課程的內容
for Table1 in table:
    #z+=1
    print("**********課程**********")
    if Table1.hasAttribute("課程名稱"):
        print("課程名稱： %s" % Table1.getAttribute("課程名稱"))
#print(z) 我只是在算次數 don't mind

#以下是把tag東西列出來
    a = Table1.getElementsByTagName("辦理單位")[0]
    print("辦理單位: %s" % a.childNodes[0].data)

    b = Table1.getElementsByTagName("開班單位")[0]
    print("開班單位: %s" % b.childNodes[0].data)

    c = Table1.getElementsByTagName("訓練期間")[0]
    print("訓練期間: %s" % c.childNodes[0].data)

    d = Table1.getElementsByTagName("訓練時段")[0]
    print("訓練時段: %s" % d.childNodes[0].data)

    e = Table1.getElementsByTagName("訓練時數")[0]
    print("訓練時數: %s" % e.childNodes[0].data)

    f = Table1.getElementsByTagName("訓練地點")[0]
    print("訓練地點: %s" % f.childNodes[0].data)

    g = Table1.getElementsByTagName("訓練位置")[0]
    print("訓練位置: %s" % g.childNodes[0].data)

    h = Table1.getElementsByTagName("報名日期")[0]
    print("報名日期: %s" % h.childNodes[0].data)

    i = Table1.getElementsByTagName("甄試日期")[0]
    print("甄試日期: %s" % i.childNodes[0].data)

    j = Table1.getElementsByTagName("負擔費用")[0]
    print("負擔費用: %s" % j.childNodes[0].data)

    k = Table1.getElementsByTagName("聯絡人")[0]
    print("聯絡人: %s" % k.childNodes[0].data)

    l = Table1.getElementsByTagName("聯絡電話")[0]
    print("聯絡電話: %s" % l.childNodes[0].data)

    m = Table1.getElementsByTagName("課程名稱")[0]
    print("課程名稱: %s" % m.childNodes[0].data)

    n = Table1.getElementsByTagName("期別")[0]
    print("期別: %s" % n.childNodes[0].data)

    o = Table1.getElementsByTagName("課程代碼")[0]
    print("課程代碼: %s" % o.childNodes[0].data)

    p = Table1.getElementsByTagName("訓練概要")[0]
    print("訓練概要: %s" % p.childNodes[0].data)

    q = Table1.getElementsByTagName("課程內容")[0]
    print("課程內容: %s" % q.childNodes[0].data)
