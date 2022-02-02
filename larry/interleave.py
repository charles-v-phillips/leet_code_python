def interleave(s1,s2):
    def helper(i1,i2,partial):
        if i1 == len(s1)  and i2 == len(s2) :
            rv.append(partial)
            return
        if i1 < len(s1):
            helper(i1 +1, i2, partial + s1[i1])
        if i2 < len(s2):
            helper(i1, i2 + 1, partial + s2[i2])


    rv = []
    helper(0,0,'')
    return rv

print(interleave('abc','XY'))