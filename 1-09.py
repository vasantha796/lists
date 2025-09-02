# oops object oriented program
# data security,real world applications.
# class:#pascl case
# variables-stores the data & refrs it , methods-hw shud it behave
# self: is a ref tht youre wrkng on 
# methods: 
# class Calculator:
#     def add(self,a,b):
#         print(a+b)



# c1=Calculator() #real entity,obj,multiple objs can b created
# c2=Calculator()
# c3=Calculator()
# c4=Calculator()

# c1.add(2,3)


# constructor: is a method tht runs /xecuted automatically during object creation

class Calculator:
    company_name="mahindra"
    def __init__(self,id1,mfg_date1,mrp1):
        self.id=id1
        self.mfg_date=mfg_date1
        self.mrp=mrp1
    @classmethod
    def change_company(cls,new_Name):
        cls.company_name=new_Name  
    @staticmethod
    def describe_company():
        n1=1000
        print("50 yrs....")
        print("hsdass")
        
clc1=Calculator(1,"02-sep",200)
print(clc1.id,clc1.id,clc1.mrp)

clc2=Calculator(2,"02-sep",2000)
print(clc2.id,clc2.id,clc2.mrp)
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


