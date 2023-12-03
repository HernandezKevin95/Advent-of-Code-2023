ans = 0
input_file = open("Day 1/input.txt",'r')
input_list = input_file.read().splitlines()
input_file.close()

#Part 1
'''
for entry in input_list:
    digits = []
    for x in entry:
        if x.isdigit():
            digits.append(x)
    score = int(digits[0]+digits[-1])
    ans += score
print(ans)
'''

#Part 2
'''
for entry in input_list:
    digits = []
    for x,y in enumerate(entry):
        if y.isdigit():
            digits.append(y)
        for x2,y2 in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
            if entry[x:].startswith(y2):
                digits.append(str(x2+1))
    ans += int(digits[0]+digits[-1])
print(ans)
'''