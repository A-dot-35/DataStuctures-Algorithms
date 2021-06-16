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

'''
    Description: Function that returns two pairs such that a+b = c+d. Return only the first two pairs found.
    Input: List of distinct Integers
    Output: 2D list with pairs where a+b = c+d 
    Time Complexity: O(n^2)
    Space Complexity: O(n)
'''
def find_pair(my_list):

    if(len(my_list) < 4):
        return None
    myDict = {}
    result = []
    for i in range(len(my_list)):
        for j in range(i+1,len(my_list)):
            pair_sum = my_list[i] + my_list[j]
            if(pair_sum not in myDict):
                myDict[pair_sum] = [my_list[i],my_list[j]]
            else:
                result.append(myDict[pair_sum])
                result.append([my_list[i],my_list[j]])
                return result
    return result

'''
    Description: Function that returns True or False if the sublist of a list amounts to zero
    Input: List of positive and negative integers
    Output: True or False wheather a sublist exist where the sum = 0 
    Time Complexity: O(n)
    Space Complexity: O(n)
'''
def find_sub_zero(my_list):   
    my_dict = {}
    total_sum = 0

    for elem in my_list:
        total_sum += elem
        if elem is 0 or total_sum is 0 or my_dict.get(total_sum) != None:
            return True
        my_dict[total_sum] = elem
    return False
'''
    Description: Function that returns True or False if it finds the words from an input in the dictionary of words given.
    The input of the word would only contain two words.
    Input: dictionary of words as list and string of char containing up to two words
    Output: True or False words are found in dictionary given 
    Time Complexity: O(n^2)
    Space Complexity: O(n)
'''

def is_formation_possible(lst, word):
    # Write your code here
    myDict = {}

    for w in range(len(lst)):
        myDict[lst[w]] = w
    
    for s in range(1,len(word)):
        word_one = word[0:s]
        word_two = word[s:len(word)]
        print(word_one)
        print(word_two)
        if(myDict.get(word_one) != None and myDict.get(word_two)!= None):
            return True
    
    return False

'''
    Description: Function that resturns two numbers within a list that up to k
    Input: list of integers and number k
    Output: a list of two numbers that add up to k
    Time Complexity: O(n)
    Space Complexity: O(n)
'''
def findSum(lst, k):
    # Write your code here
    if(len(lst) < 2):
        return []
    myDict = {}
    res = []

    for i in range(len(lst)):
        myDict[lst[i]] = i
    
    for num in range(len(lst)):
        target = k - lst[num]
        if(myDict.get(target) != None):
            if(myDict.get(target) != num):
                res.append(lst[num])
                res.append(target)
                return res
    
    return res

'''
    Description: A function that returns the first unique integer in the list. Unique means the number does not repeat and 
    appears only once in the whole list.
    Input: List of integers
    Time Complexity: O(n+n) => O(n)
    Space Complexity: O(n)
'''
def first_unique(lst):
    if(len(lst) == 0):
        return -1
    dict_count = {}
    for num in lst:
        if(dict_count.get(num) == None):
            dict_count[num] = 1
        else:
            dict_count[num] += 1

    for num in lst:
        if(dict_count[num] == 1):
            return num
        
    return -1 
'''
    Description: this function returns true or false if there is a loop in a linked list.
    Input: Linked list
    Output: Boolean stating if there is a loop or not
    Time Complexity: O(n) worst O(n^2)
    Space Complexity: O(n)
'''

def detect_loop(lst):
    # Write your code here
    temp = lst.get_head()
    myDict = {}
    while(temp != None):
        if(myDict.get(temp) != None):
            return True 
        myDict[temp] = temp.data
        temp = temp.next_element
    return False
'''
    Description: This function removes duplicates from a linked list.
    Input: Linked List
    Output: Linked List
    Time Complexity: O(n)
    Space Complexit: O(n)
'''


def remove_duplicates(lst):
    prev = None 
    temp = lst.get_head()
    myDict = {}
    while(temp != None):
        if(myDict.get(temp.data) != None):
            prev.next_element = temp.next_element
            temp = temp.next_element
        else:
            myDict[temp.data] = temp
            prev = temp
            temp = temp.next_element
    
    return 

