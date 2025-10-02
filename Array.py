import array as arr

#create an array
array_num = arr.array( 'i' , [1 , 3 , 5 , 3 , 7 , 9 , 3])
print("Original Array:" +str(array_num))

print("The number of occurrences of the number 3 in the said array: " +str(array_num.count(3)))

#reverse
array_num.reverse()
print("Reverse order of the values:" +str(array_num))