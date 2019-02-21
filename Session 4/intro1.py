teen_code = {
    "pt": "Phat trien",
    "eny": "Em Nguoi Yeu",
    "any": "Anh Nguoi Yeu",
    "stt": "Status"
}

while True:
    print("*"*70)

    k = input("Enter code:  ")

    print("*"*70)

    if k in teen_code:
        print(teen_code[k])
    else:
        print("Not Found")
        contrib = input("Do you want to contribute (Y/N)").upper()
        if contrib == 'Y':
            trans = input("Your translation? ")
            teen_code[k] = [trans]
           
    option = input("Do you want to exit ? Press 'E' and Enter to exit ")
    if option == 'e': break
