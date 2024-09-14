#283페이지 코딩프로그래밍 4번
'''
quotient = 0
remainder = 0

def div_qr(n1, n2):
    global quotient, remainder
    quotient = n1 // n2
    remainder = n1 % n2

num1 = int(input('정수1 : '))
num2 = int(input('정수2 : '))
div_qr(num1, num2)
print('몫 : ', quotient, '나머지 : ', remainder)
'''

#284페이지 코딩프로그래밍 5번
'''
def div_qr(n1, n2):
    quotient = n1 // n2
    remainder = n1 % n2
    return (quotient, remainder)

num1 = int(input('정수1 : '))
num2 = int(input('정수2 : '))
(q, r) = div_qr(num1, num2)
print('몫 : ', q, '나머지 : ', r)
'''

#284페이지 코딩프로그래밍 6번
'''
data = [21, 7, 43, 65, 2, 8, 72, 52, 9]
for i in range( len(data) ):
    print(data[i], end=' ')
print('')
'''

#286페이지 1번
'''
data = [21, 7, 43, 65, 2, 8, 72, 52, 9]
search = int(input('찾을 값 :' ))
find = len(data) # 전역변수 9
for i in range( len(data) ):
    if search == data[i]:
        find = i
        break
if find < len(data): #find가 0~8이면 찾음
    print('위치:', find)
else: #find가 그대로 9이면 찾지 못함
    print('찾지 못함')
'''

#285페이지 8번
'''
data = [[21, 7, 43, 65],
        [2, 8, 72, 52]]
for i in range(len(data)): #2: 0~1 1열 2열
    for j in range(len(data[0])): # 0~4
        print(data[i][j], end=' ')
    print('')
'''

#287페이지 3번
'''
data = [[21, 7, 43, 65],
        [2, 8, 72, 52]]
search = int(input('찾을 값 : '))
find_r = len(data) # 2
find_c = len(data[0]) # 4
for i in range(len(data)): #2: 0~1 1열 2열
    for j in range(len(data[0])): # 0~4
        if search == data[i][j]:
            find_r = i
            find_c = j
if find_r < len(data) and find_c < len(data[0]):
    print('위치 : %d행 %d열'%( find_r + 1, find_c + 1))
else:
    print('찾지못함')
'''

#290페이지 9번
'''
import copy
s7seg_num = [[1,1,1,1,1,1,0], # 0
             [0,1,1,0,0,0,0], # 1
             [1,1,0,1,1,0,1], # 2
             [1,1,1,1,0,0,1], # 3
             [0,1,1,0,0,1,1], # 4
             [1,0,1,1,0,1,1], # 5
             [1,0,1,1,1,1,1], # 6
             [1,1,1,0,0,0,0], # 7
             [1,1,1,1,1,1,1], # 8
             [1,1,1,1,0,1,1]]# 9
s7seg_num_anode = copy.deepcopy(s7seg_num)

for i in range(len(s7seg_num)):
    for j in range(len(s7seg_num[0])):
        if s7seg_num[i][j] == 0 :
            s7seg_num_anode[i][j] = 1
        else:
            s7seg_num_anode[i][j] = 0

print('s7seg_num         s7seg_num_anode')
for i in range(len(s7seg_num)) :
    for j in  range(len(s7seg_num[0])): #캐소드 타입 출력
        print(s7seg_num[i][j], end=' ')
    print(end='    ')
    for j in range(len(s7seg_num_anode[0])) : #에노드 타입 출력
        print(s7seg_num_anode[i][j], end=' ')
    print('')
'''

#285페이지 9번
'''
import turtle as t

default_shape = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
user_shape = ['7s0.gif', '7s1.gif', '7s2.gif']

t.setup(400, 400)
t.delay(1000)
for i in range(6):
    t.shape(default_shape[i])
    t.delay(1000)
for i in range(3):
    t.addshape(user_shape[i])
    t.shape(user_shape[i])
    t.delay(1000)

t.mainloop()
'''