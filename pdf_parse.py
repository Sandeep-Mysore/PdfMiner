import PyPDF2
import os
import sys
from datetime import datetime
from os.path import expanduser

class RuleEngine:
    def __init__(self):
        self.ts = datetime.now().strftime("%y-%m-%d")
        self.pdf_path = expanduser("~/Desktop/Files/")
        self.csv_path = expanduser("~/Desktop/Files/Output/")
        self.first()

    def first(self):
        for filename in os.listdir(self.pdf_path):
            file = '{}{}'.format(self.pdf_path,filename)
            try:
                print(file)
                pdf_file = open(file,'rb')
                read_file = PyPDF2.PdfFileReader(pdf_file)
                num_pages = read_file.getNumPages()
                for num in range(num_pages):
                    page = read_file.getPage(num)
                    Page_content = page.extractText()
                    y = Page_content.decode('utf-8')
                    print(y)
                    self.customer(y)
            except:
                print("Error ",sys.exc_info())


    def customer(self,lines):
        lines = lines.split(' ')
        for line in lines :
            name = lines[0]
            age = line[1]
            print(name,age)
            self.saver(name,age)

    def saver(self,name,age):
        try:
            with open(self.csv_path + name + '.csv', 'ab') as filew:
                    filew.write(name + ',' + age)
            filew.close()
        except:
            print("Error with writing to file",sys.exc_info())

if __name__ == '__main__':
    x = RuleEngine()
