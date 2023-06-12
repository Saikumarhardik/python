import os 

os.system("top -bn 1 > saikumar.txt")

with open("saikumar.txt","r") as r:
  lines = r.readlines()
  for x in lines[2]:
    y = x.strip().split(',')
    print(y)
    
   
  
    
