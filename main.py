name = "Patricia"
question = "When will I become rich?"
answer = ""

import random

random_number = random.randint(1, 11)

#print(random_number)

if random_number == 1:
    answer = "Yes - definitely."
elif random_number == 2:
    answer = "It is decidely so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
elif random_number == 10:
    answer = "I wish I could tell you the answer."
elif random_number == 11:
    answer = "Can't see that information."
else:
    answer = "Error"

print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)

#additional implementation features
#if user doesn't write a name
"""if name == "":
    print(question)
else:
    print(name + " asks: " + question)"""

#if a user doesn't write a question
"""if question == "":
    print("You need to ask a question!")
else:
    print(name + " asks: " + question)"""

