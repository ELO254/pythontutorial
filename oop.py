class Emobilisstudents:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def hello_me(self):
        print(f"my name is {self.name} and i am {self.age} years old")
    #creating an object
myobj = Emobilisstudents("elvis",18)
myobj.hello_me()
myobj2= Emobilisstudents("JOHN",12)
myobj2.hello_me()
#magari name model year properties
class Cars:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
    def my_cars(self):
        print(self.name,self.model,self.year)
obj = Cars("PREMIO","TOYOTA",2017)
obj.my_cars()
class students:
    def __init__(self,name,id,form):
        self.name = name
        self.id = id
        self.form = form
    def std_info(self):
        print(self.name,self.id,self.form)
st = students("john","11592","form 4")
st.std_info()
