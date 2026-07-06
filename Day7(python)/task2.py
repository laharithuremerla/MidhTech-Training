dialpad = [
    ["1", "2", "3"],
    ["4", "5","6",],
    ["7", "8", "9"],
    ["*", "0", "#"],
]
for row in dialpad:
    for item in row:
        print(item, end=" ")
    print()