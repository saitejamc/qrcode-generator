#!/usr/bin/python

import qrcode, sys
content = sys.argv[1]
img = qrcode.make(content)
img.save("./1.png")
print "QR Code generated and saved as 1.png" 

