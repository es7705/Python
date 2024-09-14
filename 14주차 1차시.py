#293페이지 프로그램 10-01
'''
import turtle as t

robot_fn = "robotic_vacuum.gif"
rx = []
ry = []
move_cnt = 0


def move_robot(action):
    t.clear()
    if action == 0:
        for i in range(move_cnt):
            t.goto(rx[i], ry[i])
    elif action == 1:
        for i in range(move_cnt - 1, -1, -1):
            t.goto(rx[i], ry[i])
    elif action == 2:
        t.goto(rx[move_cnt - 1], ry[move_cnt - 1])
    elif action == 3:
        t.goto(rx[0], ry[0])
    t.penup()


def clicked(x, y):
    global move_cnt
    move_cnt += 1
    rx.append(x)
    ry.append(y)


def list_clear():
    global move_cnt
    del rx[1:move_cnt]
    del ry[1:move_cnt]
    move_cnt = 1


def key_SP():
    move_robot(0)


def key_BS():
    move_robot(1)


def key_s():
    move_robot(2)


def key_r():
    move_robot(3)


def key_e():
    list_clear()


t.setup(600, 600)
s = t.Screen()
t.hideturtle()

s.addshape(robot_fn)
t.shape(robot_fn)
t.speed(6)
t.penup()
clicked(-265, 265)
t.goto(-265, 265)
t.showturtle()

s.onkey(key_SP, "space")
s.onkey(key_BS, "BackSpace")
s.onkey(key_s, "s")
s.onkey(key_r, "r")
s.onkey(key_e, "e")
s.onscreenclick(clicked)
s.listen()
t.mainloop()
'''

#300페이지 Thinking 1번 p313
'''
import turtle as t

robot_fn = "robotic_vacuum.gif"
rx = []
ry = []
move_cnt = 0


def move_robot(action):
    t.clear()
    t.pendown()
    if action == 0:
        for i in range(move_cnt):
            t.goto(rx[i], ry[i])
    elif action == 1:
        for i in range(move_cnt - 1, -1, -1):
            t.goto(rx[i], ry[i])
    elif action == 2:
        t.goto(rx[move_cnt - 1], ry[move_cnt - 1])
    elif action == 3:
        t.goto(rx[0], ry[0])
    t.penup()


def clicked(x, y):
    global move_cnt
    move_cnt += 1
    rx.append(x)
    ry.append(y)


def list_clear():
    global move_cnt
    del rx[1:move_cnt]
    del ry[1:move_cnt]
    move_cnt = 1


def key_SP():
    move_robot(0)


def key_BS():
    move_robot(1)


def key_s():
    move_robot(2)


def key_r():
    move_robot(3)


def key_e():
    list_clear()


t.setup(600, 600)
s = t.Screen()
t.hideturtle()

s.addshape(robot_fn)
t.shape(robot_fn)
t.speed(6)
t.penup()
clicked(-265, 265)
t.goto(-265, 265)
t.showturtle()

s.onkey(key_SP, "space")
s.onkey(key_BS, "BackSpace")
s.onkey(key_s, "s")
s.onkey(key_r, "r")
s.onkey(key_e, "e")
s.onscreenclick(clicked)
s.listen()
t.mainloop()
'''

#308페이지
'''
str1 = 'Text'
str2  ="String"
ste3 = """Text
String
"""

str4 = "That's string"
str5 = 'Text "in" string'

print(str1)
print(str2)
print(ste3)
print(str4)
print(str5)
'''

#309페이지
'''
a = 10
b = 3.546
ch = 'a'
st = 'abc'
print('Value = %d'%a)
print('Value = %-4d,%4d'%(a,a)) #왼쪽 맞춤 자릿수 4
print('Value = %f'%b)
print('Value = %4.1f,%4.2f'%(b,b)) #왼쪽 맞춤 자릿수 4 소수점 이하 한 자리
print('Value = %c'%ch)
print('Value = %s'%st)
'''

#310페이지
'''
st = 'Text Stirng'
print(st[0], st[1], st[len(st)-1])
for i in range(len(st)):
    print(st[i], end=' ')
print('') #줄바꿈
print(st[len(st)]) #11의 위치에는 아무것도 없으므로 에러남
'''

#311 페이지
'''
st = 'Text String'
if 'x' in st:         #st에 x가 포함되어 있는지
    print("Included")
else:
    print('Not Included')
print('lenth: ', len(st)) #길이
st1 = '123'
st2 = '3.546'
print(st1, st2)
st3 = st.replace('S', 's') #S를 s로 변환
print(st3)
st4 = 'TextString'
print(st.upper()) #대문자로 변환
print(st.lower()) #소문자로 변환
print(st.isdigit(), st4.isdigit(), st1.isdigit()) #숫자만 구성되어 있는지
print(st.isalpha(), st4.isalpha(), st1.isalpha()) #문자로만 구성되어 있는지
print(st.isalnum(), st4.isalnum(), st1.isalnum()) #숫자/문자로만 구성되어 있는지 
''
















