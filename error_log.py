import os
import re

# path of the directory
mypath = "D:\Scripts\Concepts"

for root, dirs, files in os.walk(mypath):
    error_lines = set()  # holds lines with errors

    for file in files:   # for each file
        line_num = 0     # for counting lines of each file
        with open(os.path.join(root, file), "r") as auto:  # open file
            a = auto.read(50000)  # assigning the content of the file into variable a
            for line in a.splitlines():  # splitting the content of each line
                line_num += 1
                Errors = re.findall('(?i)error', line)  # makes case insensitive
                for error in Errors:
                    if error in line:
                        error_lines.add(line)
                        # print(file, line_num, line)
# print('\n'.join(error_lines))

write = '\n'.join(error_lines)

with open('D:\Scripts\error_python.txt', 'a') as output:
    output.write(str(write))







