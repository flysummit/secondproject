import numpy as np

# a=np.arange(0,5,1)
# print(a)
# b=np.arange(0,10,2)
# print(b)#

# a=np.zeros(10)
# print(a)
# a=np.ones(4)
# print(a)
# ary = np.array([1, 2, 3, 4, 5, 6])
# print(type(ary), ary, ary.shape)
# ary = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8]
# ])
# print(type(ary), ary, ary.shape)
# ary=np.array([1,2,3,4])
# print(ary,type(ary))
# ary.dtype='int64'
# print(ary,ary.dtype)
# ary=ary.astype('float64')
# print(ary,ary.dtype)

# ary = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8]
# ])
# print(ary.shape,ary.size,len(ary))
# a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(a,a.shape)
# print(a[0])
# print(a[0][0])
# print(a[0][0][0])
# for i in range(a.shape[0]):
#     for j in range(a.shape[1]):
#         for k in range(a.shape[2]):
#             print(a[i,j,k])

data = [
    ('zs', [50, 51, 52,100], 15),
    ('ls', [50, 44, 63,100], 16),
    ('ww', [88, 66, 93,100], 17)]
# ary=np.array(data,dtype='U2,3int32,int32')
# print(ary,ary[0][1])
# print(ary[2],['f0'])
# ary = np.array(data, dtype=[('name', 'str', 2),
#                             ('scores', 'int32', 3),
#                             ('age', 'int32', 1)])
# print("_"*45)
# print(ary,ary.dtype)
# print(ary[0]['age'])
# print(ary[1]['scores'])

# d=np.array(data,dtype={'name':('U2',0),'scores':('4int32',16),'age':('int32',28)})
# print(d[2]['name'],d[2]['scores'],d.itemsize)
a=np.arange(1,9)
# print(a)
b=a.reshape(2,4)
# print(b)
x=b.reshape(2,2,2)
# print(x)
d=x.ravel()
# print(d)
e=x.flatten()
# print(e)
a+=10
# print(a,e,sep='\n')
a.shape=(2,4)
print(a)
a.resize(2,2,2)
print(a)
