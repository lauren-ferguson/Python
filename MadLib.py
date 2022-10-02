# string concatenation
# suppose we want to create a string that says "travel to ____"
country = "Costa Rica" # some string variable

# a few ways to do this
# print("travel to " + country)
# print("travel to {}".format(country))
# print(f"travel to{country}")

adj = input("adjective: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
famous_person = input("famous person: ")

madlib = f"Traveling is so {adj}! It makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)