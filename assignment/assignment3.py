#question 1
class Student:
    name="Himanshu"
    age="20"
    course="cs"
st=Student()
print("name:",st.name)
print("Age:",st.age)
print("Course:",st.course)


#question 2
class Car:
    def __init__(self,model,brand,price):       
        self.model=model
        self.brand=brand
        self.price=price
    def display(self):
        print(f"model:{self.model}\tbrand:{self.brand}\tprice:{self.price}")
car1=Car(model="xyz",brand="abc",price=1000000)
car2=Car(model="asd",brand="wer",price=2000000)
car1.display()
car2.display()



#question 3
class Employee:
    def __init__(self,employee_id,name,salary):       
        self.employee_id=employee_id
        self.name=name
        self.salary=salary
    def display(self):
        print(f"employee_id:{self.employee_id}\tname:{self.name}\tsalary:{self.salary}")
emp1=Employee(employee_id="emp101",name="abc",salary=500000)
emp1.display()


#question 4
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print("area:",self.length*self.width)
rect=Rectangle(10,20)
rect.area()




#question 5
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("area:",2*(22/7)*self.radius)
cir=Circle(10)
cir.area()


#question 6
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def displaybalance(self):
        print("balance:",self.balance)

bk=BankAccount("Himanshu",10000000)
bk.deposit(10000)
bk.displaybalance()
bk.withdraw(2000000)
bk.displaybalance()


#question 7
class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("bark")
dog=Dog()
dog.sound()


#question 8
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self, name, age,roll_no):
        super().__init__(name, age)
        self.roll_no=roll_no
    def display(self):
        print(f"name:{self.name}\tage:{self.age}\trollno:{self.roll_no}")
st=Student("Himanshu",20,33)
st.display()


#question 9
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("Addition:",self.a+self.b)
    def  sub(self):
        print("subtraction:",self.a-self.b)
    def multiplication(self):
        print("Multiplication:",self.a*self.b)
    def division(self):
        print("division:",self.a/self.b)
cal=Calculator(10,20)
cal.add()
cal.sub()
cal.multiplication()
cal.division()


#question 10
class  LibraryBook:
    def __init__(self,book_name,author,price):
        self.book=book_name
        self.author=author
        self.price=price
    def display_book_info(self):
        print("Book:-",self.book)
        print("Author:-",self.author)
        print("Price:-",self.price)

book1=LibraryBook("abc","xyz",499)
book1.display_book_info()
book2=LibraryBook("asd","bcd",899)
book2.display_book_info()
book3=LibraryBook("wer","xyz",1499)
book3.display_book_info()