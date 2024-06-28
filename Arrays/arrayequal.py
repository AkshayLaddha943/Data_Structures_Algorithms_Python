def checkarr(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    
    arr1.sort()
    arr2.sort()
    
    for i in range(0,len(arr1)):
        if (arr1[i] != arr2[i]):
            return False
    
    return True

if __name__ == "__main__":
    arr1 = [3, 5, 2, 5, 2]
    arr2 = [2, 3, 5, 5, 2]
 
    if (checkarr(arr1, arr2)):
        print("Yes")
    else:
        print("No")