# print statement 
print ("Hello, World!")
print("welcome to python programming")

# variable declaration
name= "Monika"
age=18
height=5.4
is_student=True

print(name)
print(age)
print(height)
print(is_student)

# taking input from user
name=input("enter your name: ")
age=input("enter your age: ")
height =input("enter your height: ")
is_student=input("are you a student? (True/False): ")

print(name)
print(age)
print(height)
print(is_student)

# arithematic operators
a=20
b=5
print("Addition:", a+b)
print("Subtraction:", a-b)  
print("Multiplication:", a*b)
print("Division:", a/b) 
print("Modulus:", a%b)
print("Exponentiation:", a**b)

# camparison operator
print("Equal:", a==b)
print("Not Equal:", a!=b)
print("Greater than:", a>b)
print("Less than:", a<b)
print("Greater than or equal to:", a>=b)
print("Less than or equal to:", a<=b)

#  if else statement
num=int(input("enter a number: "))
if num>0:
    print("The number is positive") 
elif num<0:
    print("The number is negative")
else:
    print("The number is zero")

# even or odd
num=int(input("enter a number: "))          
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")
    # for loop
for i in range(1, 6):
        print(i)

# while loop
count=1
while count<=5:
    print(count)
    count+=1  

# list
fruits=["apple", "banana", "cherry", "date"]
print(fruits)  
print(fruits[0])
fruits.append("elderberry")
print(fruits)


# tuple
colors=("red", "green", "blue", "yellow")
print(colors)
print(colors[0])

# dictionary
person={"name":"Monika", "age":18, "height":5.4}
print(person)
print(person["name"])
print(person["age"])
print(person["height"])
# set
numbers={1, 2, 3, 4, 5}
print(numbers)
#  function
def greet(name):
    print("Hello, " + name + "! Welcome to Python programming.")    



