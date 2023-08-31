#string concatenation in python
a=100
b=40
c=50
ex = "welcome a = {} , b = {} , c = {} ".format(a,b,c)
print(ex)

#using str() to concatenate
ex1 = "welcome to python "
ex2 = 3.4
print(ex1+str(ex2))

#using interpolation %

print(ex1 + "%d"  %(ex2))
print(ex1 + "%.1f"  %(ex2))


# repetition
a = "welcome "
print(a*4)

# comparing strings
# == , != , < ,  >= , > , <=

print("######################################")
#num1 = input("Enter num1 = ")
#num2 = input("Enter num2  = ")

#this will concatenate the two numbers
#print(num1+num2)

# so we use int() to convert the numbers to int

# n1 = int(input("Enter the value of n1 = "))
# n2 = int(input("Enter the value of n2  = "))
#
# print(n1+n2)
# print(n1 > n2)
# print(n1 == n2)
# print(n1<n2)
# print(n1>=n2)
# print(n1<=n2)
# print(n1!=n2)

# str1 = input("Enter String1  ")
# str2 = input("Enter string2   ")
#
# #this will concatenate the two numbers
# print(str1 > str2)
# print(str1 == str2)
# print(str1<str2)
# print(str1>=str2)
# print(str1<=str2)
# print(str1!=str2)
#


a = 20
b = 3

#floating point div
print(a / b)
#int division
print(a // b)
print(a % b)

print(10.0/3)
print(10.0//3)


print(ord('D'))
print(ord('A'))

print("######equality of strings")
print("Welcome" == "Welcome" )

print("=====equality chaining================")
print( 10 == 20 == 30 == 40)
print(10 != 20 != 20 != 40)

print(not True)
print(not False)
#
# print("######### Logical and operator usage ##############")
# username = input("Enter the username : ")
# password = input("Enter the password : ")
#
# if username == "myname" and password == "mypwd":
#     print("you have entered True condition")
# else:
#     print("you have entered Else condition")

print("############ Logical NOT operator ###########")
print(not True)
print(not False)

print("######### Logical and operator usage ##############")
username = input("Enter the username : ")
password = input("Enter the password : ")

if not username == "myname" and  not password == "mypwd":
    print("you have entered True condition")
else:
    print("you have entered Else condition")
