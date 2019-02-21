var = ["Death note", "Netflix", "Teaching","PUBG"]

print("*"*30)    
for i, n in enumerate(var, 1 ):  
    print(i , n, sep=". ")
print("*"*30)  

n = (input("Choice:  "))

if n.isdigit():
    i = int(n)-1
    var.pop(i)
else:
    var.remove(n)

print("*"*30) 
for i, n in enumerate(var, 1 ):
    print(i , n , sep=". ")
print("*"*30) 