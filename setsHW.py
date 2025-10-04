

# Function to find symmetric difference between two sets
def find_symmetric_difference(set1, set2):
    result = set1.symmetric_difference(set2)
    return result

#SETS
# A
set1_A = {'blue', 'green'}
set2_A = {'blue', 'yellow'}

# B
set1_B = {1, 2, 3, 4, 5}
set2_B = {1, 5, 6, 7, 8, 9}

# Calculating Symmetric Difference
result_A = find_symmetric_difference(set1_A, set2_A)
result_B = find_symmetric_difference(set1_B, set2_B)

# Display Results
print("A. Symmetric Difference =", result_A)
print("B. Symmetric Difference =", result_B)
