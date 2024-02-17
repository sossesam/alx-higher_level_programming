#!/usr/bin/python3
def find_peak(list_of_integers):
    length_of_integers = len(list_of_integers)
    
    if length_of_integers == 0:
        return None
    
    if length_of_integers == 1:
        return list_of_integers[length_of_integers - 1]
    
    mid = int(length_of_integers // 2)

    if length_of_integers == 2:
        if list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]
        else:
            return list_of_integers[1]
        
    if length_of_integers == 3:
        if list_of_integers[mid] >= list_of_integers[mid + 1] and list_of_integers[mid] >= list_of_integers[mid - 1]:
            return list_of_integers[mid]
        else:
            return max(list_of_integers[0], list_of_integers[length_of_integers - 1])

    if length_of_integers >= 4:
        max_left = find_peak(list_of_integers[mid:])
        max_right = find_peak(list_of_integers[:mid])
        return max(max_left, max_right)

