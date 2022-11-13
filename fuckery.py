

from collections import OrderedDict

d = OrderedDict()

d[1] = 1
d[2] = 5
d[-1] = "Foo"

print(d)
d.get(1)
d.move_to_end(1)
print(d)




            

