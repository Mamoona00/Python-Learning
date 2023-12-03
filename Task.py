# Intro of python (simple example)
a = 33
b = 100
if b > a:
    print("b is greater than a")
# Python 3 basics
# Variable
x = 3
print(x)
# Datatypes (string example)
name = "Moon"
print(name)
#operators (+ operator)
a = 20
b = 30
print(a+b)
#functions
def welcome():
   print ("Hello World")
welcome()
#input and output
print("I am a cute girl")
input('Enter your name: ')
#keywords (if and else example)
if 20>10:
    print("True")
else:
    print("Flase")

#import
import keyword
print("The List of all keywords is: ")
print(keyword.kwlist)

# True, False, and, or, not, in, if, else

print(not True)
print(False and True)
print(False or True)
print(True and True)
print(False or False)
if 'm' in 'mamoona':
    print("yes ")
else:
    print("no")

#namespace
name = "moon"      #name is a global namespace

def mamoona():     #mamoona is a local namespace
    mamoona = 7
    print(mamoona)
    mamoona()
print(name)





#single line comment
#My Name is Mamooa

"""I am a girls
i am a student of BSCS
i am an artist"""



