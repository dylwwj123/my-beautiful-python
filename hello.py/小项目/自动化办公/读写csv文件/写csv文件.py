import csv

def writeCsv(path, data):
    with open(path, 'w')as f:
        writer = csv.writer(f)
        for rowdata in data:
            print(rowdata)
            writer.writerow(rowdata)

path1 = r"/Users/wukaihao/Desktop/python/hello.py/小项目/自动化办公/读写csv文件/csv001.csv"

writeCsv(path1, [["qweqwdasd2131",2,3],[4,5,6],[7,8,9]])