# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("you can't divide by zero")


# if the code inside the try block works, python will skip over the except block.


print("give me two numbers and I will divide them")
print("\nEnter q to quit")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nEnter second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/ int(second_number)
    except ZeroDivisionError:
        print("you can't divide by zero")
    else:
        print(answer)


# you can wrap the line that might cause errors in a try/except/else block
