'''f = open("txt1.txt","a")
f.write("Thanks for creating me")
f.close()
f = open("txt1.txt")
print(f.read())'''
import os
os.remove("txt1.txt")
