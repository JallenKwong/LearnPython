
#from: https://stackoverflow.com/questions/10607468/how-to-reduce-the-image-file-size-using-pil

import os
from PIL import Image

mainFolderName = "03"

targetFolderName = mainFolderName + "/after"

if not os.path.exists(targetFolderName):
    os.makedirs(targetFolderName)

for item in os.listdir(mainFolderName):
    if item.endswith('jpg'):
        img = Image.open("%s/%s"%(mainFolderName,item))
        img = img.convert("RGB")
        img.save("%s/%s"%(targetFolderName,item),optimize=True,quality=30)

