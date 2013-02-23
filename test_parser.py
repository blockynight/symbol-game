# A file for testing that the file_parser.py file runs as expected.

from file_parser import *
import sys 

storage = {}
fili = "levels/test.txt"
m = "r"
storage = {}
p = Parser()
p.parse(fili, m, storage)

print storage["title"]
print storage["text"]
print storage



#======================================================#
# Testing individual functions.

print "\n\n"

# Cut_line
f = p.open_file(fili, m)
l = p.get_line(f)
print l
ls = l[2:]
ln = p.cut_line(" ".join(ls), '"""')
print ln
ln2 = p.cut_line(ln, '"""')
print ln2
storage[l[0]] = ln2
print storage                              # cut_line func works.

print ""

# Find_string 
f.seek(0, 0)
l = p.get_line(f)
print l
ls = l[2:]
ln = p.find_string(" ".join(ls), '"""', True)
print ln
ln2 = p.find_string(ln, '"""', True)
print ln2
storage[l[0]] = ln2
print storage                              # find_string func works.

print ""

# Find_set
f.seek(0, 0)
l = p.get_line(f)
print l
ls = l[2:]
ln = p.find_set(f, ls, '"""')
print ln
storage[l[0]] = ln
print storage                              # find_set func works
