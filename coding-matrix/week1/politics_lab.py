voting_data = list(open("voting_record_dump109.txt"))
#print(voting_data)

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    dct = dict()
    for line in voting_data:
        lst = line.split()
        dct[lst[0]] = [int(i) for i in lst[3:]]
    return dct
    

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    total = 0
    voting_a = voting_dict[sen_a]
    voting_b = voting_dict[sen_b]
    for i in range(len(voting_a)):
        total += voting_a[i] * voting_b[i]
    return total


## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    keys = voting_dict.keys()
    min_value = -len(keys)
    min_key = None
    for k in keys:
        if k != sen:
            comp = policy_compare(k, sen, voting_dict)
            #print(comp, k)
            if comp > min_value:
                min_value = comp
                min_key = k
    return min_key

#vd = {'Klein': [1,2,3], 'Fox-Epstein': [3,-2,0], 'Ravella': [-1,2,1], 'John':[1,1,3], 'Jane': [0,-3,2]}
#print(most_similar('Klein', vd))
    

## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    keys = voting_dict.keys()
    max_value = len(keys) 
    for k in keys:
        if k != sen:
            comp = policy_compare(k, sen, voting_dict)
            if comp < max_value:
                max_value = comp
                max_key = k
    return max_key
    
    

## Task 5

most_like_chafee    = most_similar("Chafee", create_voting_dict())
least_like_santorum = least_similar("Santorum", create_voting_dict())



# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    total = 0
    n = len(sen_set)
    for k in sen_set:
       total += policy_compare(sen, k, voting_dict) 
    return total/n

def find_most_average():
    voting_dict = create_voting_dict()
    keys = voting_dict.keys()
    dct = dict()
    for k in keys:
        dct[k] = find_average_similarity(k, keys, voting_dict)
    max_key= list(keys)[0]
    max_value= dct[max_key]
    
    for k in dct.keys():
        if dct[k] > max_value:
            max_value = dct[k]
            max_key = k
    return max_key
most_average_Democrat =  find_most_average() # give the last name (or code that computes the last name)
#print(most_average_Democrat)
#print(find_most_average())


# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    n = len(sen_set)
    all_record = [ voting_dict[sen] for sen in sen_set]
    result = [ 0 for i in all_record[0]]
    for record in all_record:
        result = [ result[j]+record[j] for j in range(len(record))]
    for i in range(len(result)):
        result[i] /= n
    return result

def find_all_democrats():
    dct = set()
    for line in voting_data:
        lst = line.split()
        if lst[1] == 'D':
            dct.add(lst[0])
    return dct
 

average_Democrat_record = find_average_record(find_all_democrats(), create_voting_dict()) # (give the vector)
#print(find_average_record({'A','B', 'C','D'}, {'A':[1,2], 'B':[3,4], 'C':[2,1], 'D':[1,1], 'E':[1,1]}))
#d = create_voting_dict()
#print(find_average_record({'Clinton', 'Reed', 'Reid'}, d))
#print(average_Democrat_record)

# Task 8
def disagree_count(sen_a, sen_b, voting_dict):
    count = 0
    voting_a = list(voting_dict[sen_a])
    voting_b = list(voting_dict[sen_b])
    for i in range(len(voting_a)):
        count += voting_a[i]*voting_b[i]
    return count

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    sen_list =list(voting_dict.keys())
    max_count = len(sen_list)
    result = None
    dct = dict() 
    length = len(sen_list)
    for i in range(length):
        for j in range(i+1, length):
            cur_count = disagree_count(sen_list[i], sen_list[j], voting_dict)
            #print(cur_count)
            if cur_count <= max_count:
                max_count = cur_count
                result = (sen_list[i], sen_list[j])

    return tuple(set(result))
#print(sorted(bitter_rivals({'A':[1,1,1],'B':[-1,-1,0],'C':[-1,-1,-1]})))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
