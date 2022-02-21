#######################################
# Calculate_the_sum_of_Element_in_an_Array
#######################################
arr = [1,2,3,4,5,6,7,8,9]
'''print(sum(arr))''' #### Using inbuilt function SUM #####
sum =0
for i in range(len(arr)):
    sum = sum +arr[i]
print(sum)