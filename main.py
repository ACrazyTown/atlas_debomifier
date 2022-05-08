import os, time
from glob import glob

inputLoop = True
path = ""

while inputLoop:
    path = input("Path to atlas folder: ")
    if os.path.exists(path):
        inputLoop = False

os.chdir(path)
filesToEncode = glob("./*.json")

for file in filesToEncode:
    bomData = ""
    
    with open(file, "r", encoding="utf-8-sig") as f:
        bomData = f.read()

    with open(file, "w", encoding="utf-8") as f:
              f.write(bomData)

print("Encoded atlas files to not use BOM!")
print("Thanks for using this lil' tool :) Exiting in 5 seconds")
print("-A Crazy Town")
time.sleep(5)
exit(0)
        
