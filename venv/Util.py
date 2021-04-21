def tupleToNestedList(data):
    # convert tuple back into nested list so it looks nice and clean in CSV
    temp = []
    # Getting elem in list of list format
    for elem in data:
        temp2 = elem.split(', ')
        temp.append((temp2))

    # List initialization
    list = []

    # Using Iteration to convert
    # element into list of list
    for elem in temp:
        temp3 = []
        for elem2 in elem:
            temp3.append(elem2)
            list.append(temp3)
    return list

def convert(list):
    return tuple(list)

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3