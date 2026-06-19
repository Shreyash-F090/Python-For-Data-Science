def list (a, m, n):
    a[m], a[n] = a[n], a[m]
    return a
a = ["basketball", "cricket", "kabbadi", "football", "hockey", "batminton"]
print("original list", a)
index1 = 1
index2 = 4

A = list(a, index1, index2)
print("update list", A)
