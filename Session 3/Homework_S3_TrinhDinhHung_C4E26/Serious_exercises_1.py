items = ["T-Shirt","Sweater"]

while True:

    print("Welcome to our shop, what do you want (C, R, U, D) ? ")

    a = (input().upper())

    if a == "R":
        print("Our items:", ",".join(items))
    elif a == "C":
        n = items.append(input("Enter new item: "))
        print("Our items:", ",".join(items))
    elif a == "U":
        n = int(input("Update Position? "))
        items[n-1] = input("New item? ")
        print("Our items:", ",".join(items))
    elif a == "D":
        n =  int(input("Delete position? "))
        del items[n-1]
        print("Our items:", ",".join(items))
    else:
        print("Please select one of the ['C','R','U','D'] options!")
    option = input("Do you want to exit ? Press 'E' and Enter to exit ")
    if option == 'e': break
 





    
