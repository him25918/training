# name = "abc"
# print("this is the string ", name)
# print(type(name))
# print(len(name))

# temp = "45 days training"
# print(temp[3:7])
# print(temp[::-1])
# print(temp.upper())

# address = "pilani"
# # print(address.lower())
# # print(address.upper())
# print(address.title()) # makes first letter capital 
# #capitalize() also works the same it makes every first letter of word capital

# name = "onngtnintnietinh"
# print(name.count('n'))
# print(name.index('n'))
# print(name.find('n'))
# split function


# intro = "i love python"
# print(intro.replace("python","java"))
# print(intro)

# a = "python"
# print(a.startswith("p"))
# print(a.endswith("p"))

num = "124"
char = "hello"
a="hello123  "
# print(num.isdigit())
# print(char.isdigit())
# print(char.isalpha())
# print(char.isalnum())
# print(char*3)
# print(char+char)
# print(a.strip())

# name = "himanshu"
# add = "pilani"
# print(f"My name is {name} and i am from {add}") # formatting k liye string k aage f likhte hai




# list == collection of heterogenous item , mutable, ordered

# lst = [1,2,3,"abc",6.89]
# print(lst)
# print(type(lst))
# print(lst[2:5])
# lst.append(5)
# lst.insert(0,100)
# lst.insert(1,"pilani")

# lst.extend([1,2,3,4])
# lst.append([1,2,3,4])
# print(lst)
# print(lst[5][1])
# lst1 = lst
# lst2 = lst.copy()
# print(lst1)
# print(lst2)
# print(lst==lst1)
# print(lst==lst2)
# print(lst1 == lst2)

# lst1 = [1,2,4,5]
# lst2 = [3,4,5,6]
# print(lst1+lst2)
# print(lst1*2)
# print(lst1*lst2)
# print(lst1/lst2)
# print(lst1//lst2)

# dict1 = {
#     "name" : "himanshu",
#     "roll" : 67,
#     "age" : 20
# }

# tup = (1,2,3,4,1,3)
# set1 = {1,2,3,3,4,1}
# print(set1)
# print(type(set1))
# print(tup)
# print(type(tup))
# print(dict1)
# print(type(dict1))
# a=5
# b=5.4
# c=5+3j
# d = False
# print(len(a) + len(b) + len(c) + len(d))

# i = "AIML"
# j = "AIDS"
# k=i/j
# l=i//j
# print(k)
# print(l)

# a=1
# b=1
# c=-1
# if(a and b):
#     print("hello")
#     if(b and c):
#         print("hi")
#     else:
#         print("hey")
# else:
#     print("bye")

# for i in range(1,11):
#     print(i)

# student = {
#      "name" : "Himanshu",
#      "age" : 20,
#      "branch" : "cse"
# }
# # print(student.get("branch"))
# # print(student["branch"])
# student["age"] = 22
# # print(student)

# student["phone"] = 8903745278
# # print(student.keys())
# # print(student.values())
# # print(student.items())
# for key,value in student.items():
#     print(key,value)


# students = {
#     "rahul" : {
#         "age" : 20,
#         "branch" : "cse"
#     },
#     "himanshu" : {
#         "age" : 20,
#         "branch" : "cse"
#     }
# }
# print(students["himanshu"]["branch"])

# def greet(name):
#     print("Good morning " + name)
# greet("himanshu")
# greet("rahul")
# greet("mohit")
# lst = ["A","b","c","d","e","f"]
# for i in lst:
#     greet(i)

# square = lambda x : x*x
# print(square(5))

# tuple == immutable and heterogenous in nature, created with () and allows duplicates

# tp1 = (1,2,3,3,"hi")
# print(tp1)
# print(len(tp1))
# print(type(tp1))
# print(tp1.count(3))
# print(tp1.index("hi"))



# >>>>>>>>>>>>>>>>>>>>>>> tuple collection >>>>>>>>>>>>>>>>>>>>>>
# a = 1,2,3,3,3,4,5,"hii"   
# print(a)
# print(type(a))
# print(len(a))

# by default python assumes this collection as tuple


# >>>>>>>>>>>>>>>>>>>>>>>..tuple unpacking>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# a,b,c = (1,2,3)
# print(a)
# print(b)
# print(c)

# if the number of variables is less than the items in tuple it will show error


# tp3 = (1,2,3)
# tp4 = (2,4,6)
# print(tp3*tp4)  >>>>>>>  gives error canot multiple sequence with sequence 
# print(tp3*2)   >>>>>>  (1, 2, 3, 1, 2, 3)



# >>>>>>>>>>>>>>>>>>>>>>>>>type casting>>>>>>>>>>>>>>>>
# print(tp3)
# ls = list(tp3)
# ls.append(4)
# tp3 = tuple(ls)
# print(tp3)




# >>>>>>>>>>>>>>>>>>>>>>>>>>>dictionary>>>>>>>>>>>>>>>>>>>>>
# student = {
#     "name" : "Himanshu",
#     "roll" : "23Ebkcs 045",
#     "phone" : "7893778492",
#     "college" : "bkbiet"
# }
# print(student)
# print(type(student))
# print(student["college"])
# print(student["roll"])


# print(student.get("name"))  
# if key present then gives value else none no error 

# update
# deepcopy reseaerch
# copy
# setdefault

# a = student.pop("roll")

# print(a)
# print(student)

# print(student.popitem())
# print(student)
# student.update({"roll" : "78"})
# print(student)

# key = input("Enter key : ")
# print(student.get(key))

# if we take two key with same name the last will overwrite the other



# >>>>>>>>>>>>>>>>> set >>>>>>>>>>>>>>>>>>>>>>>>
# do not allow duplicate 
# unordered 
# heterogenous
sat = {1,2,3,3,"hi","hello"}
# print(sat)
# print(type(sat))
# print(len(sat))
# sat.add(5)
# print(sat)

# sat1 = {1,2,3,4}
# sat2 = {3,4,5,6}
# print(sat1.difference(sat2))
# print(sat2.difference(sat1))
# print(sat1.intersection(sat2))
# print(sat1.symmetric_difference(sat2))
# print(sat2.symmetric_difference(sat1))

sat.remove(3);
print(sat)
# removes if present or give error if value not there

sat.discard("helloo")
# do not give error if value not present
print(sat)
