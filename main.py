print("Guess the number you have only three chances")
print("ALL THE BEST !")
secrete_number=7
guess_count=0
guess_limit=3
while guess_count < guess_limit:
    guess=int(input("Guess : "))
    print(guess)
    guess_count+=1
    if guess==secrete_number:
        print("you win!")
        break
else :
    print("sorry you failed")
    
