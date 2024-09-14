#194페이지 1번
'''
def print_python():
    print('python')

print_python()
'''

#194페이지 2번
'''
def welcome():
    print('환영합니다.')

for i in range(3):
    welcome()
'''

#194페이지 3번
'''
def welcome(name):
    print('환영합니다.', name,'님')

n = input('이름:')
welcome(n)
'''

#195페이지 4번
'''
def print_str(st, cnt):
    for i in range(cnt):
        print(st)

s = input('문자열 : ')
c = int(input('횟수 : '))
print_str(s, c)
'''

#201페이지 7번
'''
def welcome(name, msg='환영합니다.'): # 디폴트 값: 환영합니다.
    print(msg, name, '님')

n = input('이름 :')
welcome(n) # 이름만 전달
welcome(n, '반갑습니다.') #이름과 환영메시지 전달 #디폴트값말고 반갑습니다로 바뀜
'''

#201페이지 8번
'''
def calc(num1, num2, act='+'):
    if act == '+':
        tmp = num1 + num2
    elif act == '-':
        tmp = num1 - num2
    elif act == '*':
        tmp = num1 * num2
    elif act == '/':
        tmp = num1 / num2
    else:
        tmp = '잘못된 연산기호입니다.' # 여기 주의 할 것
    return tmp

n1 = int(input('정수1 : '))
n2 = int(input('정수2 : '))

print(calc(n1, n2))
print(calc(n1, n2, '*'))
print(calc(n1, n2, '^'))
'''

#202페이지 9번
'''
def calc(num1, num2, act='+'):
    if act == '+':
        tmp = num1 + num2
    elif act == '-':
        tmp = num1 - num2
    elif act == '*':
        tmp = num1 * num2
    elif act == '/':
        tmp = num1 / num2
    else:
        tmp = '잘못된 연산기호입니다.'
    return tmp

n1 = int(input('정수1 : '))
n2 = int(input('정수2 : '))

print(calc(n1, n2, '*')) #순서 그래로
print(calc(num1=n1, num2=n2, act='*')) #직접 num1과 num2에 n1,n2를 전달함
print(calc(num2=n2, num1=n1, act='*')) #순서가 바뀌어도 num1에는 n1, num2는 n2가 들어감
'''

#196페이지 10번
'''
def circle_area(radius):
    tmp = 3.141592 * radius * radius
    return tmp

r = int(input('반지름 : '))
print('반지름', r,'인 원의 넓이 :',circle_area(r))
'''

#196페이지 8번
'''
def pow(x, y):
    return x ** y
print('3 * 2**4 + 5 = ', 3 * pow(2, 4) + 5)
'''



























