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

random_swim = random.randint(0, 1)
random_walk = random.randint(0, 2)
print("Welcome,", name ,",this is sure to be a wild ride!")

# loop to display all options in organized fashion
count = 0
for i in swim_options:
  count += 1
  print(count, i, "swim options")


answer = input("You are on a dirt road, your only options are left or right which way would you like to go? \nType Left/Right or Q to quit: ").lower()
if answer == 'q':
  quit()

# user decides to go left from dirt road
if answer == "left":
  answer = input("You arrive at a river. You can walk around it or swim through it.\nType walk or swim: ").lower()
  if answer == "swim":
    answer = swim_options[random_swim]
    if answer == swim_options[0]:
      print(answer, "another one bites the bottom of a river. You lose.")
    elif answer == swim_options[1]:
      print(answer, "well done king or king-et.")
      answer = input("Feeling great, do you want to rest or keep walking? Type Walk/Rest: ").lower()
      if answer == "walk":
        print("While walking you are bitten by the world's largest ant and you die a slow and painful, super painful death. You lose.")
    elif answer == swim_options[2]:
      print(answer, "index two")
    if answer == swim_options[3]:
      print(answer, "index three")
    elif answer == swim_options[4]:
      print(answer, "index four")
    elif answer == swim_options[5]:
      print(answer, "index five")
    elif answer == swim_options[6]:
      print("You crazy son of a ..., you win! You bloody win! You find a beautiful oasis with\
        a friendly population who takes you in and you live decently ever after. You win!")

    # answer = input("Swimming is quite challenging, do you blow out your air and walk along\
    # the bottom or keep swimming? Type Swim/Sink").lower()

# left > walk
  elif answer == "walk":
    answer = input("Walk on your hands or on your feet? Hands/Feet ").lower()
    if answer == "hands":
      print("Feet are overrated anyways. Until you palm a sharp stake with your favorite hand and meet your end via blood loss. You lose.")
    elif answer == "feet":
      print("You hear someone shout 'Foot boy!' from the trees, you are apparently in the wrong neighborhood and are eaten for dinner. You lose. ")
#  end options for left > walk



# user takes a right instead of a left
elif answer == "right":
  answer = input("Right you are! While walking you enjoy a beautiful sunset, but you need to find shelter soon\
    do you look for a town or build a shelter? Type town/shelter: ").lower()
  if answer == "shelter":
    print("Great call.")
    answer = input("What will you use to build a shelter genius? Sticks/Wet Leaves ").lower()
    if answer == "wet leaves":
      print("your wet leaves dripped on you while you slept, you died from covid.")
    elif answer == "sticks":
      print("Your stick mansion caught on fire with you in it, RIP user.")
  elif answer == "town":
    answer = input("Great choice, now decide, milk or rainwater? ").lower()
    if answer == "rainwater":
      print("You lose.")
    elif answer == "milk":
      answer = input("Excellent choice my user! Where will you go next? Bed/Tavern ").lower()
      if answer == "tavern":
        print("You drunk, you lose.")
      elif answer == 'bed':
        print("Real exciting...lying in bed...alone... you lose. ")
# end options if path right is taken
