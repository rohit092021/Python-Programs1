winning_no=int(input("enter winning no"))
guess_no=int(input("guess any no"))
if guess_no==winning_no:
    print("you win")
else:
    if winning_no<guess_no:
        print("winning no is too low")
    else:
        print("winning no is too high")