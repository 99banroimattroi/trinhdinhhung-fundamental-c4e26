import random

WORDS = ("Rhinoceros","Cheetah","Elephant")

print(
"""
         Trò Chơi Truy Tìm Động Vật !
Xắp xếp các chữ cái để tạo thành một từ (Tiếng Anh)
          (Nhấn phím Enter để thoát)
"""
)

play=input("Bạn đã sẵn sàng ? (Y/N) ")
while play=="y":
    word = random.choice(WORDS)
    correct = word
    jumble =""
    while word:
        position = random.randrange(len(word))
        jumble += word[position] +" "
        word = word[:position] + word[(position + 1):]

    print("Cho các chữ cái sau:", jumble)
    guess = input("\nCâu trả lời của bạn: ")
    while guess != correct and guess != "":
        print(":( Rất tiếc !")
        guess = input("Câu trả lời của bạn: ")

    if guess == correct:
        print("Hura\n")
        play=input("Bạn có muốn chơi tiếp? (Y/N) ")
    elif guess== "":
        print("Bạn đã thua!")
        play=input("Bạn có muốn chơi lại? (Y/N) ")


print("Thanks for playing GAME")

input("\n\nNhấn phím ENTER để thoát.")