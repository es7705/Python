#261페이지 프로그램 09-02
'''
import turtle as t

s7seg_img = ['7s0.gif', '7s1.gif', '7s2.gif', '7s3.gif', '7s4.gif', '7s5.gif', '7s6.gif', '7s7.gif', '7s8.gif', '7s9.gif', '7s10.gif']

def disp_num(k):
    t.shape(s7seg_img[k])
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
    disp_num(10)

t.setup(400, 400)
s = t.Screen()
t.hideturtle()
t.speed(0)

for i in range(11):
    s.addshape(s7seg_img[i])

disp_num(10)

s.onkey(key_0, '0')
s.onkey(key_1, '1')
s.onkey(key_2, '2')
s.onkey(key_3, '3')
s.onkey(key_4, '4')
s.onkey(key_5, '5')
s.onkey(key_6, '6')
s.onkey(key_7, '7')
s.onkey(key_8, '8')
s.onkey(key_9, '9')
s.onkey(key_10, 'r')
s.listen()

t.mainloop()
'''

#265페이지 thinking 2번 p275
'''
import turtle as t

#s7seg_img = ['7s0.gif', '7s1.gif', '7s2.gif', '7s3.gif', '7s4.gif', '7s5.gif', '7s6.gif', '7s7.gif', '7s8.gif', '7s9.gif', '7s10.gif']

def disp_num(k):
    #t.shape(s7seg_img[k])
    t.shape('7s%d.gif'%k)
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
    disp_num(10)

t.setup(400, 400)
s = t.Screen()
t.hideturtle()
t.speed(0)

for i in range(11):
    #s.addshape(s7seg_img[k])
    s.addshape('7s%d.gif'%i)

disp_num(10)

s.onkey(key_0, '0')
s.onkey(key_1, '1')
s.onkey(key_2, '2')
s.onkey(key_3, '3')
s.onkey(key_4, '4')
s.onkey(key_5, '5')
s.onkey(key_6, '6')
s.onkey(key_7, '7')
s.onkey(key_8, '8')
s.onkey(key_9, '9')
s.onkey(key_10, 'r')
s.listen()

t.mainloop()
'''

#265페이지 thinking 3번 p276
'''
import turtle as t

s7seg_img = ['7s0.gif', '7s1.gif', '7s2.gif', '7s3.gif', '7s4.gif', '7s5.gif', '7s6.gif', '7s7.gif', '7s8.gif', '7s9.gif', '7s10.gif']

def disp_num(k):
    t.shape(s7seg_img[k])
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
    disp_num(10)

t.setup(400, 400)
s = t.Screen()
t.hideturtle()
t.speed(0)

for i in range(11):
    s.addshape(s7seg_img[i])

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
#s.onkey(key_10, 'r')

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

#274페이지
'''
a = [1, 2]
b = range(3)
c = [a, b, [4], [5, 6]]
print(a, a[0], a[1])
print(b, b[0], b[1], b[2])
print(c)
print(c[0], c[1], c[2], c[3])
print(c[0][0], c[1][2], c[2][0], c[3][0])
'''

#274페이지 잠깐코딩 4번 p281
'''
a = [0, 1, 2, 3, 4, 5]
for i in range(6):         #0 ~ 5
    print(a[i], end = ' ')
print('')
'''

#274페이지 잠깐코딩 5번 p281
'''
b = [[0, 1], [2, 3], [4, 5], [6, 7]]
for i in range(4):
    for j in range(2):
        print(b[i][j], end=' ')
    print('')
'''












