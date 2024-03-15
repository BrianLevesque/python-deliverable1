name = input("Welcome to GC mini golf! What is your name?")
holes = int(input("Hi, "+name+ "! Would you like to play 3 or 6 holes?"))
score = 0
i = 1
putts = 0
while i<= holes:
    putts = int(input("How many putts for hole "+ str(i)+"? (par:3)"))
    score += putts
    i += 1
    parScore = 0
if holes == 3:
    if score < 9:
        parScore = score - 9
        print("Great job, "+name+"! Your total score was: "+str(parScore))
    elif score == 9:
        print("Good game, "+name+". Your total score was: 0.")
    else:
        parScore = score -9
        print("Nice try, "+name+"... Your total score was: +"+str(parScore)+".")

else:
    if score < 18:
        parScore = score - 18
        print("Great job, "+name+"! Your total score was: "+str(parScore))
    elif score == 18:
        print("Good game, "+name+". Your total score was: 0.")
    else:
        parScore = score -18
        print("Nice try, "+name+"... Your total score was: +"+str(parScore)+".")

