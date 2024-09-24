def bolish(lst, son):
    res = []
    
    for i in range(0, len(lst), son):
        res.append(lst[i:i + son])
    
    return res

n = int(input("Sonni kiriting >>> "))
st = ["A", "B", "C", "D", "E", "F", "G", "L", "Q", "U"]

res = bolish(st, n)
print(res)

