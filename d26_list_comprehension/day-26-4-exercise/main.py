sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
words_list = sentence.split()
words_list = [word.rstrip("?") for word in words_list]
print(words_list)

result = {word: len(word) for word in words_list}

print(result)

