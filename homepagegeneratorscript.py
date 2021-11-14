import os
import re

#print(os.listdir("Working and notes"))

p = re.compile('^.+.html$') # html file regex
htm_fil={} # file list dictionary
# html header
main="""<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<link rel="stylesheet" href="styles.css">
	<title>Notes</title>
	
</head>
<body style="background-color:#f2f2d9">
<h1> Index of stylus notes </h1>
"""

for root, dirs, files, in os.walk("./Working and notes"):
    for _d in dirs:
        htm_fil[_d] = []
        for files in os.walk("./Working and notes\/" +_d):
            for f in files:
                if isinstance(f, list) and len(f)>0:
                    for _f in f:
                        if p.match(_f):
                            htm_fil[_d].append(_f)

for key in htm_fil:
    main+="<h2>"+key+"</h2>"
    main+="<ul>"
    #print(list_wrap)
    for file in htm_fil[key]:
        main+="<li><a href=\""+"./Working and notes/"+key+"/"+file+"\">"+file+"</a></li>"
    main+="</ul>"

main+="""
<p style="/*text-align:center*/">🐝</p>
<!-- END -->
</body>
</html>"""

#print("====== test print =======")
print(main)

# Write to file
f=open("index.html", "w", encoding="utf-8")
f.write(main)
f.close()


