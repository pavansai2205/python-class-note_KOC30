#day 01
print("hello world")
print("Day 1 - python print function")
print("the function is declered like this")
print("print('what to print')")
print("hello world\nhello world")
print("hello" + "nithin")
print("hello" + " " + " nithin")
input("what is your name")
input ("what is your age\n")
print("you are age is" + input("what is your age"))
name = input("what is your name")
length = int(len(name))
print(f"your name has {length} characters")


#project 01
print("welcome to band name generator")
name = input("whats name of the city you grew up in")
pet = input("whats your pets name")
print("your band name is " + name + " " + pet)

#day 02
import random
num = random.randint(1,100)
print(num)
num_1 = random.random()
num_2 = round(num_1,2)
print(num_2)

#heads or tailes
number = random.randint(1,2)
if number == 1:
  print("heads")
else:
  print("tails")

#python lists

  
# states_names = ["andhrapradesh","telangana","tamilnadu","kerela","punjab",]
# print(states_names)
# print(states_names[2])
# print(states_names[-2])
# states_names[-2] = "kearalayia"
# print(states_names)
# states_names.append("nithin land")
# print(states_names)
# states_names.extend(["nithin land", "mother land", "father land"])
# print(states_names)


#project random member bill
import random
name = input("give me everybody names, seperated by commas\n")
name_1 = name.split(",")
length = len(name_1)
random_choice = random.randint(1 , length - 1)
name_2 = name



# day-04-randamaition
# import random
# num = random.randint(1, 100)
# print(num)


# num_1 = random.random()
# print(num_1)[random_choice]
print(f"{name_2} will pay the bill today")





import math
import random
loses=0
score=0
looprun=0
print("_________\n")
print("Welcome To Dice Game🎲")
print("_________\n")
while True:
  a=input(">>>Enter Your Guess 🤫:  ")
  if a.lower()=='quit':
    if score==0:
      a1="times! 😂"
    elif score==1:
      a1="time! 🥱"
    elif score==2:
      a1="times! 😃"
    else:
      a1="times! 🤩"
    print("\nThanks for playing the game. You won",score, a1 )
    exit()
  def dice_game(user_guess,loses,score):
    if user_guess>6:
      print("\n🚫🚫🚫\nEnter a valid guess within the range 1-6\n")
    else:
      print("\nRolling 🎲...")
      dice_value=random.randint(1,6)
      print("🎲"+ "="+str(dice_value))
      if user_guess==dice_value:
        print("Congratulations You won!!! 🥳\n")
        score+=1
      else:
        if loses>0:
          print("You lost again 🤕 but don't give up keep trying!😤\n")
        else:
          print("You lost 😕\n")
          loses+=1
    b=[loses,score]
    return b       
  b=dice_game(int(a),loses,score)
  loses=b[0]
  score=b[1]