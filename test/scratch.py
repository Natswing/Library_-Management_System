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
# 
def sort012(arr,n):
        j=0
        while j<n:
            if arr[j]==0:
                arr[n-j-1]==0
                j+=1
        while j<n:
            if arr[j]==1:
                arr[n-j-1]==1
                j+=1
        while j<n:
            if arr[j]==2:
                arr[n-j-1]==2
                j+=1
        return arr

result=sort012([0,2,1,2,0],5)
print(result)