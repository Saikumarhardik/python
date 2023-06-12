import os 

os.system("top > saikumar.txt")

with open("saikumar.txt","r") as r:
  lines = r.readlines()
  for x in lines:
    print(x)
  
    
