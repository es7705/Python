# 312페이지 잠깐 코딩 3번 p317
'''
st = input('Input : ')
st2 = st[0] + st[2]
print(st2)
'''

# 312페이지 잠깐 코딩 4번 p317
'''
st = input('Input : ')
if st.isalpha():
    st2 = st.upper()
    print(st, '>', st2)
elif st.isdigit():
    n = int(st) + 1
    print(st, '+ 1', n)
'''

#304페이지 프로그램 10-02
'''
def isbn_check(isbn):
    s = 0

    for i in range(len(isbn) - 1):
        if (i+1) % 2 ==1:
            s = s + int(isbn[i]) * 1
        else:
            s = s + int(isbn[i]) * 3
    print('ISBN 1~12자리의 가중치 반영 합계 %d'%s)

    t = s % 10
    chk = (10 - t) % 10
    print('ISBN 1~12자리의 체크 기호 값 : %d'%chk)

    if chk == int(isbn[12]) :
        rst = 1
    else:
        rst = 0
    return rst

isbn = input('ISBN 13자리(-제외) : ')

if len(isbn) == 13:
    rst = isbn_check(isbn)
    if rst == 1:
        print('ISBN 코트 : %s는 검증되었습니다.'%isbn)
    else:
        print('ISBN 코트 : %s는 검증되지 않았습니다.' %isbn)
else:
    print('ISBN 코드 입력은 -를 제외하고 13자리를 입력해주세요.')
'''

#307페이지 Thinking 2번 p313
'''
a = 1234
a0 = a // 1000
a1 = a % 1000 // 100
a2 = a % 100 // 10
a3 = a % 10
print(a0, a1, a2, a3)

b = '1234'
print(b[0], b[1], b[2], b[3])
'''

#307페이지 Thinking 3번 p314
'''
def isbn_check(isbn):
    s = 0

    for i in range(len(isbn) - 1):
        if (i+1) % 2 ==1:
            s = s + int(isbn[i]) * 1
        else:
            s = s + int(isbn[i]) * 3
    print('ISBN 1~12자리의 가중치 반영 합계 %d'%s)

    t = s % 10
    chk = (10 - t) % 10
    print('ISBN 1~12자리의 체크 기호 값 : %d'%chk)

    if chk == int(isbn[12]) :
        rst = 1
    else:
        rst = 0
    return rst

isbn = input('ISBN 13자리(-제외) : ')

if len(isbn) == 13 and not '-' in isbn:
    rst = isbn_check(isbn)
    if rst == 1:
        print('ISBN 코트 : %s는 검증되었습니다.'%isbn)
    else:
        print('ISBN 코트 : %s는 검증되지 않았습니다.' %isbn)
else:
    print('ISBN 코드 입력은 -를 제외하고 13자리를 입력해주세요.')
'''

#322페이지 코딩프로그래밍 10번
'''
data = []
while True:
    str = input('문자열 : ')
    if str == '':
        break
    data.append(str)
for i in range(len(data)):
    print(data[i], end=' ')
print('')
'''

#326페이지 8번
'''
data = ['Python', 'C', 'Java', 'C++', 'Swift', 'R']
print(data)
idx = data.index('Swift')  #Swift의 위치를 찾음
if idx < len(data): #찾은 위치가 data 범위 내에 있다면
    data[idx] = 'Objective-C'
idx = data.index('Java') #Java의 위치를 찾음
if idx < len(data): #찾은 위치가 data 범위 내에 있다면
    data.insert(idx, 'C#') #그 위치에 C#울 추가해줌
data.remove('R')
for i in range(len(data)):
    print(data[i], end=' ')
print('')
'''

#318페이지 1번
'''
i = 20
print('#123456789#')
print('#%d#'%i)
print('#%-d#'%i)
print('#%9d'%i)
print('#%-9d#'%i)
'''






















