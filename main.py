import os 

os.system("top > saikumar.txt")

withopen("saikumar.txt","r") as r:
  lines = r.readlines()
  for x in lines:
    print(x)
  
    
