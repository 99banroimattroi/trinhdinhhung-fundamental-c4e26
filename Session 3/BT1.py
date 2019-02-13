var = ["Death note", "Netflix", "Teaching","PUBG"]

print("Hi there, here you favorite things so far")

print("*"*30)    
for i, n in enumerate(var, 1 ):  
    print(i , n, sep=". ")
print("*"*30)  

n = int(input("Position you want to update ? "))
var[n-1] = input("Enter new favorite: ")

print("*"*30) 
for i, n in enumerate(var, 1 ):
    print(i , n , sep=". ")
print("*"*30) 

