import os 
import sys

input1 = sys.argv[1]
input2 = int(sys.argv[2])

os.system("top -bn 1 > saikumar.txt")

def calculateCPU():
  li = []

  with open("saikumar.txt","r") as r:
    lines = r.readlines()
    y = lines[2].split(',')
    for x in y:
      li.append(x.strip())
    for item in li:
      if item.endswith('id'):
        z= item
    final =  z.split(' ')
    utilized = 100 - float(final[0])

    if utilized > input2:
      print("cpu > threshold")
    else:
      print("cpu < threshold")
  
  
  






if input1 == "cpu":
  calculateCPU() 
  
  

    
  
  
   
  
    
