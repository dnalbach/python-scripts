from os import system
import math

system('clear')

i = 0
while i < 49 :
    format_string = "{0:." + str(i) + "f}"
    print format_string.format(math.pi)
    i += 1



