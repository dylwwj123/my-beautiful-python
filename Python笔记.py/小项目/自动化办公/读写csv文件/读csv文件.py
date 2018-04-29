import csv

def readCsv(path):
    infolist = []
    with open(path, "r")as f:
         allFileInfo = csv.reader(f)
         for rowstr in allFileInfo:
            allcount = rowstr.count('')
            print(allcount)
            for newrows in range(allcount):
                rowstr.remove('')
                infolist.append(rowstr)
    return infolist


path1 = r"/Users/wukaihao/Desktop/python/hello.py/小项目/自动化办公/读写csv文件/csv002.csv"

infolist = readCsv(path1)
print(infolist)