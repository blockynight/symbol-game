# A file for testing that the file_parser.py file runs as expected.

from file_parser import *

storage = {}

parser = Parser("levels/")
parser.parse("test.txt", "r", storage)

print storage["title"]
print storage["text"]
