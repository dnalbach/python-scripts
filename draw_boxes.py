from os import system
import time

system('clear')

pattern_character = "*"

print "Please only enter numbers (for example, 3, 5, 9, 22)\n"
length = int(raw_input("How long is the box?  "))
height = int(raw_input("How tall is the box?  "))

# The \ symbol means to continue the line of code on the next line.
# There cannot be any chacters (including spaces) after the \
# The \n inside the string tells the terminal to start a new line,
# which is one way you can generate white space between lines.
print "\nYou requested a box that is " + \
str(length) + " x " + str(height) + "\n"

length_line = (pattern_character + " ") * length

print length_line

i = 2
while i < height :
    print pattern_character, " " * ((length * 2) - 5), pattern_character
    i += 1

print length_line
print "\n\n"