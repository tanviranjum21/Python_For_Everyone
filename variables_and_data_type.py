# I will use the name and hours of study as my variables and dynamically assign them
print("Please insert your name")
name = input()
print("Please insert how many hours you have done coding today")
hours = input()
print("Please insert the IDE/editor name you have used to do coding")
IDE_name = input()

print("Hey I am " + name + ",")
print("I have started refresh my data science knowledge")
print("Today I have done coding for " + hours + " hours.")
print("And I am using " + IDE_name + "as IDE/editor for this")

print("____________________________________________________________________________________")

# Now to understand int let's move one step forward with the practice
# Now let's assume if I do coding less than 3 hours a day a prompt will tell me not enough study

converted_hours = int(hours)  # hours converted to int so that mathematical calculation or if/else functionality can
# be used
hours_need = 3 - converted_hours
if converted_hours < 3:
    print("Not enough you must need to do " + str(hours_need) + " hour coding")
else:
    print("Great you have achieved the goal for today now be consistent")

print("____________________________________________________________________________________")

# Now let's assume you are participating in a hackathon where you need to separate between a male and female to give
# them different t-shirt and kit type. We will showcase the use of boolean data type here

is_male = False

if is_male:
    print("Please take t-shirt from left shelves")
else:
    print("Please take t-shirt from the right shelves")


