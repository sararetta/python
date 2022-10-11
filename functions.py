import math
import random


# print(math)
# print(math.sqrt(4))
# print(math.pow(3,2));
# print(math.pi)
# print(math.floor(random.random()*3))
# x=random.randint(5, 10)
# print(x)
# t = [1, 2, 3]
# print(random.choice(t))
# print(int(False))

# def saraa():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all night and I work all day.')

# saraa()
# def elsa():
#     print('elsa retta')
# xx=elsa();

#  if function doesnot return a value and we assign it it produce a none value
# print(xx)


# def addTwo(a,b):
#     x=a+b
#     return x
# q=addTwo(2,3)
# print(q)

def computegrade(score):
    x='';
    if(score>90):
        x='prefect'
    elif(score>80):
        x='excellent'
    elif(score>70):
        x='good'
    else:
        x='fail'
    return x

value=''
try:
    value=int(input('Enter a value'));
    print(computegrade(int(value)))
    
except:
    if isinstance(value, str):
        value=int(input('please enter the value in number'))
        print(computegrade(int(value)))


# def na(a,b):
#     return a + b
# def qq(a):
#     print(a)
#     return na(a,' retta')

# x=qq('sara')
# print(x)







        