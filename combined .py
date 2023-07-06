# Created a program that takes 2 texfiles and combines them into 1 

# useed the open bulit in funtion to wite text files 
f1 = open("numbers1.txt","w")
f2 = open("numbers2.txt","w")
all_numbers = open("numbers3.txt","w")

# created lists  
List1 = []
List2 = []
Total_List = []

# created a variable that ask user to input numbers line 13-27  
numbers = int(input("how many numbers would you like to enter ?:"))

# created a for Loop,used the append method and bulit in function called sorted 
for i in range (0,numbers):
    user = int(input("Enter the numbers:"))
    List1.append(user)
    Total_List.append(user)
    List1 = sorted(List1)
for i in List1:
    f1.write(str(i))

print(sorted(List1))


Numbers2 = int(input("\n How many numbers would you like to enter ?: "))

# created a for Loop,used the append method and bulit in function called sorted 
for x in range(0,Numbers2):
    user2 = int(input("Enter the numbers ? "))
    List2.append(user2)
    Total_List.append(user2)
    List2 = sorted(List2)
for x in List2:
    f2.write(str(x) + "\n")

print(sorted(List2))  

# created a for Loop,used the append method and bulit in function called sorted 
Total_List = sorted(Total_List)
print("")
print(Total_List )

for k in Total_List:
     all_numbers.write(str(k) + "\n")

# used the close built in function to close all my programs 
f1.close() 
f2.close()
all_numbers.close()

# https://www.youtube.com/watch?v=UaqGPBB-eH4 watched this video to help me 

# https://stackoverflow.com/questions/17749058/combine-multiple-text-files-into-one-text-file-using-python
# got ideas from stackoverflow 

# https://www.geeksforgeeks.org/python-program-to-merge-two-files-into-a-third-file/
# gott ideas from geeksforgeeks 
