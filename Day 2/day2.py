from collections import defaultdict

ans = 0
input_file = open("Day 2/input.txt", 'r')
input_list = input_file.read().splitlines()
input_file.close()

# Part 1
'''
for line in input_list:
    valid_game = True
    gameId, line = line.split(':')
    for cubes_grabbed in line.split(';'):
        for cubes in cubes_grabbed.split(','):
            n, color = cubes.split()
            if int(n) > {'red': 12,
                         'green': 13,
                         'blue': 14}.get(color, 0):
                valid_game = False
    if valid_game:
        ans += int(gameId.split()[-1])
print(ans)
'''

# Part 2
'''
for line in input_list:
    gameId, line = line.split(':')
    max_blocks = defaultdict(int)
    for cubes_grabbed in line.split(';'):
        for cubes in cubes_grabbed.split(','):
            n, color = cubes.split()
            max_blocks[color] = max(max_blocks[color], int(n))
    scorer = 1
    for entry in max_blocks.values():
        scorer *= entry
    ans += scorer
print(ans)
'''