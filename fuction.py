'''x=10
print(x)

def my_function(fname):
    print("hello" + fname)

def f1():
    print("Hello F1")
def callMe(a,b):
    print("Hello "+ a +" and")
    print(b)
print("Execution start")
f1()
my_function("Arti")
my_function("10")
f1()
callMe("Pune", 10)
callMe("Pune","Mumbai")
f1()'''
def hello(greeting='hello', name='world'):
    print('{0}, {1} !'.format(greeting, name))
    print(greeting + " " +name)

hello()
hello('hi')
hello('hi','bye')
    
