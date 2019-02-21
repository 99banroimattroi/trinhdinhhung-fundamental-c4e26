items = ["Com", "Pho", "Bun", "Piza"]
#EX1:
# for i
#for i in range(len(items)):
#    print(items[i])


#EX2:
# for reach
#no = 0
#for food in items:
#    print(no, food, sep=". ")
#    no += 1


#EX3:A
#for i, food in enumerate(items):                 #C2: enumerate(items, 1)
#    print(i +1 , food)


#EX4: 
# print(items)
# items.pop(1)
# print(items)




#EX5:
print(items)
items.remove("Bun")
print(items)