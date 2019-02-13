var = ["Death note", "Netflix", "Teaching","PUBG"]

print("*"*30)    
for i, n in enumerate(var, 1 ):  
    print(i , n, sep=". ")
print("*"*30)  

n = str(input("Nhap tu can xoa:  "))
var.remove(n)

print("*"*30) 
for i, n in enumerate(var, 1 ):
    print(i , n , sep=". ")
print("*"*30) 
