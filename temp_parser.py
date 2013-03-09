# Making the file_parser from symbol game into a full library

import os

class FileParser(object):

    def __init__(self, rules):
        
        self.rules = rules


    def read_file(self, input_file, storage):

        file_obj = self.setup(input_file, "r", False)
        
        info = self.get_line(file_obj)
        if (None == info): self.error(file_obj, "Reading file failed.")
   
        storage["1"] = info
        file_obj.close()


    def write_file(self, input_file, storage, newfile=False):
        
        if (0 == len(storage)): self.error(None, "Nothing to write.")
            
        file_obj = self.setup(input_file, "r+", newfile)       
        file_obj.close()


    def append_file(self, input_file, append_line ,newfile=False): 

        file_obj = self.setup(input_file, "a", newfile)

        file_obj.close()


    def setup(self, input_file, mode, newfile):
    
        test_exists = self.open_file(input_file, "r")

        if (None == test_exists and True == newfile):
            file_obj = self.open_file(input_file, "w")    
            
            if (None == file_obj): 
                self.error(file_obj, "File failed to be created or other IO error.")

        elif (None == test_exists and False == newfile):
            self.error(file_obj, "File doesn't exist.")

        else:
            test_exists.close()
            file_obj = self.open_file(input_file, mode)
            
            if (None == file_obj): 
                self.error(file_obj, "An IO error, but %s exists." % input_file)

        return file_obj


    def open_file(self, input_file, mode):

        try:
            return open(input_file, mode)

        except IOError:
            return None


    def get_line(self, file_obj):

        try: 
            raw_line = file_obj.next().strip()
            line = self.clean_line(raw_line)
            return line

        except StopIteration:
            return None


    def clean_line(self, raw_line):
        """
        Returns a blank line if the raw_line has no visable 
        alpha numeric characters.
        """

        proving_table = []

        for char in raw_line:
            if (False == char.isalnum): proving_table.append(False)
            else: proving_table.append(True)

        for value in proving_table:
            if (True == value): return raw_line
            
        return ""


    def find_str(self, string, line):
        
        pass


    def error(self, file_obj, message):

        if (None != file_obj): file_obj.close()
        raise Exception(message)


class RulesParser(object):

    def parse_rules(self, rules):    # interpert and apply rules passed to FileParser

        pass


p = FileParser("none")
s = {"a":5}
f = "levels/test3.txt"
p.write_file(f, s, True)
s = {}
p.read_file(f, s)
print s
