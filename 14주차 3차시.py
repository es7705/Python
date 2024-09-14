#318페이지 2번
'''
f = 3.141592
print('#123456789#')
print('#%f#'%f)
print('#%-f#'%f)
print('#%9.3f#'%f)
print('#%9.1f#'%f)
print('#%-9.3f#'%f)
print('#%-9.1f#'%f)
'''

#319페이지 3번
'''
c = 'a'
s = 'str'
print('#123456789#')
print('#%c#'%c)
print('#%s#'%s)
print('#%9s#'%s)
print('#%-9s#'%c)
print('#%9c#'%s[0])
print('#%-9c#'%s[1])
'''

#319페이지 4번
'''
jn = '980610-1234567'
print('%s %s %s'%(jn[0:2], jn[2:4], jn[4:6]))
print('%c'%jn[7])
print('%c %c %c'%(jn[-1], jn[-3], jn[-5]))
'''

#324페이지 5번
'''
import time
now = time.localtime()

jnymd = input('주민등록번호 년월일 : ')
year = now.tm_year
age = year - (int(jnymd[0:2]) + 1900) + 1
print('나이 : ', age)
'''

#322페이지 1번
'''
s = input('문자열 : ')
while True:
    c = input('문자 : ')
    if c == '':
        break
    if c in s:
        print('문자 %c가 문자열 %s에 존재함'%(c, s))
    else:
        print('문자 %c가 문자열 %s에 존재하지 않음' % (c, s))
'''

#323페이지 2번
'''
def str2int(s):
    if s.isdigit():
        tmp = int(s)
    else:
        tmp = None
    return tmp

st = input('문자열 : ')
n = str2int(st)
if n != None:
    print('%d'%n)
else:
    print(n)
'''

#327페이지 10번
'''
def issn_check(isbn):
    s = 0
    weight = 8
    for i in range(len(issn) - 1):
            s = s + int(isbn[i]) * weight
            weight = weight - 1
    print('ISSN 1~7자리의 가중치 반영 합계 %d'%s)

    t = s % 11
    chk = 11 - t
    print('ISBN 1~7자리의 체크 기호 값 : %d'%chk)

    if chk == 10:
        chk = 'x'
    elif chk == 11:
        chk = 0
    if chk == int(isbn[7]) :
        rst = 1
    else:
        rst = 0
    return rst

issn = input('ISSN 8자리(-제외) : ')

if len(issn) == 8:
    rst = issn_check(issn)
    if rst == 1:
        print('ISBN 코트 : %s은(는) 검증되었습니다.'%issn)
    else:
        print('ISBN 코트 : %s은(는) 검증되지 않았습니다.' %issn)
else:
    print('ISSN 코드 입력은 -를 제외하고 8자리를 입력해주세요.')
''