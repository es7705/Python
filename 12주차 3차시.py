#267페이지 프로그램 09-03
'''
import turtle as t
s7seg_base = '7s10.gif'
s7seg_led = ['7s-a.gif', '7s-b.gif', '7s-c.gif', '7s-d.gif', '7s-e.gif', '7s-f.gif', '7s-g.gif']

             #a b c d e f g
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

def disp_num(k):
    t.shape(s7seg_base)
    t.stamp()
    if k < 10:
        for i in range(7):
            if s7seg_num[k][i] == 1:
                t.shape(s7seg_led[i])
                t.stamp()

def key_0():
    disp_num(0)
def key_1():
    disp_num(1)
def key_2():
    disp_num(2)
def key_3():
    disp_num(3)
def key_4():
    disp_num(4)
def key_5():
    disp_num(5)
def key_6():
    disp_num(6)
def key_7():
    disp_num(7)
def key_8():
    disp_num(8)
def key_9():
    disp_num(9)
def key_10():
    t.clearstamps()
    disp_num(10)

t.setup(400, 400)
s = t.Screen()
t.hideturtle()
t.speed(0)

s.addshape(s7seg_base)
for i in range(7):
    s.addshape(s7seg_led[i])

disp_num(10)

s.onkeypress( key_0, '0')
s.onkeypress(key_1, '1')
s.onkeypress(key_2, '2')
s.onkeypress(key_3, '3')
s.onkeypress(key_4, '4')
s.onkeypress(key_5, '5')
s.onkeypress(key_6, '6')
s.onkeypress(key_7, '7')
s.onkeypress(key_8, '8')
s.onkeypress(key_9, '9')

s.onkeyrelease(key_10, '0')
s.onkeyrelease(key_10, '1')
s.onkeyrelease(key_10, '2')
s.onkeyrelease(key_10, '3')
s.onkeyrelease(key_10, '4')
s.onkeyrelease(key_10, '5')
s.onkeyrelease(key_10, '6')
s.onkeyrelease(key_10, '7')
s.onkeyrelease(key_10, '8')
s.onkeyrelease(key_10, '9')
s.listen()

t.mainloop()
'''

#273 페이지 Thinking 4번 p277
'''
import turtle as t

old_key = 0
s7seg_base = '7s10.gif'
s7seg_led = ['7s-a.gif', '7s-b.gif', '7s-c.gif', '7s-d.gif', '7s-e.gif', '7s-f.gif', '7s-g.gif']

             #a b c d e f g
s7seg_num = [[1,1,1,1,1,1,0], # 0
             [0,1,1,0,0,0,0], # 1
             [1,1,0,1,1,0,1], # 2
             [1,1,1,1,0,0,1], # 3
             [0,1,1,0,0,1,1], # 4
             [1,0,1,1,0,1,1], # 5
             [1,0,1,1,1,1,1], # 6
             [1,1,1,0,0,0,0], # 7
             [1,1,1,1,1,1,1], # 8
             [1,1,1,1,0,1,1], ]# 9

def disp_num(k):
    global old_key
    t.shape(s7seg_base)
    t.stamp()
    if k != old_key:
     if k < 10:
         for i in range(7):
             if s7seg_num[k][i] == 1:
                   t.shape(s7seg_led[i])
                   t.stamp()
    old_key = k
def key_0():
    disp_num(0)
def key_1():
    disp_num(1)
def key_2():
    disp_num(2)
def key_3():
    disp_num(3)
def key_4():
    disp_num(4)
def key_5():
    disp_num(5)
def key_6():
    disp_num(6)
def key_7():
    disp_num(7)
def key_8():
    disp_num(8)
def key_9():
    disp_num(9)
def key_10():
    t.clearstamps()
    disp_num(10)

t.setup(400, 400)
s = t.Screen()
t.hideturtle()
t.speed(0)

s.addshape(s7seg_base)
for i in range(7):
    s.addshape(s7seg_led[i])

disp_num(10)

s.onkeypress( key_0, '0')
s.onkeypress(key_1, '1')
s.onkeypress(key_2, '2')
s.onkeypress(key_3, '3')
s.onkeypress(key_4, '4')
s.onkeypress(key_5, '5')
s.onkeypress(key_6, '6')
s.onkeypress(key_7, '7')
s.onkeypress(key_8, '8')
s.onkeypress(key_9, '9')

s.onkeyrelease(key_10, '0')
s.onkeyrelease(key_10, '1')
s.onkeyrelease(key_10, '2')
s.onkeyrelease(key_10, '3')
s.onkeyrelease(key_10, '4')
s.onkeyrelease(key_10, '5')
s.onkeyrelease(key_10, '6')
s.onkeyrelease(key_10, '7')
s.onkeyrelease(key_10, '8')
s.onkeyrelease(key_10, '9')
s.listen()

t.mainloop()
'''

#282페이지 코딩프로그래밍 1번
'''
a = b = c = 1

def func():
    a = b = c = 2
    print('func:', a, b, c)

print('main:', a, b, c)
func()
print('main:', a, b, c)
'''

#282페이지 코딩프로그래밍 2번
'''
a = b = c = 1

def func():
    global a, b, c
    a = b = c = 2 # 전역변수가 2로 바뀜
    print('func:', a, b, c)

print('main:', a, b, c)
func()
print('main:', a, b, c)
'''

#283페이지 코딩프로그래밍 3번
'''
a = b = c = 1

def func1():
    a = b = c = 2
def func2():
    global a, b
    a = b = 3
    c = 3

print(a, b, c)
func1()
print(a, b, c)
func2()
print(a, b, c)
'''








