import os 

os.system("top -bn 1 > saikumar.txt")

li = []

with open("saikumar.txt","r") as r:
  lines = r.readlines()
  y = lines[2].split(',')
  for x in y:
    li.append(x.strip())
  for item in li:
    if item.endswith('id'):
      print(item)
    
  
  
   
  
    
