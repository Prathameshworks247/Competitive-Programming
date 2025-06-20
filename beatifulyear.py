y = int(input())

while True:
    y = y+1

    digits = [int(digit) for digit in str(y)]
    if len(digits) == len(set(digits)):
        print(y)
        break