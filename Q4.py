#Write a Python program to get a single string from two given strings, separated by a space and swap the first 
#two characters of each string. 

str1=input("Enter a string :- ")
str2=input("Enter a string :- ")

x=str1[0]

str1=str1.replace(str1[0:2], str2[0:2]) #it use for swap
str2=str2.replace(str2[0:2], x)

print(str1)
print(str2)