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
# 
def countPairs(arr1=[1,3,5,7], arr2=[2,3,5,8], M=4, N=4, x=10):
    count=0
    for number in arr1:
        target=x-number
        result=binary_search(arr2,N,target)
        if result != -1:
            count+=1
    return count
def binary_search(arr2,N,target):
    start=0
    end=N-1
    while start<=end:
        mid=(start+end)//2
        if arr2[mid]<target:
            start=mid+1
        elif arr2[mid]>target:
            end=mid-1
        elif arr2[mid]==target:
            return 1
    else:
        return -1
result=countPairs(arr1=[1,3,5,7], arr2=[2,3,5,8], M=4, N=4, x=10)
print(result)