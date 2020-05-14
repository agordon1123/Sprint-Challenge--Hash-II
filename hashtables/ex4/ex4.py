def has_negatives(a):

    """
    YOUR CODE HERE
    """
    # what does -1, 1, 1, 2 return ?
    # I'll assume duplicates are fine- it's not pairs
    # [ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]

    d = {}
    for i in a:
        if (i * -1) in d:
            d[(i * -1)] = True
        elif i not in d:
            d[i] = False
    result = []
    for key in d.keys():
        if d[key]:
            if key < 0:
                key = key * -1
            result.append(key)
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
