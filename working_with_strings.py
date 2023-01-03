# printing a string in the new line
print("Better late\nthan never")

# putting quotation mark inside a string
print("\"Better late than never\"")

# store string and print the variable
phrase: str = "Better Better late than never"
print(phrase)

# using upper and lower function
print(phrase.lower())
print(phrase.upper())

# count() function
counting = phrase.count("Better")
print(counting)

# len() function
print(len(phrase))

# index value giving
print(phrase[0])

# index() function
print(phrase.index("t"))

# Replace functionality
print(phrase.replace("Better","Hello mate"))