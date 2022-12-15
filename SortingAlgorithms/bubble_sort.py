def bubble(list_a):
     # Can not apply comparision starting with last item of list (No item to right)
    indexing_length = len(list_a) - 1
    sorted = False 

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            # unsorted if left > right
            if list_a[i] > list_a[i+1]: 
                sorted = False
                # Swap vals
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    return list_a


print(bubble([4,8,1,14,8,2,9,5,7,6,6]))