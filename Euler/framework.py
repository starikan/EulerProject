# -*- coding: utf-8 -*-
__author__ = 'Starik'

import os
import re
import math

import numpy as np


""" OS """

class FileList():
    """ Working with filenames """

    def __init__(self, path=os.getcwd()):
        """ path -> ur"some_text" """
        self.path = path
        self.pathAll = [i for i in os.walk(self.path)]

    def getFiles(self, filter=[], depth="one", namesView=""):
        """Take filenames from directory.

        Arguments:
        filter -- filter filenames in regular expressions
        depth -- depth of finding files -> "one" - same folder, other - all depth
        namesView -- if path = "c:\" "full" -> "c:\foo\spam.txt", "short" -> "spam.txt", other -> "foo\spam.txt"

        """
        if not isinstance(filter, list): filter = [str(filter)]
        pathAll = self.pathAll

        # Filter
        for filt in filter:
            for iter, item in enumerate(pathAll):
                removeList = []
                for iter2,item2 in enumerate(item[2]):
                    if len(re.findall(filt,item2))==0:
                        removeList.append(item2)
                for remove in removeList:
                    pathAll[iter][2].remove(remove)

        # Depth
        if depth=="one":
            pathAll = [pathAll[0],]

        # NameseReturn
        files = []
        for i in pathAll:
            for i2 in i[2]:
                if namesView=="full":
                    files.append(os.path.join(self.path, i[0], i2))
                elif namesView=="short":
                    files.append(os.path.join(i[0], i2))
                else:
                    files.append(i2)

        return files

class File():
    """ Working with concretely file """

    def __init__(self, path):
        self.path = path

    def openFileToList(self):
        """ Open file -> list """
        with open(self.path, "r") as f:
            text = [i.strip() for i in f.xreadlines()]
        return text

    def replaceStringInFile(self, find="", repl=""):
        """ Replace string in file. """
        with open(self.path, "r") as f:
            text = f.read()
        with open(self.path, "w") as f:
            f.write(re.sub(find, repl, text))

class MathClass():
    """ Математические методы """
    def __init__(self):
        pass

    def primeListUpTo(self, upto):
        """ Список простых чисел до определенного числа """
        primes=np.arange(3,upto+1,2)
        isprime=np.ones((upto-1)/2,dtype=bool)
        for factor in primes[:int(math.sqrt(upto))]:
            if isprime[(factor-2)/2]: isprime[(factor*3-2)/2::factor]=0
        return list(np.insert(primes[isprime],0,2))


def openFileToList(fileName=""):
    """ Open file -> list """
    with open(fileName, "r") as f:
        text = [i.strip() for i in f.xreadlines()]
    return text

def translit(str, method = "0"):
    """ Транслитерация русского текста, принимает Unicode строки """
    # http://habrahabr.ru/blogs/python/137089/ - статья про транслитерацию
    result = ''
    simbRuss = u"а,б,в,г,д,е,ё,ж,з,и,й,к,л,м,н,о,п,р,с,т,у,ф,х,ц,ч,ш,щ,ъ,ы,ь,э,ю,я,А,Б,В,Г,Д,Е,Ё,Ж,З,И,Й,К,Л,М,Н,О,П,Р,С,Т,У,Ф,Х,Ц,Ч,Ш,Щ,Ъ,Ы,Ь,Э,Ю,Я".split(",")
    simbEng  = u"a,b,v,g,d,e,yo,j,z,i,i,k,l,m,n,o,p,r,s,t,u,f,h,c,ch,sh,sch,,y,',e,yu,ya,A,B,V,G,D,E,YO,J,Z,I,I,K,L,M,N,O,P,R,S,T,U,F,H,C,CH,SH,SCH,,Y,',E,YU,YA".split(",")
    for i in str:
        if i in simbRuss:
            result += simbEng[simbRuss.index(i)]
        else:
            result += i
    return result

def removeAll(remove, list):
    """ Удаляет все элементы равные remove из list """
    listItems = []
    for iter,item in enumerate(list):
        if remove==item:
            listItems.append(iter)
    listItems.reverse()
    for i in listItems:
        del list[i]
    return list

def coordsTrans(input):
    """ Преобразование координат """
    if isinstance(input, str): # TODO: basestring
        split = re.split(r"[^\.\d]", input)
        if "" in split: removeAll("", split)
        if len(split)==1:
            result = float(split[0])
        elif len(split)==2:
            result = float(split[0])+float(split[1])/60
        elif len(split)==3:
            result = float(split[0])+float(split[1])/60+float(split[2])/3600
        else:
            result = 0
        return result
    else:
        return None

def test(func=""):

    if func=="":
        print u"""Нужно ввести test(функция)
        Функции:
        - translite
        """

    if func=="translit":
        print "==== def TRANSLITE ===="
        print "Работа функции translit(str) - возвращает строку транслитерации"
        print "method=0"
        str=raw_input("Ввести строку: ")
        if str=="": str=u"Тестовая строка"
        print u"Ввод: "+str
        print u"Результат: "+translit(str)

    if func=="coordsTrans":
        print u"E48°55'20.86 -> "+"%f" % coordsTrans("E48°55'20.86")
        print u"N54°36'26.26 -> "+"%f" % coordsTrans("N54°36'26.26")
        print u"48°55 -> "+"%f" % coordsTrans("48°55")
        print u"48 55 -> "+"%f" % coordsTrans("48 55")



if __name__ == "__main__":
    test("coordsTrans")