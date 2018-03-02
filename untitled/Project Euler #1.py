# ------
print("This program will take a number, x, then add up all multiples of 3 and 5 up to that number and")
print("display it.")
print("")
# ------

# Input
x = int(input("Go ahead and enter a positive integer: "))

my_sum = 0

for i in range(0, x):
    if i % 3 == 0 or i % 5 == 0:
        my_sum += i
        i += 1
print(my_sum)

# This is out of your while loop so that all the sums aren't displayed.


