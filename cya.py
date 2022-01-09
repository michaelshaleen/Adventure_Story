name = input("Greetings! What's your name? ")
print("Welcome" , name , "this is sure to be a wild ride!")
# commas add a space automatically

answer = input("You are on a dirt road, your only options are left or right \
  which way would you like to go? ").lower()

if answer == "left":
  answer = input("You arrive at a river. You can walk around it or swim through it.\
    Type walk or swim: ").lower()
  if answer == "swim":
    print()
  if answer == "walk":
    print()



elif answer == "right":
  print()

else:
  print("Not a vaild option. You lose.")