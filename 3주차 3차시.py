# 86페이지 프로그램 04-01
'''
x = int(input('정수1 : '))
y = int(input('정수2 : '))
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)
'''

# 87페이지 잠깐 코딩 1번(97페이지)
'''
odd = 1+3+5+7+9
even = 2+4+6+8+10
diff = even - odd
print(odd, even, diff)
'''

# 87페이지 잠깐 코딩 2번(97페이지)
'''name = input('이름 :')
year = int(input('출생년도 :'))
age = 2022 - year + 1
print('나이 :', age)'''

# 88페이지 프로그램 p04-02 필요한 동전 개수 구하기
'''
x=int(input('금액 : '))
x500 = x // 500
x100 = x % 500
x100 = x100 // 100
print('500원 :', x500, '100원 :', x100)
'''

# 88페이지 Thinking 3번(95페이지)
'''
x = int(input('정수1 :'))
y = int(input('정수2 :'))
print(x / y) #나누기 연산자는 결과가 실수로 나옴
print(x // y) # 나머지 연산자는 결과가 정수로 나옴
'''

# 88페이지 잠깐 코딩 3번(97페이지)
'''
x = int(input('금액 :'))
x500 = x // 500 # 1
t = x % 500 # 270
x100 = t // 100 # 2
t = t % 100 # 70
x50 = t // 50 # 1
t = t % 50 # 20
x10 = t // 10 # 2
print('500원 :', x500, '100원 :', x100, '50원 :', x50, '10원 :', x10)
'''

# 89페이지 다중 대입문
'''
a = b = c = 1
print(a, b, c)
x, y = 3, 4
print(x, y)
x, y = y, x
print(x, y)
'''













