def add_numbers():
    numbers=[]
    summ=0
    count=int(input("Enter how many numbers you want to add:"))
    for i in range(count):
        number=int(input(f'Enter number:{i+1}'))
        numbers.append(number)
    summ=sum(numbers)
    return f'The total sum of the numbers is: {summ}'
print(add_numbers())