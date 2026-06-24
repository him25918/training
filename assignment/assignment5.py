# Section A - Numpy

'''
Q1. Create a 1D NumPy array of 20 random integers between 1 and 100. 
Find the minimum, maximum, mean, and standard deviation without 
using Python built-in functions — use only NumPy aggregation 
functions. 
'''

import numpy as np
import random

arr = []

for i in range(20):
    arr.append(random.randint(1,100))

arr = np.array(arr)

print(f"Minimum Value : {arr.min()}")
print(f"Maximum Value : {arr.max()}")
print(f"Mean Value : {arr.mean()}")
print(f"Standard Deviation : {arr.std()}")


'''
Q2. Create a 4x4 matrix using NumPy. Perform the following operations:  
• Extract the diagonal elements 
• Replace all even numbers with 0 
• Find the index of the maximum value using argmax() 
'''

# Both Right & Left Diagonal
arr = np.arange(1,17).reshape(4,4)
Diagonal_ele = []

for i,j in zip(range(4),range(3,-1,-1)):
    if(i==j): Diagonal_ele.append(arr[i,j])
    else:
        Diagonal_ele.append(arr[i,i])
        Diagonal_ele.append(arr[i,j])
        
print(f"Diagonal Elements : {np.array(Diagonal_ele)}")


# Replace even numbers with 0
arr[arr % 2 == 0] = 0
print(f"Array After Replacement :\n {arr}")


# Find index of maximum value
print(f"Index of maximum value: {np.argmax(arr)}")


'''
Q3. Write a program to create two 3x3 NumPy arrays and perform 
element-wise addition, subtraction, and matrix multiplication. Display 
results with proper labels
'''

arr1 = np.arange(1,10).reshape(3,3)
arr2 = np.arange(11,20).reshape(3,3)

print(f"Array1 = \n {arr1}")
print(f"\n Array2 = \n {arr2}")

print(f"\nAddition = \n {arr1+arr2}")
print(f"\nSubtraction = \n {arr1-arr2}")
print(f"\nMultiplication = \n {arr1*arr2}")


'''
Q4. Using np.linspace() and np.zeros() and np.ones(), create three different 
arrays and stack them vertically using np.vstack(). Display the final 
stacked array.
'''

arr1 = np.zeros(5)
arr2 = np.ones(5)
arr3 = np.linspace(1,10,5)

arr4 = np.vstack((arr1,arr2,arr3))
print(f"Stacked Array = \n{arr4}")


# Section B - Pandas

'''
Q5. 5. Create a DataFrame of at least 10 students with columns: Name, Age, 
Marks, City. Perform the following:  
• Display the first 5 rows using head() 
• Show basic statistics using describe() 
• Filter students who scored more than 75 marks 
• Sort by Marks in descending order 
'''
import pandas as pd

Data = pd.DataFrame(
    {
        "Name" : ["Amit","Akash","Akshat","Kartik","Kunal","Khushal","Priya","Pushpa","Sonu","Sumit"],
        "Age" : [20,21,20,22,23,20,21,22,25,28],
        "Marks" : [90,81,75,55,41,90,21,70,33,50],
        "City" : ["Jaipur","Mumbai","Bengaluru","Kanpur","Bihar","Varanasi","Jaipur","chennai","Bengal","Raachi"]
    },
    index=[x for x in range(1,11)]
)

print(f"First 5 Rows = \n{Data.head()}")
print(f"\nBasic Statistics = \n{Data.describe()}")

print("\nStudents with Marks>75")
print(Data[Data['Marks']>75])

print("\nData Sorted By Marks Obtained")
print(Data.sort_values('Marks',ascending=False))


'''
Q6. Create a DataFrame with some missing values intentionally placed in the 
Marks and City columns. Then:  
• Identify missing values using isnull() 
• Fill missing marks with the column mean using fillna() 
• Drop rows where City is missing using dropna() 
'''

Data1 = Data.copy()


Data1.loc[4,"Marks"] = np.nan
Data1.loc[7,"Marks"] = np.nan

Data1.loc[3,"City"] = np.nan
Data1.loc[10,"City"] = np.nan

print(f"NULL Presence in Cols = \n{Data1.isnull().sum()}")
print()

# Filling NULL Values of Marks Column with mean
Data1["Marks"] = Data1['Marks'].fillna(Data1["Marks"].mean())

# Dropping Rows with NULL Values
Data1.dropna()


'''
Q7. Read a CSV file (you may create it manually) containing product sales 
data with columns: Product, Category, Sales, Region. Perform:  
• Group by Category and calculate total Sales using groupby() and agg() 
• Find the top 3 products by sales using sort_values() and head() 
'''

Data = pd.read_csv("Product_Sales.csv")
group1 = Data.groupby("Category")["Sales"].agg(Total_Sales = "sum")

print(group1)

Data.sort_values("Sales").head(3)


'''
Q8. Merge two DataFrames:  
• DataFrame 1: StudentID, Name, Department 
• DataFrame 2: StudentID, Marks, Grade 
• Merge on StudentID and display students who scored Grade 'A' '''

df1 = pd.DataFrame(
    {
        "StudentID": [101, 102, 103, 104],
        "Name": ["Ankit", "Rahul", "Priya", "Aman"],
        "Department": ["CSE", "IT", "ECE", "CSE"]
    }
)

df2 = pd.DataFrame(
    {
        "StudentID": [101, 102, 103, 104],
        "Marks": [95, 78, 88, 92],
        "Grade": ["A", "B", "A", "A"]
    }
)

print("Students Who Scored'A' ")
Merge = pd.merge(df1, df2, on="StudentID")
result = Merge[Merge["Grade"] == "A"]

print(result)


# Section C - Data Visulization

'''
Q9. Using Matplotlib, create the following plots from a student marks 
dataset (create the dataset yourself):  
• A line plot showing marks trend across 5 subjects 
• A bar chart comparing marks of 5 students 
• Add proper title, xlabel, ylabel, legend, and grid to both plots 
'''

import matplotlib.pyplot as plt

# Line Plot
Stu = pd.DataFrame(
    {
        "Subject" : ["English","Hindi","Maths","Science","Music"],
        "Marks" : [80,72,99,41,33]
    }
)
plt.plot(Stu["Subject"],Stu["Marks"],label = "Marks")
plt.title("Marks Trend Across 5 Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid()
plt.legend()
plt.show()


# Bar Chart
Stu2 = pd.DataFrame(
    {
        "Subject" : ["Ankit","Rahul","Vikash","Bablu","Mohit"],
        "Marks" : [80,72,99,41,33]
    }
)

plt.bar(Stu["Subject"],Stu["Marks"],label = "Marks")
plt.title("Comparing Marks of 5 Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid()
plt.legend()
plt.show()


'''
Q10. Using Pandas built-in plotting, load or create a dataset with at least 
4 numeric columns. Create:  
• A histogram for marks distribution 
• A box plot to visualize spread and outliers 
• A pie chart showing category-wise percentage
'''

# Dataset
df = pd.DataFrame(
    {
        "Maths": [85, 78, 92, 88, 76],
        "Physics": [80, 75, 90, 84, 70],
        "Chemistry": [82, 77, 91, 86, 74],
        "English": [88, 81, 85, 90, 78],
        "Category":["A","B","A","A","C"]
    }
)

# 1. Histogram 
plt.hist(df["Maths"],bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 2. Box Plot
plt.plot(
    kind="box",
    title="Marks "
)
plt.boxplot(df["Maths"])
plt.title("Spread and Outliers")
plt.ylabel("Marks")
plt.show()

# 3. Pie Chart 
plt.pie(
    df["Category"].value_counts(),
    labels=df["Category"].value_counts().index,
    autopct="%1.1f%%"
)
plt.title("Category-wise Percentage")
plt.show()


'''
Q12. Create a subplot layout of 2 rows × 2 columns using Matplotlib 
containing:  
• Line plot 
• Scatter plot 
• Bar chart 
• Histogram 
All using the same dataset. Add a main title using suptitle() 
'''

subjects = ["Maths", "Physics", "Chemistry", "English", "Computer"]
marks = [85, 78, 92, 88, 95]

plt.figure(figsize=(10, 8))

#1. Line Plot
plt.subplot(2, 2, 1)
plt.plot(subjects, marks, marker='o')
plt.title("Line Plot")

#2. Scatter Plot
plt.subplot(2, 2, 2)
plt.scatter(subjects, marks)
plt.title("Scatter Plot")

#3. Bar Chart
plt.subplot(2, 2, 3)
plt.bar(subjects, marks)
plt.title("Bar Chart")

#4. Histogram
plt.subplot(2, 2, 4)
plt.hist(marks, bins=5)
plt.title("Histogram")

# Main Title
plt.suptitle("Student Marks Visualization")

plt.show()