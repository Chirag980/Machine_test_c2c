arr1= [3,10,4,21,45,2,12]

arr2=[13,1,3,2,22,4,45,17]
# 1.
# [1,2,3,4,10,12,13,17,21,22,45]
# 2.
# [3,4,45]




def unique_value(arr1,arr2):
    final_list= arr1+arr2
    return final_list
unique= set(unique_value(arr1,arr2))
# unique.sort()
list1=list(unique)
list1.sort()
print('Unique Value: ',list1)


def common_value(arr1,arr2):
    arr1_set =set(arr1)
    arr2_set = set(arr2)
    if(arr1_set & arr2_set):
        print('common value: ',list(arr1_set & arr2_set))
    else:
        print('No Common value')

common_value(arr1,arr2)