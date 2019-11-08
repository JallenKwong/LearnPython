# -*- coding: utf-8 -*


# Prepend line to beginning of a file
# from: https://stackoverflow.com/questions/5914627/prepend-line-to-beginning-of-a-file

import datetime

now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

content = "hello at %s\n" % now
print content

def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

line_prepender("hello.txt", content)
