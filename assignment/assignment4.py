# question 1
lst = [2,4,5,6,7,8,9,11,56]
for i in lst:
    isPrime = True
    for j in range(2,i):
        if i%j==0 :
            isPrime = False
    if isPrime:
        print(i)

# question 2

for i in range(1,11):
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")

# question 3
def fun1(lst:list):
    sum=0
    count=0
    for i in lst:
        if(i%2==0):
            count+=1
        else:
            sum+=i
    print(f"The count of even numbers is {count}")
    print(f"The sum of odd numbers is {sum}")

# question 4
def simpleInterest(p,r=10,t=1):
    return (p*r*t)/100

si1 = simpleInterest(670000) # calling with default argument
si2 = simpleInterest(100000,12,2)  # calling with positional arguments
si3 = simpleInterest(p=100000,r=13,t=3)  # calling with keyword argument
print(si1)
print(si2)
print(si3)



# question 5
class Student:
    name = None
    marks = None

    def __init__(self,n:str,m:list):
        self.name = n
        self.marks = m
    
    def display(self):
        print(self.name)
        print(self.marks)
    def showGrade(self):
        tot = 0
        count = 0
        for i in self.marks:
            count+=1
            tot+=i
        tot/=count
        if tot > 90:
            print("A grade")
        elif tot > 75:
            print("B grade")
        elif tot > 60:
            print("C grade")
        elif tot > 40:
            print("D grade")
        elif tot > 33:
            print("E grade")
        else : 
            print("Fail")


# question 6
st = Student("Himanshu",[90,40,50,80])
st.display()
st.showGrade()

st2 = Student("Anuj",[80,90,75,78])
st2.display()
st2.showGrade()

#question 7
class BankAccount:
    
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if amount>self.__balance:
            print("insufficent balance")
        else:
            self.__balance-=amount
    def displaybalance(self):
        print("balance:",self.__balance)
a=BankAccount("abc",100000)
a.deposit(1000)
a.displaybalance()


#question 8
try:
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    print("Division:",a/b)
except ZeroDivisionError as e:
    print("error:",e)
except ValueError as e:
    print("error:",e)

# question 9
file=open("student","a")
file.write("name:Hitesh\tmarks:90")
file.close()
file=open("student","r")
print(file.read())
file.close()

#question 10
total = 0
count = 0
try:
    with open("data", "r") as file:
        for line in file:
            number = float(line.strip())
            total += number
            count += 1
    
    if count > 0:
        average = total / count
        print("Total =", total)
        print("Average =", average)
except FileNotFoundError as e:
    print("error:",e)