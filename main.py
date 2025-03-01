print("Hello, world")
print("Changed")

def find_maximum(numbers):
    if not numbers:
        return "Список пуст."
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum