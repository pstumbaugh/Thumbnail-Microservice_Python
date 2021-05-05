# MAIN:

import ssl
import urllib.request as urlrq
from urllib.request import urlretrieve
import certifi
from PIL import Image

# get the image location and save it as RGB
img = Image.open(r"/Users/pstumbaugh/Desktop/bear.jpg")


url = "https://www.sciencenewsforstudents.org/wp-content/uploads/2021/04/1440_bb_brown_black_bear_explainer_feat.jpg"

resp = urlrq.urlopen(url,
                     context=ssl.create_default_context(cafile=certifi.where()))

newImg = Image.open(resp)
newImg.save("newURLimage.jpg")

basewidth = 300

wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))

img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save('thumbnailImage.jpg')
print("DONE")
