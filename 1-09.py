# oops object oriented program
# # data security,real world applications.
# # class:#pascl case
# # variables-stores the data & refrs it , methods-hw shud it behave
# # self: is a ref tht youre wrkng on 
# # methods: 
# # class Calculator:
# #     def add(self,a,b):
# #         print(a+b)



# # c1=Calculator() #real entity,obj,multiple objs can b created
# # c2=Calculator()
# # c3=Calculator()
# # c4=Calculator()

# # c1.add(2,3)


# # constructor: is a method tht runs /xecuted automatically during object creation

# class Calculator:
#     company_name="mahindra"
#     def __init__(self,id1,mfg_date1,mrp1):
#         self.id=id1
#         self.mfg_date=mfg_date1
#         self.mrp=mrp1
#     @classmethod
#     def change_company(cls,new_Name):
#         cls.company_name=new_Name  
#     @staticmethod
#     def describe_company():
#         n1=1000
#         print("50 yrs....")
#         print("hsdass")
        
# clc1=Calculator(1,"02-sep",200)
# print(clc1.id,clc1.id,clc1.mrp)

# clc2=Calculator(2,"02-sep",2000)
# print(clc2.id,clc2.id,clc2.mrp)
# only 1 constructor is possible in a class n method overloading is nt possible in python.
# types of variables based on characters 2 types 1.instances 2.class/static variables
# 3 types of methods : 1.instances 2.class 3.static

# variables: instance variables: those variables whose value depends on obj
# class/static :has same value fr all the objects depends on class name 
# cannot access instance variable using clss name 
# yh can access class/static variable using instance 
# can access clas/static variable using main class 


# methods are classsified using variables
# 1.instance method: any mehtod dt hs instance variable in it .
# eg: def describe(self)

# class methods: any method uh use only class or static variables 
# decorators adds additional functionality to yr method
# static methods are used based on utility purpose.
# 
# assignment:create yr own class n use all ;
# decorators: this are the functions that add some more functionality to the method
# def printer():
#     print("printing the required documents")

# printer()     
# decorators creates new function and wraps the existing function and executes new function 

# def example_decorator(func): #

#     def wrapper():
#         print("checking requirement....")
#         func()
#         print("thank you")
#     return wrapper
# @example_decorator
# def printer():
#     print("printing the required documents")

# printer()    
# whn yh copy a code it causes maintainability,bug issue,increases lines of code,

#4 pillars of oops : inheritance,polymorphism,abstraction,encapsulation
# inheritance: is always 1 way

# class Calculator: #parent ,superclass,base class 

#     def add(self,a,b):
#         print(a+b)

#     def sub(self,a,b):
#         print(a-b)

# class AdvCalculator:
    # def add(self,a,b):
    #     print(a+b) instead of this use inherit opt

# class AdvCalculator(Calculator):#child,subclass,derived class 
#     pass


# adv1=AdvCalculator()
# adv1.add()


# types of inheritance:
# single:1 single parent 1 child 
# multilevel: class to subclass to superclass a->b->c
# multiple level: 2 parents single child  inherits from boththe parents
# hierarchial: single parent multiple child classes
# hybrid: mix and match (combinations are prst) lyk multilevel &multiple are prsnt 
# class lion:
#    pass
# class tiger:
#    pass
# clss liger(lion,tiger):
# not only methods bt also variables can b inherited along wid properties eg: static variables
# 
# # 
# # 
# class Vechile:

#     def drive(self):
#         print("vechile in drive mode")
# class Car(Vechile):
    # def brake(self):
        # print("car brakes applied") #if both parent &child hv same method & youre calling it using child class
        # then it frst prints its own class - this method is known as method overridding 
        # instance variables may or may not b inherited based on the code  
# class Teslacar(Car):
#     pass

#     def drive(self):
#         print("car started")    

# v1=Vechile()
# v1.drive()

# c1=Car()
# c1.drive()
# c1.brake()

# elon=Teslacar(Car)
# elon.drive() 
# super().drive() or the function yh want
# to run parent constructor in child class super().__init__(pass all the variables prsnt to print)
# 
# mro can be used in any inheritance
# method resolution order (MRO)
# class Tiger:
#     def hunt(self):
#         print("ntr")

# class Lion:
#     def roar(self):
#         print("balayya")


# class Liger(Lion,Tiger):
#     pass
# lg1=Liger()
# lg1.roar() 
# # or
# print(Liger.mro())
# print(Liger.__mro__)

# polymorphism: same entity acting in dffrnt forms and dffrnt situations
# operator overloading
#method overloading: functions with same name are in same place and they r distinguished by using parameters.
# def add (a,b):
#     return a+b

# def add(a,b,c):
#     return a+b+c
# these are achived using arbituary& karb arguements 
# def add(*a):
#     return sum(a)

# add(2)
# add()
# add(2,4,5).method overloading isnt supported by python bt achived by arb &karb method overiding is possible

#operator overloading :single operator given multiple functions
# evrything in python is an object 
# 2+3= bts: (2).__add__(3)=5 an operator uses a method  n dts known as synthetic sugar
# class Marks:
#     def __init__(self,so_marks,math_marks):
#         self.so_marks=so_marks
#         self.math_marks=math_marks
#     def __add__(self,other):
#         print(self.so_marks+other.so_marks)
#         print(self.math_marks+other.math_marks)


# m1=Marks(20,30)
# m2=Marks(30,40) 
# m1+m2  
# __truediv__ (division)
# __mul__(multiplication)
# __sub__(subtraction)
# __floordiv__(floor division)
# tuck typing : can add or perform any func 2 diffrnt classes
# encapsulation: wraping data into single function or data #data integrity increases
# class user:
#     def __init__(self,username,password,balance):
#         self.username=username
#         self.__password=password
#         self.balance=balance
#     def get_username(self):
#         return self.username
#     def get_password(self):
#         return self.password   
#     def get_balance(self):
#         return self.balance
#     def get_password(self):
#         return self.__password
    
     

# us1=user('vasnatha','jyothi',50000)
# username=us1.get_username()
# print(us1.get_password())
# accesss specifiers: 3 types public,private,protected 
# access specifiers tells wr a particular variable shud b used 
# public : it is universal can b accessed wrevr yh want 
# private: cant access outside the clss def n specified using double (__)
# protected: in btw public & private same as public single(_) can b accessed anywr
# 
# destructor: to dlt an obj
# class user:
#     def __init__(self,username,password,balance):
#         self.username=username
#         self.__password=password
#         self.balance=balance
#         print("obj created")

#     def __del__(self):
#         print("obj is deleted")

#     def __str__(self):
#         return self.username+str(self.balance)  
#     def __len__(self):
#         return 50  



# us1=user('k','p',500)
# us2=user('k','p',500)
# print(us2)

# del us1

# doulbe underscore methods/magic methods/spl methods 
#  helps python inbuilt methods & operations to work on user defined  self constructors



# 
# 

# class Acadclass:
#     def __init__(self):
#         self.student_list=[]
#         print("Acadclass created")
#     def add_students(self,name):
#         self.student_list.append(name) 

#     def __len__(self):
#         return len(self.student_list)  
    

# cls1=Acadclass()  
# cls1.add_students("mahesh")     
# cls1.add_students("vijay") 
# cls1.add_students("suresh")
# cls1.add_students("varun")
# print(cls1.student_list)
# print(len(cls1)
# abstraction:hides implemntn details of methods 
# uses: code modularization,data security,makes code flexible and extensible 
# abstract class & abstract method:
# method: a method dt doesnt hv any implementn
# class: atleast hs one abstract method 
# every abstract class must inherit from abc class
# yh cnnot create an obj fr abstract class 
# abstrct method can hv n number of classess


# from abc import abstractmethod
# import abc

# class ATM (abc):

#     @abstractmethod
#     def debit_money(self,amount):
#         pass 

# atm1=ATM()
# abstrct classess are used to impose structure 

