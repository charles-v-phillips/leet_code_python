def flatten(l):
    rv = []
    if not isinstance(l,list):
        return [l]
    for e in l:
        rv.extend(flatten(e))
    return rv


# Uncle Larrys Way
def flatten2(x):
    if isinstance(x, list):
        if (x == []):
            return x
        else:
            lft = flatten(x[0])
            rht = flatten(x[1:])
            lft.extend(rht)
            return lft
    else:
        return [x]

# print(flatten([1,[2,[3,7],[1,2,3],4]]))
print(flatten([1,2,3,4,5]))
