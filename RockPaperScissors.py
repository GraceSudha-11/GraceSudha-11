import random

possible_Actions =["rock","paper","scissor"]
computer_action =random.choice(possible_Actions)
print(computer_action)
user_action =input("Enter choice {rock,paper,scissor} :")

if (user_action == computer_action):
    print("IT'S A TIE")
elif((user_action =='rock') and (computer_action =='paper')):
    print("Paper rolled rock! ! ! \n Computer wins")
elif((computer_action =='rock') and (user_action =='paper')):
    print("Paper rolled rock! ! ! \n User wins")
elif((user_action =='paper') and (computer_action =='scissor')):
    print("Paper cutted ! ! ! \n Computer wins")
elif((computer_action =='paper') and (user_action =='scissor')):
    print("Paper cutted! ! ! \n User wins")
elif((user_action =='rock') and (computer_action =='scissor')):
    print("Rock smashed the scissor! ! ! \n User wins")
elif((computer_action =='rock') and (user_action =='scissor')):
    print("Rock smashed the scissor! ! ! \n Computer wins")
else:
    print("Invalid !!")