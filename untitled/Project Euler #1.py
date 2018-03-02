# ------
print("This program will take a number, x, then add up all multiples of 3 and 5 up to that number and")
print("display it.")
print("")
# ------

# Input
x = int(input("Go ahead and enter a positive integer: "))

# Set your current sum
my_sum = 0

for i in range(0, x):
    if i % 3 == 0 or i % 5 == 0:
        my_sum += i
        i += 1
# The print() function goes out side of your loop so it doesn't display each iteration up to the end.
# It will only display the final iteration.
print(my_sum)


