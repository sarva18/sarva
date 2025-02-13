import random
a=["Rock","Paper","Scissors"]
computer_choice=random.choice(a)
computer_score=0
player_score=0
while True:
    player_choice=(input("enter your choice:")).capitalize()
    if player_choice==computer_choice:
      print("tie")
      computer_score+=1
      player_score+=1
    elif player_choice=="rocks":
        if computer_choice=="scisscors":
             print("player wins")
             player_score+=1
        if computer_choice=="paper":
            print("computer wins")
            computer_score+=1
    elif computer_choice=="paper":
        if player_choice =="rock":
            print("computer wins")
            computer_score+=1
        if player_choice=="scissors" :
            print("player wins")
            player_score+=1
    elif player_choice=="scissors":
        if  computer_choice=="paper":
            print("player wins")
            player_score+=1
        if computer_choice=="rock":
             print("computer win")
             computer_score+=1
    else:
         print  ("final scores")
         print(player_score)
         print(computer_score)
         break
