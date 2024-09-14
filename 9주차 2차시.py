#200페이지 6번
'''
def fc(temper, action):
    if action == 0 :
        tmp = temper * 1.8 + 32 #C2F
        tmpact = 'C2F'
    else:
        tmp = (temper - 32) / 1.8 #F2C
        tmpact = 'F2C'
    return (tmp, tmpact)

t = int(input('온도 : '))
a = int(input('변환(0:C2F, 1:F2C) : '))
(rt , ra) = fc(t, a) # 두 개 동시에 튜플로 반환하는 법
print(ra, ':', t, '=>', rt)
'''

#200페이지 5번
'''
def pzn(num):
    if num > 0:
        tmp = 1
    elif num == 0:
        tmp = 0
    else :
        tmp = -1
    return tmp
while True:
    n = int(input('정수 : '))
    r = pzn(n)
    if r  == 1:
        print('양수')
    elif r == 0:
        print('0')
        break
    else :
        print('음수')
'''


#202페이지 10번 중요
'''
def vsum(*num): # 여기 잘 알아두기 *num은 가변 매개변수
    s = 0
    for i in num : # num으로 쓰는거 잘 알아두기
        s = s + i
    return s
print('2 + 3 =', vsum(2, 3))
print('2 + 3 + 4 =', vsum(2, 3, 4))
print('2 + 3 + 4 + 5 =`', vsum(2, 3, 4, 5))
'''








