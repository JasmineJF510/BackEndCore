print("Hello World!")

# week 1 day 1 lecture
# Using # allows you to write a comment in your code that will not be ran. Pythin and VS code will ignore it

first_words = "Hello World!"

#intiate a docstring with triple quotes, either single ''' ot double """"

doc = '''
Enter 1 to continue 
Enter 2 to go back
Enter 3 to figure it all out
'''

print(doc)

#python reads code from the top to the bottom we've defined the variable doc, if we redefine the data stored there, then our print function will print that new piece of data

doc = "This is a new string"

print(doc)

first, middle, last = "Jasmine", "Elyise", "Jackson-Ford"
print(first, middle, last)