import sys
import random
filename = sys.argv[1]
string = "P3\n600 600\n255\n"
first = "33 223 69 "
second = "255 1 89 "
third = "100 100 100 "
for i in range(600):
  for x in range(600):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    if i % 30 < 10: string += first
    elif i % 30 > 9 and i % 30 < 20: string += second
    else: string += third
  string += "\n"
file = open(filename, 'w')
file.write(string)
print("file name: " + sys.argv[1])
