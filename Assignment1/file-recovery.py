import os
import string

key = open('key.txt').read()
letter = string.ascii_lowercase + string.ascii_uppercase

for file in os.listdir():
   lines = list()
   if file.endswith(".enc"):
       with open(file, "r") as f:
           for line in f:
               lines.append(line)
       with open(file[:-4] + ".txt", "w") as dec:
           for line in lines:
               for char in line:
                   if char in letter:
                       dec.write(letter[key.index(char)])
                   else:
                       dec.write(char)
       os.remove(file)