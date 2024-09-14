# 150 페이지
'''
i = 1
while i <= 5:
    print(i, end = " ")
    i = i + 1
print("")
print(i)
'''

# 151페이지 프로그램 06-03
'''
n = 1
s = 0
while n <= 10:
    if n % 2 == 0:
        s = s + n
    n = n + 1
print('s : ', s)

n = 1
s = 0
while n <= 10:
    if n % 2 == 0:
        s = s + n
        print('n : ', n, ' ,s : ', s)
    n = n + 1
print('s : ', s)
'''

# 152페이지 Tinking p158 4번
'''
n = 1
s = 0
while n >= 10:
    if n % 2 == 0:
        s = s + n
    n = n + 1
print('s : ', s)
'''

# 152페이지 Tinking p159 5번
'''
n = 1
s = 0
while n <= 10:
    if n % 2 == 0:
        s = s + n
    n = n - 1
print('s : ', s)
'''

# 152페이지 Tinking p160 6번
'''
n = 1
s = 0
while n <= 10:
    if n % 2 == 0:
        s = s + n
        print('n : ', n, 's : ', s)
    n = n + 1
print('n : ', n, 's : ', s)
'''

# 152페이지 잠깐코딩 4번 p162
'''
n = 2
s = 0
while n <= 10:
    s = s + n
    print('n : ', n, ',s : ', s)
    n = n + 2
print('s : ', s)
'''

# 152페이지 잠깐코딩 5번 p162
'''
n = 9
s = 0
while n >= 1:
    s = s + n
    print('n : ', n, ',s : ', s)
    n = n - 2
print('s : ', s)
'''

#155페이지 프로그램 06-04
'''
s = 0
for i in range(1, 21):
    if i % 2 == 1:
        continue
    s = s + i
    print('i : ', i, 's : ', s)
    if s > 30:
        break
print('i : ', i, 's : ', s)
'''

#156페이지 잠깐 코딩 6번 p162
'''
s = 0
for i in range(1, 21):
    if i % 2 == 0:
        continue
    s = s + i
    print('i : ', i, 's : ', s)
    if s > 30:
        break
print('i : ', i, 's : ', s)
'''

