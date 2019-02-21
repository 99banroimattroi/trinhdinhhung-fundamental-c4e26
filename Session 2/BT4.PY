import random   #from random import randint
n = random.randint(1, 100)

Cloudy = '''
            ------               _____
           /      \ ___\     ___/    ___
        --/-  ___  /    \/  /  /    /   \
       /     /           \__     //_     \
      /                     \   / ___     |
      |           ___       \/+--/        /
       \__           \       \           /
          \__                 |          /
         \     /____      /  /       |   /
          _____/         ___       \/  /\
               \__      /      /    |    |
             /    \____/   \       /   //
         // / / // / /\    /-_-/\//-__-
          /  /  // /   \__// / / /  //
         //   / /   //   /  // / // /
          /// // / /   /  //  / //
       //   //       //  /  // / /
         / / / / /     /  /    /
      ///  / / /  //  // /  // //
         ///    /    /    / / / /
    ///  /    // / /  // / / /  /
       // ///   /      /// / /
      /        /    // ///  /'''
print("Hello, this is a random number from 1 to 100 - Weather")
if n < 30:
    print("Rainy")
elif n < 60:
    print(Cloudy)
else:
    print("Sunny")
