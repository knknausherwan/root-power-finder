# User input for processing
user_inpt = int(input('Please enter a integer: '))

# Enter control variables
root = 0

# Identify root**pwr value that equals the entered integer
while True:
    for pwr in range(0, 6):
        if root**pwr == user_inpt:
            print(f'The following root {root} and power {pwr} equal to the users entered input {user_inpt}')
            break

    if root**pwr == user_inpt:
        break

    root += 1

    if root == 100:
        print(f'No pair of root and power exists to equal the value entered by the user')
        break
