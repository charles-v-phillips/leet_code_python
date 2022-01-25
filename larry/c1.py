l = [2,[3,4,[5,6]],7,8,['c',2.3]]
l2 = [2,[3,4],[5]]
l3 = []

def count_elements(l):
    if isinstance(l,list):
        head, *tail = l
        if len(l) > 1:
            return count_elements(head) + count_elements(tail)
        else:
            return count_elements(head)

    return 1



# Destructuring 
if __name__ == '__main__':
    head, next, *rest = [1,2,3,4,5]
    print(head, next, rest)


