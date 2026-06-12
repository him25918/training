# Question 1
Tup1 = (10, 20, 30, 40, 50) 
print(f"First Element = {Tup1[0]} ")
print(f"First Element = {Tup1[len(Tup1)-1]} ")
print(f"Length of Tuple = {len(Tup1)}")
print(Tup1[1:4])



# Question 2
fruits = ("apple", "banana", "mango", "orange")
print(f"Second Fruit = {fruits[1]} ")

n = len(fruits)-2
print("Last 2 Fruits : ", fruits[n:len(fruits)])

print(f"Total Number of Fruits = {len(fruits)}")



# Question 3
numbers = {10, 20, 30, 40, 50}
print(f"Set = {numbers}")

print(f"Length = {len(numbers)}")

if(30 in numbers):
    print("30 is Present")
else:
    print("30 is Not Present")



# Question 4
set1 = {1, 2, 3, 4} 
set2 = {3, 4, 5, 6} 

print(f"Union = {set1.union(set2)}")
print(f"Intersection = {set1.intersection(set2)}")



# Question 5
student = {"name":"Kriti", "age":20, "course":"Python"}
print(student)
print(f"Name = {student['name']}")
print(f"Age = {student['age']}")

numbers = [12, 45, 7, 23, 56, 89, 34]
print(f"Smallest = {min(numbers)}")
print(f"Largest = {max(numbers)}")
largest = max(numbers)
second_max = -1

for i in numbers:
    if(i>second_max and i!=largest):
        second_max = i

print(f"Second Largest = {second_max}")



# Question 6
def Rev(lst:list)->list:
    return lst[::-1]
    
arr1 = [10, 20, 30, 40, 50, 60]
arr2 = Rev(arr1)
print(arr2)



# Question 7
data = (5, 10, 15, 20, 25, 30, 35)
count = 0
sum = 0
for i in data:
    if(i%5 == 0): count +=1
    sum += i

print(f"Number of elements are divisible by 5 = {count} ")
print(f"Sum of Elements = {sum}")
print(f"Average of Tuple = {sum / len(data)}")



# Question 8
students = { 
    "Aman": 78, 
    "Riya": 92, 
    "Kriti": 88, 
    "Rahul": 95 
} 

Max_marks = max(students.values())
print(Max_marks)
names = []

Max_marks = max(students.values())
Min_marks = min(students.values())

for i in students.keys():
    if(students[i] == Max_marks):
        Max_stu = i
    if(students[i] == Min_marks):
       Min_stu = i
    if(students[i]>85):
        names.append(i)
       

print(f"Student with Highest = {Max_stu}")
print(f"Student with Lowest = {Min_stu}")

print(names)



# Question 9
def freq(lst:list):
    Set1 = set(lst)

    for i in Set1:
        print(f"{i} -> {lst.count(i)} times")

arr = [1, 2, 2, 3, 1, 4, 2] 
freq(arr)



# Question 10
def Find_Duplicates(lst:list):
    Set1 = set(lst)

    for i in Set1:
        if(lst.count(i)>1):
            print(i)

arr = [10, 20, 30, 20, 40, 10, 50, 30] 
Find_Duplicates(arr)