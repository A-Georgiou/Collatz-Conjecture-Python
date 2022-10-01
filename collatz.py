appendCollatz = []

#Define Collatz Conjecture Function
def collatz(number: int) -> int:
    appendCollatz.append(number)
    if number <= 0:
        print("Only non-negative Integers allowed")
    count = 0
    while number != 1:
        if number % 2:
            number = number * 3 + 1
        else:
            number //= 2
        appendCollatz.append(number)
        count += 1 #Number of Steps Taken
    return count

result = input("Enter non-negative number: ")
print(f"Number of steps: ", collatz(int(result)))
print("Steps Taken:", appendCollatz)
