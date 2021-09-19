"""
To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is **z**."
"""

your_name = input("Tell me your name: ")
other_name = input("Tell me your crush name: ")

combined = your_name + other_name

score1 = str(sum([combined.count("t"),
                combined.count("r"),
                combined.count("u"),
                combined.count("e"),
    ]))
    
score2 = str(sum([combined.count("l"),
                combined.count("o"),
                combined.count("v"),
                combined.count("e")
    ]))

score = int(score1 + score2)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
