question = [
    "Answer the following algebra question:\nIf x = 8, then what is the value of 4(x+3) ?",
    "Estimate this answer (exact caculation not need):\nJack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean ?",
    "How many student are in CE4 GEN 26 ?",
]

answer = [
    {
        "a": 35,
        "b": 36,
        "c": 40,
        "d": 44,
    },
    {
        "a": "About 55",
        "b": "About 65",
        "c": "About 75",
        "d": "About 85",
    },
    {
        "a": 15,
        "b": 20,
        "c": 25,
        "d": 30,
    },
]

choice = ["a","b","c","d"]

right = [44, "About 65", 15]

count = 0

x = 0

print("                     =====================Game Đi Tìm nhà Giải Đố=====================")

for i, j in enumerate(question):
    x += 1
    print(x,j,"\n",sep = " ")
    for k in choice:
        print(k, answer[i][(k)], sep = ". ")
    n = input("Your choice: ")
    if answer[i][n] == right[i]:
        print("\nBingo\n")
        count += 1
        
    else:
        print("\n:(\n")
        

print("You correctly answer %s out of %s questions"%(count, len(question)))
print("\n=======================THANKS FOR PLAYING GAME===========================")
