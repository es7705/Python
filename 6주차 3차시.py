# 163페이지 1번
'''
s = 0
for i in [1, 3, 5, 7, 9]:
    s = s + i
    print(i,s)
'''

# 163페이지 2번
'''
subject = ['국어', '영어', '수학', '과학', '한국사']
for i in subject:
    print(i, end = ' ')
'''

# 163페이지 3번
'''
name = ['홍길동', '임꺽정']
subject = ['국어', '영어', '수학']
for i in name:
    for j in subject:
        print(i, j)
'''

# 164페이지 4번
'''
s = 0
for i in range(1, 101): # range(1, 101, 1)로 해도 됨
    s = s + i
print(s)
'''

# 164페이지 5번
'''
s1 = 0
s2 = 0
for i in range(1, 101):
    if i % 2 == 0 :
        s1 = s1 + i
    else:
        s2 = s2 + i
print('짝수합 : ' ,s1)
print('홀수합 : ' ,s2)
'''

# 164페이지 6번
'''
s = 0
for i in range(3, -4, -1):
    print(i, end = ' ')
    s = s + i
print('')
print(s)
'''

# 170페이지 1번
'''
import sys
maxnum = -sys.maxsize - 1
minnum = sys.maxsize
num = [8, 7, 3, 2, 9, 4, 1, 6, 5]
for i in num:
    if i > maxnum :
        maxnum = i
    if i < minnum :
        minnum = i
        minnum = i
print('최댓값 : ', maxnum)
print('최솟값 : ', minnum)

print('최댓값 : ', max(num))
print('최솟값 : ', min(num))
'''

# 167페이지 12번
'''
for i in range(1 ,6):
    for j in range(1, 5):
        print('*', end = '')
    print('')
'''

# 172페이지 6번
'''
for i in range(6):
    for j in range(1, i + 1):
        print('*', end = '')
    print('')
'''

# 173페이지 8번
'''
for i in range(1, 6) :
    for j in range(1, 6 - i):
        print(' ', end = '')
    for j in range(1, i + 1):
        print('*', end = '')
    print('')
'''



