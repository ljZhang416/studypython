# 3.将10000以内的所有素数存于列表中,求这些素数的和

L = [2,]
for i in range(3, 10000):
    for j in range(2, i+1):
        if i % j == 0:
            break
        elif j == i-1:
            L.append(i)
print(L)
print(sum(L))
