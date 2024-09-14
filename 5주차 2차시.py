# 잠깐 코딩 8번 130페이지
'''
num = int(input('정수 :'))
if num == 0:
    print('0')
elif num > 0:
    print('양수')
else :
    print('음수')
'''

# 132페이지 코딩 프로그래밍 3번
'''
num = int(input('정수 :'))
if num < 100 :
    print(num)
'''

# 133페이지 코딩 프로그래밍 8번
'''
num = int(input('정수 :'))
if num % 2 == 0 :
    print('짝수')
'''

# 134페이지 코딩 프로그래밍 9번
'''
num = int(input('정수 :'))
if num % 2 == 0 :
    print('짝수')
else :
    print('홀수')
'''

# 135페이지 코딩 프로그래밍 1번
'''
num = int(input('정수 :'))
if num < 100:
    print(num * 0.9)
else :
    print(num * 1.1)
'''

# 136페이지 코딩 프로그래밍 2번
'''
a = int(input('정수1 :'))
b = int(input('정수2 :'))
tmp = a + b - b*b
if tmp >= 0 :
    print(tmp)
else :
    print('음수')
'''

# 136페이지 코딩 프로그래밍 3번
'''
num = int(input('정수:'))
if num % 2 == 0 and num % 3 == 0 :
    print('나누어짐')
else :
    print('나누어지지 않음')
'''

# 137페이지 코딩 프로그래밍 5번
'''
a = 5
b = 3
ch = input('연산자 :')
if ch == '+':
    tmp = a + b
elif ch == '-' :
    tmp = a - b
elif ch == '*':
    tmp = a * b
elif ch == '/':
    tmp = a / b
else :
    tmp = '잘못된 연산자'
print(a, ch, b, '=', tmp)
'''