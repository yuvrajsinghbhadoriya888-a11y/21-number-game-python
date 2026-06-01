current=0
print("welcome to 21 number game ""\n""you will play with the program ")
while current<= 21:
 #user turn
 user = int(input("your turn"  ))
 while user < 1 or user > 3:
    print("invalid number try again between 1 and 3 only")
    user = int(input("your turn  "  ))
 for i in range(user):
   current += 1
   if current == 21:
     print("the current value is 21\nyou lose")
     break
 if current == 21:
  break
#computer turn
 import random
 computer = random.randint(1,3)

 for i in range(computer):
        current += 1
        print("computer played",current)

        if current == 21:
            print("\nComputer reached 21. You win!")
            break

print("^" * 20)