# I watched a TikTok about not being able to think of a "random fun fact". I decided to make a fun fact generator, in case I end up in a similar situation.
# Import package
import random


# List fun facts (feel free to edit what applies to you)
fun_fact_list = ["I'm double jointed", "I speak a foreign language", "My favorite food is sushi", "I went skydiving", "I grew up in a different country", "I hate chocolate", "I'm married", "I grew up playing soccer", "I have a twin", "My top spotify artist was Taylor Swift"]


# Fun Fact Generator
user_input = input("Do you hate it when you can't think of a random fun fact? (yes/no): ")  # Ask if user wants to generate a fun fact
if user_input.lower() == "yes":  # If yes, give fun fact
    print("Let's do something about that. See below for a randomly generated fun fact!")
    for i in range(1):
        fun_fact = random.choice(fun_fact_list)
        print(fun_fact)
elif user_input.lower() == "no":  # If no, no fact :(
    print("OK")
else:
    print("Please type yes or no")
