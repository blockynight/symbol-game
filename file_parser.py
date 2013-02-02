# Parses a text file for the symbol game.

import copy # use deep copy.

class Parser(object):

    def __init__(self, DIR):

        self.DIR = DIR                  # Directory to get files from.
        self.file_data = {}


    def parse(self, FILE, M, storage):       # FILE to be opened, M -mode to use eg 'r'
        
        txt = self.open_file(FILE, M)
        if(None == txt): self.error("No such file exists.")
        self.mk_list(txt, storage)

            
    def open_file(self, FILE, M):            # Handles if the file to open doesn't exist.

        try:
            return open(self.DIR + FILE, M)

        except IOError:
            return None


    def mk_list(self, txt, storage):         # store vars from file in a dictionary

        while True:
            raw_line = self.get_line(txt)
            if(None == raw_line): break

            if("" == raw_line): continue

            else:
                line = raw_line.split()
                self.store(line, storage, txt)
                print storage[line[0])

    def get_line(self, txt):                 # Gets next line of file, handles errors.

        try:
            return txt.readline().strip()

        except EOFError:
            return None


    def store(self, line, storage, txt):
        
        asign = self.find_str(line, "=", 0)
        if (None == asign): self.error("No = char can't read data")

        info = []
        
        du = 0
        print "DEBUG:", txt.tell()
        cut_locate1 = self.find_str(line, '"""', du)
        if (None == cut_locate1): self.error("Nothing to read")

        info.append("".join(line)[cut_locate1 + 1:])
        du += 1
        
        nline = deepcopy(
            
        cut_locate2 = self.find_str(line, '"""', du)
        if (None == cut_locate2):
            while True:
                raw_line = self.get_line(txt)
                if (None == raw_line): self.error("End of File")
                    
                if ("" == raw_line): continue
                line = raw_line.split()

                temp_locate = self.find_str(line, '"""', du)               
                du += 1

                if (None == temp_locate):
                    info.append("".join(line))
                    continue

                cut_locate2 = temp_locate
                break

        info.append("".join(line)[:cutlocate2 + 1])
                    
        storage[line[0]] = "".join(info)


    def find_str(self, line, string, du):

        if string in line:
            return line.index(string, du)

        else:
            return None


    def error(self, message):

        raise Exception(message)
