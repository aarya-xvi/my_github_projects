from itertools import *
words = (input("Type the word: ")).upper()
mapping= {
    "A":1,
    "B":2,
    "C":3,
    "D":4,
    "E":5,
    "F":6,
    "G":7,
    "H":8,
    "I":9,
}
load =(["".join(w) for w in permutations(words)])
for l in load:
    sum = 0
    result = []
    for word in l:
        result_final = str(mapping.get(word,0))
        result.append(result_final)
        resultt= "".join(result)
    print("{}:{}".format(l,resultt))
vals= permutations(result)
for val in vals:
    values="".join(val)
    sum += int(values)
print ("TOTAL SUM:{}".format(sum))







