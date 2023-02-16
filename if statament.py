#if statement
x=2
if x>0:
    print("the num is valid")
#if else statement
marks = 200
if marks>=300:
    print("pass")
else:
    print("fail")
#if...else...if....else
grades = 80
if grades<=29 and grades>=0:
    print("you have failed")
elif grades<49 and grades>=30:
    print("you have passed")
elif grades<=79 and grades>=50:
    print("you have done grate")
elif grades<=100 and grades>=80:
    print("distinction")
    exit(grades)
else:
    print("wrong input")
