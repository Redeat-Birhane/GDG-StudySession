def largest_number():
    numbers=[]
    count=int(input("Enter the number of  elements you wish to have in a list:"))
    for i in range(count):
        number=int(input(f'Enter number {i+1}'))
        numbers.append(number)
    return f'The largest number is {max(numbers)}'
print(largest_number())
