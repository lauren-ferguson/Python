#
import random

fun_fact_list = ["I'm double jointed", "I speak a foreign language", "My favorite food is sushi", "I went skydiving", "I grew up in a different country", "I hate chocolate", "I'm married", "I grew up playing soccer", "I have a twin", "My top spotify artist was Taylor Swift"]


user_input = input("Do you hate it when you can't think of a random fun fact? (yes/no): ")
if user_input.lower() == "yes":
    print("Let's do something about that. See below for a randomly generated fun fact!")
    for i in range(1):
        fun_fact = random.choice(fun_fact_list)
        print(fun_fact)
elif user_input.lower() == "no":
    print("OK")
else:
    print("Please type yes or no")
