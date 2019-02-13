var = ["Death note", "Netflix", "Teaching","PUBG"]

print("*"*30)    
for i, n in enumerate(var, 1 ):  
    print(i , n, sep=". ")
print("*"*30)  

n = int(input("Nhap vi tri can xoa:  "))
var.pop(n-1)

print("*"*30) 
for i, n in enumerate(var, 1 ):
    print(i , n , sep=". ")
print("*"*30) 