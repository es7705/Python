#173페이지 9번 시험 나옴
'''
for i in range(1 ,6):
    for j in range(1, 6 - i): # 공백
        print(' ', end = '')
    for j in range(1, i + 1): # 왼쪽 삼각형 별 갯수 1 ,2 ,3 ,4 ,5
        print('*', end = '')
    for j in range(1, i):
        print('*', end = '') # 오른쪽 삼각형 별 갯수 0, 1, 2, 3, 4
    print('') # 줄바꿈
'''

#168페이지 14번
'''
s = 0
n = int(input('정수 : '))
while n != 0 :
    s = s + n
    n = int(input('정수 : '))
print('합 : ', s)
'''

#168페이지 15번
'''
pw = ' '
while pw != 'pwpass' :
    pw = input('비밀번호 : ')
print('LogIn Pass')
'''


#168페이지 16번
'''
s = 0
while True:
    n = int(input('정수 : '))
    if n > 0:
        s = s + n
    elif n < 0 :
        continue
    else :
        break
print('합 : ', s)

s = 0
while True:
    n = int(input('정수 : '))
    if n < 0 :
        continue
    if n == 0 :
        break
    s = s + n
print('합 : ', s)
'''

# 176페이지 14번
'''
h = 1
cnt = 0
while True :
    h = h * 2
    cnt = cnt + 1
    print(cnt, '번 접으면', h, 'mm')
    if h > 100000:
        break
print('횟수 : ', cnt , '두께', h)
'''
