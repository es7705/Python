# 228페이지 도 > 라디안 변환
'''
import math
a = 45
r = a * 3.14 / 180.0
print(r)

r = a * math.pi / 180.0
print(r)

r = math.radians(a)
print(r)

print(math.cos(r), math.sin(r))
'''

# 228페이지 라디안 > 도 변환
'''
import math
r = 1
a = r * 180.0 / 3.14
print(a)

a = r * 180.0 / math.pi
print(a)

a = math.degrees(r)
print(a)
'''

# 228페이지 잠깐코딩 4번 p235
'''
import  math
a = [-3, 7, 9, 4, 2, 3]
print(a[0], abs(a[0]), max(a),
      min(a), sum(a), pow(2, 3))
'''

# 228페이지 잠깐코딩 5번 p235
'''
import math
a = 90
r = 2
print(math.radians(a))
print(math.degrees(r))
'''

#221페이지 프로그램 08-02-2
'''
import turtle as t
import math

tm = 0.3 # 시간
ux = 0  # x축 속도
uy = 0  # y축 속도
dx = 0 # x축 이동거리
dy = 0 # y축 이동거리
g = 9.8 # 중력가속도
velo = 0 # 초기입력속도
ang = 0 # 초기입력각도

def draw_pos(x, y):
    velo = t.numinput('입력', '속도:', 50, 10, 100)
    ang = math.radians(t.numinput('입력', '각도 : ', 45, 0, 360)) #라디안으로 변경

    t.clearstamps() #s 붙이기
    t.hideturtle()
    t.setpos(x, y)
    t.showturtle()
    t.stamp()

    hl = -(t.window_height() / 2) # 바닥
 
    ux = velo * math.cos(ang) # x축 속도
    uy = velo * math.sin(ang) # y축 속도

    while True:
        uy = uy + (-1 * g) * tm #y축 속도는 중력가속도로 인해 계속 바뀜
        dy = t.ycor() + (uy * tm) - (g * tm**2) / 2
        dx = t.xcor() + (ux * tm)

        if dy > hl:
            t.goto(dx, dy)
            t.stamp()
        else:
            break

t.setup(600, 600)
t.shape('circle')
t.turtlesize(0.3, 0.3, 0)
t.penup()
s = t.Screen()
s.onclick(draw_pos)
s.listen()
t.mainloop()
'''

#226페이지 Thinking 6번 p232
'''
import turtle as t
import math

tm = 0.3
ux = 0
uy = 0
dx = 0
dy = 0
g = 9.8
velo = 0
ang = 0

def draw_land():
    sx = -(t.window_width() / 2 - 10)
    sy = -(t.window_height() / 2 - 20)
    dist = t.window_width() - 20
    t.hideturtle()
    t.penup()
    t.setpos(sx, sy)
    t.pendown()
    t.forward(dist)
    t.penup()

def draw_pos(x, y):
    velo = t.numinput('입력', '속도:', 50, 10, 100)
    ang = math.radians(t.numinput('입력', '각도 : ', 45, 0, 360))

    t.clearstamps()
    t.hideturtle()
    t.setpos(x, y)
    t.showturtle()
    t.stamp()

    hl = -(t.window_height() / 2)

    ux = velo * math.cos(ang)
    uy = velo * math.sin(ang)

    while True:
        uy = uy + (-1 * g) * tm
        dy = t.ycor() + (uy * tm) - (g * tm**2) / 2
        dx = t.xcor() + (ux * tm)

        if dy > hl:
            t.goto(dx, dy)
            t.stamp()
        else:
            t.goto(dx, hl)
            t.stamp()
            break

t.setup(600, 600)
t.shape('circle')
t.turtlesize(0.3, 0.3, 0)
t.penup()
s = t.Screen()
draw_land()
s.onclick(draw_pos)
s.listen()
t.mainloop()
'''









