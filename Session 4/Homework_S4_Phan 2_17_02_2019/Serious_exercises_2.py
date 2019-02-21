answer = [35 , 36 , 40 , 44]

print("Answer the following algebra question:\nIf x = 8, then what is the value of 4(x+3) ?")

n = 0

for i in answer:
    n += 1
    print(n,i, sep = ". ")

choice = input("Your choice: ") 

if choice == "4":
    print("Bingo")
else:
    print(":(")
