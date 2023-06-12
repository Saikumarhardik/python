import os 

os.system("top -bn 1 > saikumar.txt")

li = []

with open("saikumar.txt","r") as r:
  lines = r.readlines()
  y = lines[2].split(',')
  print(y)
  
   
  
    
