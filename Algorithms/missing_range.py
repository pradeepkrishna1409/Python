arr = [88, 105, 3, 2, 200, 0, 10]

hm = [0] * 100

for num in arr:
    if num < 99:
        hm[num] = 1

print hm

start = 0
end = 0

i = 0
while i <= 99:
    if hm[i] == 0:
        j = i + 1
        while j <= 99 and hm[j] == 0:
            j += 1

        print "Range is ", i, ' to ', j

        i = j
    else:
        i += 1
