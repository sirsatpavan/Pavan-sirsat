b = "hello, world"
   # 01234567891011
    #length = 12
print(b[1]) #e

print(b[1:4]) #ell

print(b.replace("h", "p")) #pello, world

arr = b.split("l")
#converts single value into multiple value
#converts scalar variable into array variable
print(arr)              #['he', '', 'o,wor','d']

x = b.find("or") #8
print(x)

print("p" in "apple") #true
print("p" not in "apple") #false since it is present

s2 = ("Hello i am {0} and i am {1} year old".format("pavan", 25))
print(s2)
