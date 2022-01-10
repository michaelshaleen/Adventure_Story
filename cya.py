import random
name = input("Greetings! What's your name? ")
swim_options = ["you forgot you can't swim", "you remember your swimming lessons from your youth and\
  you power across the river easily!", "you swim to the other side of the river and see the feet of a tribal\
    warrior", "you dive into the water, and while swimming you become covered in huge black leeches!\
      as you leave the water you are dizzy and fall down from blood loss"]

random_swim = random.randint(0, 3)
print("Welcome" , name , "this is sure to be a wild ride!")
# commas add a space automatically

answer = input("You are on a dirt road, your only options are left or right \
  which way would you like to go? ").lower()

if answer == "left":
  answer = input("You arrive at a river. You can walk around it or swim through it.\
    Type walk or swim: ").lower()
  if answer == "swim":
    print(swim_options[random_swim])
    # if swim random int from swim array
    
  if answer == "walk":
    print()



elif answer == "right":
  print()

else:
  print("Not a vaild option. You lose.")