# d={"username":"Vaish","password":"12345"}
# column="'"+"','".join(d.keys())+"'"
# print(column)
# # print(type(column))
# values=""
# for i in range(len(d)):
#     values+="'%s'"+","
# print(values[:-1])
# t=tuple(d.values())
# print(t)
def isAnagram(a,b):
        d={}
        for i in a:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for j in b:
            if j in d and b.count(j)==d[j]:
                return True,b.count(j),d[j]
            else:
                return False,b.count(j),d[j]

result=isAnagram('aabaa','baaaaa')
print(result)