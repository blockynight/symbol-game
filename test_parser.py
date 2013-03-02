# A file for testing that the file_parser.py file runs as expected.

from file_parser import *
import sys                   # Test options -f for full, -i for individual func tests.


def print_list(items):

    for item in items:
        print item


if 1 == len(sys.argv): 
    print "USAGE: Script [Options] eg -f or -i"
    sys.exit(1)

storage = {}
fili = "levels/test.txt"
m = "r"
storage = {}
p = Parser()

if "-f" == sys.argv[1]:

    p.parse(fili, m, storage)

    print storage["title"]
    print storage["text"]
    print storage

   # print "\n\n"


#======================================================#
# Testing individual functions.

elif "-i" == sys.argv[1]:
    
    # cut_line
    try:
        f = p.open_file(fili, m)
        l = p.get_line(f)
        ls = l[2:]
        ln = p.cut_line(" ".join(ls), '"""')
        ln2 = p.cut_line(ln, '"""')
        storage[l[0]] = ln2
        f.close()

        print "cut_line [True]"

    except:
        print_list(["cut_line [False]", f, l, ls, ln, ln2, storage])

    print ""

    # find_string 
    try:
        f = p.open_file(fili, m)
        l = p.get_line(f)
        ls = l[2:]
        ln = p.find_string(" ".join(ls), '"""', True)
        ln2 = p.find_string(ln, '"""', True)
        storage[l[0]] = ln2
        f.close()

        print "find_string [True]"

    except:
        print_list(["find_string [False]", f, l, ls, ln, ln2, storage])

    print ""

    # Find_set
    try:
        f = open_file(fili, m)
        l = p.get_line(f)
        ls = l[2:]
        ln = p.find_set(f, ls, '"""')
        storage[l[0]] = ln
        f.close()

        print "find_set [True]"

    except:
        print_list(["find_set [False]", f, l, ls, ln, ln2, storage])
        error_info = sys.exc_info()
        print error_info[0]
        print error_info[1]
