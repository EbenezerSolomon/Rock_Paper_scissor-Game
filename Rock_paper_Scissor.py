#importing random module
import random
#printing Game Rules
print("Welcome_To_Rock_paper_scissor Game")
print("Winning Rules"+"\n1.Rock Vs Paper==>Paper Wins"+"\n2.Rock vs Scissor==> Rock wins"+"\n3.Paper vs Scissor==>Scissor Wins")

#Printing Choices For user to select
while True:
    print("\nChoices: \n"+("1.Rock\n")+("2.Paper\n") +("3.Scissor\n"))
    choice=int(input("Enter Your Choice:"))

    while choice>3 or choice<1:
      choice=int(input("Enter valid choice"))

    if choice==1:
       choice_name="Rock"
    elif choice==2:
       choice_name="Paper"
    else:
       choice_name="Scissor"

#printing Users Choice
    print("\nUser Choice is "+ choice_name)
    print("\nnow its computer turn.....")
#assigning random.randint() for random choice selections

    comp_choice=random.randint(1, 3)

#computer Selection Random choices
    while comp_choice==choice:
        comp_choice=random.randint(1, 3)
    if comp_choice==1:
        comp_choice_name="Rock"
    elif comp_choice==2:
        comp_choice_name="Paper"
    else:
        comp_choice_name="Scissor"
#printing Computer choice and User Choice

    print("\nComputer Choice is "+comp_choice_name)
    print(choice_name +" Vs "+ comp_choice_name)
#Assigning Game Rule Process
    if((choice==1 and comp_choice==2)or(choice==2 and comp_choice==1)):
        print("Paper Wins")
        result="PAper"
    elif((choice==1 and comp_choice==3)or(choice==3 and comp_choice==1)):
        print("Rock Wins")
        result="Rock"
    else:
        print("scissor Wins")
        result="Scissor"
#printing Who Wins
    if result== choice_name:
        print("User Wins")
    else:
        print("So Computer Wins")
#To play again
    print("\nDo you want to play again(Y/N)")
    ans=input()

    if ans==N or ans==N:
        break


print("Thank you for Playing")
