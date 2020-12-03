# while
num = 0
while num < 9:
    if num % 2 == 0:
        print('Even:', num)
    else:
        print('Odd:', num)
    num = num + 1

print('Bye')

# for
names = ['neha', 'harry', 'ron']
for name in names:
    print(name)

# for with 2 variables
for name, index in zip(names, range(0, len(names))):
    print('Name', index, ':', name)



