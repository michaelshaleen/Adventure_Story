import random
name = input("Greetings! What's your name? ")
swim_options = ["you forgot you can't swim", 
"you remember your swimming lessons from your youth and\
  you power across the river easily!", 
  "you swim to the other side of the river and see the feet of a tribal warrior.",
    "you dive into the water, and while swimming you become covered in huge black leeches!\
      as you leave the water you are dizzy and fall down from blood loss", "while swimming you cramp\
        but remember you're not a quitter so you power through perfectly fine.",\
          "Swimming sure is fun, you arrive on shore shortly."]

walk_options = ["while walking you end up feeling ill, and actually pass out from heat exhaustion."\
  , "during a lovely walk through an enchanted forest you are greeted by an elf!", "Walking around a\
    river takes a long time.",]

print(len(swim_options), "swim options")
print(swim_options[0])
print(len(walk_options), "walk options")

random_swim = random.randint(0, 5)
print("Welcome," , name , ",this is sure to be a wild ride!")
# commas add a space automatically
answer = input("You are on a dirt road, your only options are left or right\
  which way would you like to go? ").lower()


# user decides to go left from dirt road
if answer == "left":
  answer = input("You arrive at a river. You can walk around it or swim through it.\
    Type walk or swim: ").lower()
  if answer == "swim":
    # random option
    answer = print(swim_options[random_swim])
    if answer == swim_options[0]:
        print("Sorry buddy, you sunk like a stone.")
        quit()
    elif answer == swim_options[1]:
        print("Catching your breath on the shore you notice the sun will set soon.")
        answer = input("Would you like to continue walking or build shelter? Type walk/shelter: ").lower()
        if setting_sun == "walk":
          print("result from walking")
    elif answer == swim_options[2]:
        answer = input("He reaches his hand down to you, you notice\
        blood on his hand. Do you run or grab his hand or run? Type Grab/Run").lower()
    elif answer == swim_options[3]:
      print("You wake up to the howling of wolves.")
      quit()
    elif answer == swim_options[4]:
      print("Your cramp gets serious once on shore.")
      quit()
    elif answer == swim_options[5]:
      print("Feeling confident and full of vigor\
        you decide to sprint into the forest.")
      quit()


  if answer == "walk":
    print()




# user takes a right instead of a left
elif answer == "right":
  answer = input("Right you are! While walking you enjoy a beautiful sunset, but you need to find shelter soon\
    do you look for a town or build a shelter? Type town/shelter: ").lower()
  if answer == "shelter":
    print("Great call, print statements")

else:
  print("Not a vaild option. You lose.")