import os
import re

mypath = "D:\Scripts\Concepts"

for root, dirs, files in os.walk(mypath):
    error_lines = set()  # holds lines

    for file in files:
        line_num = 0
        with open(os.path.join(root, file), "r") as auto:
            a = auto.read(50000)
            for line in a.splitlines():
                line_num += 1
                Errors = re.findall('(?i)error', line)
                for error in Errors:
                    if error in line and line not in error_lines:
                       # print(file, line_num, line)
                        error_lines.add(line)
                        print(file, line_num, line)





