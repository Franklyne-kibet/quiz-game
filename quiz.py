print("Welcome to the quiz game")

playing  = input("Do you want to play the game? ")

if playing != "yes":
    quit()

score =  0
print("Okay lets play the game")
    
answer = input("what does CPU stand for ? ")
if answer.lower() == "central processing unit":
    print("Thats correct answer")
    score +=1
else:
    print("Thats a wrong aswer")
    

answer = input("what does GPU stand for ? ")
if answer.lower()== "graphical processing unit":
    print("Thats correct answer")
    score +=1
else:
    print("Thats a wrong aswer")
    
answer = input("Best football club ? ")
if answer.lower() == "chelsea":
    print("Thats correct answer")
    score +=1
else:
    print("Thats a wrong aswer")
    
answer = input("Best Football Player ? ")
if answer.lower() == "messi":
    print("Thats correct answer")
    score +=1
else:
    print("Thats a wrong aswer")


answer = input("Best City in Africa ? ")
if answer.lower() == "nairobi":
    print("Thats correct answer")
    score +=1
else:
    print("Thats a wrong aswer")
    

print("You answered " + str(score) + " questions correctly")
print("You answered " + str((score/4) * 100) + "%.")
