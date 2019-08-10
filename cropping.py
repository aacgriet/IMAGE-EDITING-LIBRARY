import  matplotlib.image  as  img 
 import numpy as npy 
  m = img.imread("taj.png") 
  w, h = m.shape[:2] 
 xnew = int(w * 1 / 4) 
 ynew = int(h * 1 / 4)
 newimage = npy.zeros([xNew, yNew, 4]) 
print(w) 
 print(h) 
  for i in range(1, xNew):  
 for j in range(1, yNew): 
       
       newimage[i, j]= m[100 + i, 100 + j] 
  
img.imsave('cropped.png', newimage)
