# import random
# for i in range(10):
#     random_pixel=random.randint(0,3)
#     print(random_pixel)


# import numpy as np
# a=[]
# a.append(np.array([1,2]))
# a.append(np.array([1,2]))
# a.append(np.array([1,2]))
# print(a)
# a=np.array(a)
# print(a)
#
# for c in a:
#     for b in c:
#         b=0
# print(a)



# from math import sqrt
#
# a=pow(2,2)
# print(a)
# b=pow(2,3,5)
# print(b)
# print(sqrt(2))

d = {1: 20, 4:15, 2: 10, 3: 50}
items=list(d.items())
print(items)
print(type(items))
print(type(items[0]))
n=sorted(items, key=lambda center: center[1])
print(n)
indexs=[x[0] for x in sorted(items, key=lambda center: center[1], reverse=True)]
print(indexs)
