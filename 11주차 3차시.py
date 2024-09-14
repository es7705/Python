#255페이지
'''
import turtle as t

def print_key(char):
    print(char, end='')
def key_a():
    print_key('a')
def key_sp():
    print_key('s_')
def key_sr():
    print_key('s^')

s = t.Screen()
s.onkey(key_a, 'a')
s.onkeypress(key_sp, 's')
s.onkeyrelease(key_sr, 's')
s.onkey(s.bye, '')
s.listen()
t.mainloop()
'''

#256페이지
'''
gv = 3

def func1():
    lv1 = 1
    lv1 = lv1 + gv
    print(lv1)

def func2(pv):
    lv2 = pv
    print(lv2)

func1()
func2(2)
print(gv)
'''

#257페이지
'''
gv = 3

def func1():
    lv1 = 1
    gv = 1
    lv1 = lv1 + gv
    print(lv1)

def func2(pv):
    lv2 = pv
    print(lv2)

func1()
func2(2)
print(gv)
'''

#258페이지
'''
gv = 3

def func1():
    lv1 = 1
    lv1 = lv1 + gv # 지역변수 gv가 밑에 있으므로 오루

    gv = 1 # 지역변수
    print(lv1)

def func2(pv):
    lv2 = pv
    print(lv2)

func1()
func2(2)
print(gv)
'''

#259페이지
'''
gv = 3

def func1():
    global gv
    lv1 = 1
    lv1 = lv1 + gv
    gv = 1
    print(lv1, gv)

def func2(pv):
    lv2 = pv
    print(lv2)

func1()
func2(2)
print(gv)
'''

#260페이지 잠깐코딩 1번 p278
'''
import turtle as t

def print_digit(n):
    print(n, end = '')
def key_1():
    print_digit(1)
def key_2():
    print_digit(2)
def key_3():
    print_digit(3)

s = t.Screen()
s.onkey(key_1, '1')
s.onkey(key_2, '2')
s.onkey(key_3, '3')
s.listen()
t.mainloop()
'''

#260페이지 잠깐코딩 2번 p279
'''
a = 1
def  func(d):
    global a
    b = a + 2
    c = b + d
    print('func : ', a, b, c, d)
    a = c
    print('func : ', a, b, c, d)
    return c

print('main : ', a)
e = func(3)
print('main : ', a, e)
'''




