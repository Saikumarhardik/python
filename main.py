import os 

os.system("top -bn 1 > saikumar.txt")

li = []

with open("saikumar.txt","r") as r:
  lines = r.readlines()
  print(lines[2])
  for x in lines[2]:
    print(x)
    
   
  
    
