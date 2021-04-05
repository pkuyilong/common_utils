import os
class FileParser():

    def file_open(self, inputfile, outputfile=""):
        self.fin = open(inputfile, 'r')

        if os.path.exists(outputfile):
            os.remove(outputfile)

        if outputfile != '':
            self.fout = open(outputfile, 'w')
        return self.fin

    def save(self, content): 
        self.fout.write(content)

    def file_close(self):
        self.fin.close()
        if self.fout:
            self.fout.close()
    

class TextFileParser(FileParser):
    def __init__(self, inputfile, outputfile):
        self.inputfile = inputfile
        self.outputfile = outputfile
    
    def parse_one_line(self, line):
        # 子类必须要重写这个函数
        raise NotImplementedError

    def process(self):
        print("Derived process")
        r = self.file_open(self.inputfile, self.outputfile)

        for line in r:
            content = self.parse_one_line(line)
            self.save(content)

        self.file_close()


class Job(TextFileParser):
    def __init__(self, inputfile, outputfile):
        super().__init__(inputfile, outputfile)

    # def parse_one_line(self, line):
    #     print("line -> {}".format(line))
    #     line = line.strip()
    #     content = line + '\t' + "XXXXXXXXXXX1234567890" + "\n"
    #     print("content -> {}".format(content))
    #     return content



if __name__ == '__main__':
    fp = Job(inputfile="1.txt", outputfile="2.txt")
    fp.process(
