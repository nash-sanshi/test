squares = []
for value in range(1,11):
    squares.append(value**2)
    print(squares)
print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)

print([value**2 for value in range(1,11)])