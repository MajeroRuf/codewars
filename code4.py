"""Your goal in this kata is to implement a difference function,
which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b.
array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:
array_diff([1,2,2,2,3],[2]) == [1,3]"""

def array_diff(a, b):
    if not b:
        return a
    elif not a:
        return a
    else:
        c = a.copy()
        for el in b:
            for el1 in a:
                if el1 == el:
                    try:
                        c.remove(el1)
                    except ValueError as err:
                        print(err)
        return c

# def array_diff(a, b):
#     return [x for x in a if x not in b]


print(array_diff([1, 2, 2], [3]))
print(array_diff([-17, -13, 19, -20], [-20, 19]))
print(array_diff([11, 6, -8, -17, -9, -12],[-19, -11, -16]))
print(array_diff([], [1, 2, 2]))
print(array_diff([1, 2, 2], []))