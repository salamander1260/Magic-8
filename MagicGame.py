import random
from playsound import playsound

random_number = (random.randint(0, 10))
print(random_number)
name = input("Please enter your name: ")
question = input("Ask your question: ")
answer = []

if random_number == 1:
    answer.append("Yes - Definitely")

elif random_number == 2:
    answer.append("It is decidedly so")

elif random_number == 3:
    answer.append("Without a doubt")

elif random_number == 4:
    answer.append("Reply hazy, try again")

elif random_number == 5:
    answer.append("Ask again later")

elif random_number == 6:
    answer.append("Better not tell you now")

elif random_number == 7:
    answer.append("My sources say so")

elif random_number == 8:
    answer.append("Outlook not so good")

elif random_number == 9:
    answer.append("Very doubtful")

else:
    playsound('2sike.wav') # if the random number is 10. it will play a wav file but there's an Error 263 which I don't know hot to fix
    answer.append("Number not in list")
print()
print(name + " ask: " + question + "? " + "\nAnswer:{}".format(answer))
