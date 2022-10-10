import sys

str = sys.argv[1]
str = str.replace("\n","")
str = ' '.join(str.split())
sys.stdout.write(str)