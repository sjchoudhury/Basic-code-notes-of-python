nums=[1,2,3,4,9,9,5,4]
d=dict()
for num in nums:
    d[num]=d.get(num,0)+1
print(d)
for key in d:
    if d[key]==2:
        print(key)
#
