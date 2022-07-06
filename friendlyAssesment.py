#  Write a Python script to print a dictionary where the keys are numbers between 
#  1 and 15 (both included) and the values 
#  are squares of keys.
my_dict={}
for i in range(1,16):
    my_dict[i]=i*i 
    print(my_dict) 

# Q6: Write a Python program to create a dictionary
#  from two lists without losing duplicate values. 
marks=[10,20,30,40,50]   
names=["Mary","Charles","Jack","Star","Steve"] 
names_and_marks={}
for m in names: 
    for b in marks:
        names_and_marks[m]=b
        print(names_and_marks)
# Write a Python program to convert more than 
# one list to a nested dictionary. 
marks=[10,20,30,40,50]   
names=["Mary","Charles","Jack","Star","Steve"]   
classes=["North","East","West","South","Central"]
my_dict={} 
my_dict=marks.copy
my_dict.update(names)
print(my_dict) 

# Write a Python program to remove consecutive duplicates of a given list. 
list_one=[5,4,3,2,1,2,3,4] 
list_two=set(list_one)
print(list_two)


# Write a Python program to check whether an element exists within a tuple.
my_turple=(1,"monique","true",955,20)
n=input("Enter value: \n")
for i in my_turple: 
    if i==n:
        print("present")
    else:
        print("absent")   

# Use a dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down',
#  etc. Display all words and 
# then ask the user to enter a word and display the antonym of it.           
# antonyms={'Right':'Left', 'Up':'Down','east':'west'} 
# n=input("Enter word: \n") 
# for i in antonyms: 
#     if i.values()==n or :
#         print(i)    




# Write a function for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give  
# the driver one demerit point and print the total number of demerit points. For example, 
# if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended” 


def speed_check(speed): 
    speedlimit=70 
    dermitpoint=((speed-speedlimit)*1)/5 
    if speed<70: 
        print("okay")
    elif dermitpoint>12 and speed>70: 
        print("lisence suspended")    
    elif speed>70:
        print(f"Points:{dermitpoint}")
    else: 
        print("none") 

speed_check(88)  

numbers=2**3
# print(numbers)  
# Write a function called showNumbers that takes a parameter called limit. 
# It should print all the numbers between 0 and limit with a label to identify 
# the even and odd numbers. For example, if the limit is 3, it should print: 



list_y=[{19:"mary",20:"jack"},{10:"tessa",15:"mmm"}]  
my_dict=dict(list_y)
for i in my_dict: 
    for m in i: 
        year_of_birth=2020- i.key()
        print(f"Hello {i.value()} you were born in {year_of_birth}")

x="james"
print(x[0::1]) 
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"] 
list_3=[]
for i in list1: 
    for j in list2: 
        list_3.append(i+j) 
        print(list_3) 

numbers = [1, 2, 3, 4, 5, 6, 7] 
new_numbers=[]

for x in numbers: 
    new_numbers.append(x*x)
    print(new_numbers)     


a=[10,20,30,40,50,60]   
b=[20,80]
for i in a: 
    for j in b: 
        if i==j: 
            print("true") 
    else: 
        print("none")  



def comparison(n): 
    list=[1,2,3,4,5,6]
    if n in list: 
        print(n) 
    else: 
        print("none")      

comparison(6)  