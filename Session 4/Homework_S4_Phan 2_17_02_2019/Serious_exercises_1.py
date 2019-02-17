prices = {}

prices["banana"] = 4
prices["apple"] = 2
prices["orange"] = 1.5
prices["pear"] = 3

stock = {}

stock["banana"] = 6
stock["apple"] = 0
stock["orange"] = 32
stock["pear"] = 15

total = 0

for i in prices :
    print(i, "\nprice:", prices[i], "\nstock:", stock[i],"\n")

for i in stock:
    print("sell all %s to receive: %s $"% (i, stock[i] * prices[i]))
    total += stock[i] * prices[i]

print ("The money you receive:", total,"$")