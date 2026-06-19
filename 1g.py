A = [90, 84, 122, 106, 104, 140, 67, 42, 80, 8]
print("original list :", A)
A.pop(1)
X = max(A)
Y = min(A)
A.append(100)
Z = sorted(A)
R = sorted(A, reverse = True)
Avg = sum(A)/len(A)
print("Maximum value :",X)
print("minimum Value:",Y)
print("accending order",Z)
print("Descending order",R)
print("AVG Number",Avg)




