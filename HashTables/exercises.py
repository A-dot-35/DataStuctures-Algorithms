# Will use python dictionaries as it provides same functionalities as own implementation

'''
    Description: Function that returns wheather a list is a subset of another.
    Input: list1 and list2. Neither contain duplicate values
    Output: Boolean 
    Time Complexity: O(m+n)
    Space Complexity: O(n)
'''
def is_subset(list1, list2):
    mySet = set()
    smaller_list = []

    if(len(list1) > len(list2)):
        mySet.update(list1)
        smaller_list = list2
    else:
        mySet.update(list2)
        smaller_list = list1
    
    for num in smaller_list:
        if(num not in mySet):
            return False
    
    return True

'''
    Description: Function that returns wheather two lists are disjoint or not. The two lists are disjoint i no value of list1 appears in list2.
    Input: list1 and list2. There are no duplicate values
    Output: Boolean
    Time Complexity: O(n+m)
    Space Complexity: O(n)
'''
def is_disjoint(list1,list2):
    if(len(list1) == 0 or len(list2) == 0):
        return True
    mySet = set()
    mySet.update(list1)

    for item in list2:
        if(item in mySet):
            return False
    
    return True

'''
    Description: Function that returns a list of all symmetric pairs from an input list. A symmetruc pair means that in (a,b) and (c,d) a = d and b = c
    Input: 2D List, list of pairs
    Output: 2D List, list of symmetric pairs
    Time Complexity: O(n)
    Space Complexity: O(n)
'''
def find_symmetric(pair_list):
    if(len(pair_list) == 0):
        return None
    pair_set = set()
    result = []

    for pair in pair_list:
        pair_tup = tuple(pair)
        pair.reverse()
        reverse_tup = tuple(pair)
        
        if(reverse_tup in pair_set):
            result.append(list(pair_tup))
            result.append(list(reverse_tup))
        else:
            pair_set.add(pair_tup)
    return result

'''
    Description: Function that returns the correct complete journey from a given list of source:destination pairs. Assume there is always a complete journey.
    Input: Dictionary, source:destination
    Output: 2D list: [sournce,destination] 
    Time Complexity:
    Space Complexity:
'''
def trace_path(journey_dict):
    if(len(journey_dict) == 0):
        return None
    if(len(journey_dict) == 1):
        return [[]]
    starting_point = None
    reverse_dict = {}
    result = []
    for key in journey_dict.keys():
        reverse_dict[journey_dict[key]] = key
    
    for key in reverse_dict.keys():
        if(reverse_dict[key] not in reverse_dict):
            starting_point = reverse_dict[key] 
            break
    
    while(starting_point in journey_dict):
        result.append([starting_point, journey_dict[starting_point]])
        starting_point = journey_dict[starting_point]
    return result