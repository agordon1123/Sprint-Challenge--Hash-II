def intersection(arrays):

    """
    YOUR CODE HERE
    """

    d = {}
    for array in arrays:
        for val in array:
            if val not in d:
                d[val] = False
            else:
                d[val] = val

    final = []
    for boolean in d.values():
        if boolean:
            final.append(boolean)

    return final


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
