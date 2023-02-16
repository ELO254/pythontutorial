def hello():
    print("this is my first function")
hello()
def calculate():
    x = 34
    y = 56
    print(x+y)
calculate()
def name(first,last):
    print(first+" "+last)
name("elvis","odhiambo")
name("john","black")
name("bruno","balack")
def greetings(name,greeting="hello"):
   print(greeting + " " + name)
greetings("elvis")
def courses(course,period = "4 months"):
    print(course+":"+period)
courses("full stack")
courses("android development")
courses("robotics")
def maxvalue(a,b,c,d,e,f):
    return max(a,b,c,d,e,f)
result=maxvalue(3,4,5,6,8,9)
print(result)
def minvalue(a,b,c,d,e):
    return min(a,b,c,d,e)
result=minvalue(11,33,45,56,43)
print(result)
def sort_list(list):
    return sorted(list)
answer = sort_list([1,34,56,78,98,45])
print(answer)
def numlist(n):
    for i in range(n):
        print(i)
numlist(12)