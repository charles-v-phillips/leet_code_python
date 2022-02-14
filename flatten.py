def flatten(l):
    rv = []
    if not isinstance(l,list):
        return [l]
    for e in l:
        rv.extend(flatten(e))
    return rv


# Uncle Larrys Way
def flatten2(l):
    if isinstance(l, list):
        if (l == []):
            return l
        else:
            lft = flatten(l[0])
            rht = flatten(l[1:])
            lft.extend(rht)
            return lft
    else:
        return [l]

# print(flatten([1,[2,[3,7],[1,2,3],4]]))
print(flatten([1,2,3,4,5]))
