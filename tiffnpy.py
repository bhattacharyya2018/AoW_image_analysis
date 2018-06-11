import numpy 
from PIL import Image 
import os 
import os.path

directory_in_str = '/root/Documents/tiffimages'
directory = os.fsencode(directory_in_str)
#save_path = '/media/root/AYE/tiffnumpyconvert'

for file in os.listdir(directory):
  #print(file)
  filename = os.fsdecode(file)
  #print(filename)
  if filename.endswith(".tiff"):
   im = Image.open('/root/Documents/tiffimages/' + filename)
   f = os.path.splitext(filename)[0]
   imarray = numpy.array(im)
   #print(imarray)
   numpy.save(f,imarray)
   #imarray.save(f + ".npy")
   shapeofnumpy = imarray.shape
   sizeoftiff = im.size
   print("Numpy array shape: ", shapeofnumpy)
   print("Tiff image size: ", sizeoftiff)
