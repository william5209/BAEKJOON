h, m = map(int, input().split(' '))

if m >= 45:
    m -= 45
else:
    h -= 1
    m =m + 15
if h < 0:
    h += 24
    
print(h, m)