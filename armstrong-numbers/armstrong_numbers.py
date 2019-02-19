def is_armstrong(number):
    numbers = [int(n) for n in str(number)]
    length = len(numbers)

    total = 0
    for num in numbers:
        total += num**length

    return total == number
