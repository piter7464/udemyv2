import os
import time

print('Current directory:', os.getcwd())

currentdir = os.getcwd()
filename = 'results.txt'
fullpath = os.path.join(currentdir, filename)
print('Structured file path is:', fullpath)

relativepath = 'output.txt'

print('The absolute path is:', os.path.abspath(relativepath))

filepath = r'C:\Users\pgrac\PycharmProjects\udemyv2\results.txt'
print('The file name part is', os.path.basename(filepath))
print('The directory part is', os.path.dirname(filepath))

print('is file existing?', os.path.exists(filepath))

if os.path.exists(filepath):
    print('last modify date is:', os.path.getmtime(filepath))
    print('last modify time is',  time.localtime(os.path.getmtime(filepath)))

    print('file size is:', os.path.getsize(filepath))

    print('is it a file?', os.path.isfile(filepath))

    print('is it dir?', os.path.isdir(filepath))

    print('path splitted', os.path.split(filepath))

