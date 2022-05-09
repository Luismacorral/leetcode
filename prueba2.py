
strs=["xitaobus", "xita", "xitadum","xitem", "xitadam", "xitaxita"]

ans = ''
n = len(min(strs))
print("n: ",n)
n2 = min(strs)
print("n2: ", n2)
for i in range(n):
    
    if all(x[i]==strs[0][i] for x in strs):

        ans = ans + strs[0][i]
        
        print("strs[0][i]", strs[0][i])
        print("i: ",i)
        print("ans: ", ans)
    else:
        break

print(ans)
