num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even , odd = 0, 0
for i in num :
    if i % 2 == 0:
        even += 1
    else :
        odd += 1

print("even : ", even)
print("odd : ", odd)