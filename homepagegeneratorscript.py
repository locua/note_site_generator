import os
import re


print(os.listdir("Working and notes"))

p = re.compile('^.+.html')

html_files=[]

for root, dirs, files, in os.walk(".\Working and notes"):
    for _d in dirs:
        for files in os.walk(".\Working and notes\/" +_d):
            for f in files:
                if isinstance(f, list) and len(f)>0:
                    for _f in f:
                        if p.match(_f):
                            #print(_f)
                            html_files.append(_f)
                
print(html_files)
