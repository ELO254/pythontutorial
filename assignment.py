intro = "this are the fruits we have:"
print(intro)
fr = ["carrots","avocado","mangoes"]
for fruits in fr:
    print(fruits)
carrots = 30
avocado = 40
mangoes = 20
fruit = input("which friut do you want :")
num = int(input("enter number of fruit :"))
if fruit == "carrots":
    print("this is the price:")
    cr = num*carrots
    print(cr)
elif fruit == "avocado":
    print("this is the price:")
    av = avocado*num
    print(av)
elif fruit == "mangoes":
    print("this is the price:")
    mg = mangoes*num
    print(mg)
else:
    print("we do not have that kind of fruit")
int2 = "this are the method of payment:"
print(int2)
method = ("credit card","mpesa","cash")
for methods in method:
    print(methods)
method2 = str(input("in which way do you want to pay :"))
if method2 == "credit card":
    amt1 = int(input("enter amount"))
    credit = input("enter your credit num")
    pin = int(input("enter pin number"))
elif method2 == "mpesa":
    amt2 = int(input("enter amount"))
    pin2 = int(input("enter pin"))
elif method2 == "cash":
    print("make payments now")
else:
    print("we do not have that kind of payment")
print("your payment is being processed......")
print("thank you for your service")