# 181페이지
'''
def fpython():
    print('python')
    print('파이썬')
fpython()

def ifpython():
    print('python')
print('파이썬')
ifpython()
'''

# 181페이지  TIP
'''
ifpython()
def ifpython():
    print('python')
print('파이썬')
'''
# 182페이지 프로그램 07-01
'''
# 1번
print('12345678')
print('홍길동')
print('12345678')
print('홍길동')
print('')

# 2번
for i in range(2):
    print('12345678')
    print('홍길동')
print('')

# 3번
def sn():
    print('12345678')
    print('홍길동')

sn()
sn()
print('')

# 4번
for i in range(2):
    sn()
'''

#184페이지 잠깐코딩1번 p192
'''
def print19():
    for i in range(1,10):
        print(i, end = ' ')
    print('')

print19()
'''

#185페이지 프로그램 07-2
'''
def cal_gugudan(dan):
    for i in range(1,10):
        print(dan, '*', i, '=', dan*i, '')

d = int(input('단 : '))
cal_gugudan(d)
'''

#186페이지 잠깐코딩 2번 p192
'''
def cal_gugudan(dan):
    for i in range(1,10):
        print(dan, '*', i, '=', dan*i, '')

d = int(input('단 : '))
if d >= 1 and d <= 9:
    cal_gugudan(d)
else :
    print('단은 1~9까지 입력해주세요.')

def cal_gugudan(dan):
    if d >= 1 and d <= 9:
        for i in range(1,10):
            print(dan, '*', i, '=', dan*i, '')
    else:
        print('단은 1~9까지 입력해주세요.')
d = int(input('단 : '))
cal_gugudan(d)
'''

#186페이지 잠깐코딩 3번 p193
'''
def print19(st,ed):
    for i in range(st, ed+1):
        print(i, end = ' ')
    print('')
s = int(input('시작값 : '))
e = int(input('끝값 : '))
if s < e :
    print19(s, e)
else:
    print('시작값이 끝값보다 작아야 합니다.')
'''

# 188페이지 프로그램 07-03
'''
def avg(a, b):
    s = (a + b) / 2
    return s
in1 = int(input('값1 : '))
in2 = int(input('값2 : '))
r = avg(in1, in2)
print('평균 = ',r)
'''

# 189페이지 잠깐 코딩 4번
'''
def avg(a, b, c):
    s = (a + b + c) / 3
    return s
in1 = int(input('값1 : '))
in2 = int(input('값2 : '))
in3 = int(input('값3 : '))
r = avg(in1, in2, in3)
print('평균 = ',r)
'''













