# A class for parsing text files, must add write ability to store things.

class Parser(object):


    def parse(self, FILE, M, storage):    # FILE path to file to be parsed.
                                          # M mode to use when opening file.
        txt = self.open_file(FILE, M)     # storage must be a dictionary.
        if (None == txt): self.error(txt, "No such file exists.")

        while True:
            
            print "DEBUG: loop1"
            line = self.get_line(txt)
            if (None == line): break
            if ("" == line): continue
            if ("#" == line[0]): continue    # ignore comments
            if ("=" != line[1]): self.error(txt, "No asignment possible.")

            name = line[0]

            if ('"""' in line[2]):
                info = self.find_set(txt, line[2:], '"""')
                storage[name] = info

            elif ('/' in line[2]):
                info = self.find_set(txt, line, '/')
                storage[name] = info

            else:
                self.error(txt, "Nothing to store.")

            print "DEBUG2: %s" % info

        txt.close()


    def open_file(self, FILE, M):

        try:
            return open(FILE, M)

        except IOError:
            return None

        
    def get_line(self, txt):    # Reads a line from the file object passed to it
                                # and checks for errors and returns the line as a list.
        try:
            raw_line = txt.next().strip()
            line = self.clean_line(raw_line)
            return line 

        except StopIteration:
            return None 


    def clean_line(self, raw_line):    # Used to determine wheather a line has any 
                                       # visable chars in it, if theres even one in it
        proving_table = []             # the whole line is returned as a list.

        for char in raw_line:
            if (False == char.isalnum()): proving_table.append(False)
            else: proving_table.append(True)

        for value in proving_table:                       # If all values in proving_table
            if (True == value): return raw_line.split()   # are false, the line has
                                                          # no visable chars in it. 
        return ""


    def find_set(self, txt, line, string):    # Find the locations of a set eg """ to """
                                              # and return all thats between them.
        temp_storage = []
        print "DEBUG3: Got Here"
        stage1 = self.find_string(" ".join(line), string, True)
        if (None == stage1): self.error(txt, "%s isn't there." % string)
        print "DEBUG: STAGE1:", stage1

        stage2 = self.find_string(stage1, string, True)
        print "DEBUG: STAGE2:", stage2
        if (None == stage2):
            temp_storage.append(stage1)

            while True:
                print "DEBUG: looping here or?"
                nline = self.get_line(txt)
                if (None == nline): self.error(txt, "Second %s doesn't exist." % string)
                if ("" == nline): continue

                stage2 = self.find_string(" ".join(nline), string, True)
                if (None == stage2):
                    temp_storage.append("\n" + " ".join(nline))    # Makes sure that the final string
                    continue                                       # created is correctly formated

                else: 
                    print "DEBUG: STAGE2.2:", nline, stage2
                    temp_storage.append("\n" + stage2)
                    print temp_storage                     # debug
                    break

        else:
            temp_storage.append(stage2)

        print "DEBUG4: %s" % " ".join(temp_storage)
        return " ".join(temp_storage)


    def find_string(self, line, string, cut=False):   # line should be a string never list.

        if string in line:

            if (True == cut): return self.cut_line(line, string)
            else: return line.index(string)

        else:
            return None


    def cut_line(self, line, string):
 
        lenstr = len(string)
        linedex = line.index(string)
        print "DEBUG", line
        if (string == line[:linedex + lenstr]): 
            print line[linedex + lenstr:]                # debug.
            return line[linedex + lenstr:]
        else:
            print line[:linedex]                   # debug
            return line[:linedex]


    def error(self, txt, message):

        txt.close()
        raise  Exception(message)
            
            
