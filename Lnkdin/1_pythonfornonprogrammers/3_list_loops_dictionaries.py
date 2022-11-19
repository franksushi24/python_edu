# LISTS: To use we use square brackets []

# fav_movies = ["Starwars", "Rocky", "Dune"]

# print(len(fav_movies))

# fav_movies.append("Iron Man")

# print(len(fav_movies))

# print(fav_movies)

# fav_movies.insert(1,"Batman")

# print(fav_movies)

# del(fav_movies[2])

# print(fav_movies)

# del(fav_movies[2])
# del(fav_movies[2])
# del(fav_movies[1])

# print(fav_movies)

# LOOPS: to use we use for _ in ____ ()

for number in range(10):
    # print("Hello")
    # print("Hi there")
    print(number)

for x in range(10):
    print(x)

fav_movies = ["Sandlot", "The Lego Movie", "Dune"]

for movie in fav_movies:
    print(movie)

        # Challenge: Loop 40 times and print the number of the loop times 2. EX. 2,4,6,8...

for number in range (40):
    print(2 + number * 2)

# DICTIONARIES: to use we use curly brackets {}

# cats = {"Jane":6, "Tom":14, "Sara":8}

# print(cats["Tom"])

        # TO ADD TO DICTIONARY

# cats["Wilson"] = 1 

        # TO DELETE FROM DICTIONARY
        
# del(cats["Tom"])

# print(cats)

# print(len(cats))

#         Challenge: Create a dictionary with Ints for keys and Booleans for values

X = {1:True, 2:False}

import random

coin_flip = random.randint(1,2)

print(coin_flip)

# 1 = Heads
# 2 = Tails

print(f"Was the result of the coin flip Heads? Answer: {X[coin_flip]}")
