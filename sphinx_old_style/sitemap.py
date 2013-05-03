import os
import re
import time

dir = './_build/dirhtml/'

print "CACHE MANIFEST"
print "# Version "+time.strftime("%Y-%m-%d")


for dirname, dirnames, filenames in os.walk(dir):
    for subdirname in dirnames:
        #print os.path.join(dirname.replace(dir,''), subdirname)
		pass
    for filename in filenames:
        print os.path.join(dirname.replace(dir,''), filename.replace(dir,''))

