import os 

os.system("top -bn 1 > saikumar.txt")

li = []

with open("saikumar.txt","r") as r:
  lines = r.readlines()
  for x in lines[2]:
    li.append(x)
print(li)
    
   
  
    
