# Replace the "ANSWER HERE" for your answer

def max_of_two(x, y):
    max1 = x or y
    if x > y:
        max1 = x
    elif x < y:
        max1 = y
    return max1
#max_of_two()
def max_of_three(x, y, z):
    max2 = x or y or z
    if max_of_two(x, y) > z:
        max2 = max_of_two(x, y)
    elif max_of_two(x, y) < z:
        max2 = z
    return max2
#max_of_three()