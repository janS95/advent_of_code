f = open('input.txt','r')

numbers = f.read().split('\n')

del numbers[-1]

numbers = list(map(int,numbers))

print(numbers)

for idx,num1 in enumerate(numbers):
    for idx2,num2 in enumerate(numbers[idx:]):
        for num3 in numbers[idx:]:
            if num1+num2+num3 == 2020:
                print('gefunden')
                print(num1 * num2 * num3)
