# 213페이지 프고르램 08-02-1
'''
import turtle as t

def draw_pos(x, y):
    t.clear()
    t.setpos(x, y)
    t.stamp()

    hl = - (t.window_height() / 2) # 바닥

    tm = 0
    while True:
        d = (9.8 * tm**2) / 2
        ny = y - int(d) # 새로운 위치 = 이전위치 - 이동거리
        if ny > hl : #y의 위치가 바닥보다 높으면
            t.goto(x, ny)
            t.stamp()
            tm = tm + 0.3
        else :
            break

t.setup(500, 600)
t.shape('circle')
t.shapesize(0.3, 0.3, 0) # 0: 테두리 없음
t.penup()
s = t.Screen()
s.onscreenclick(draw_pos)
s.listen()

t.mainloop()
'''

#217페이지 Thinking 3번 p230
'''
import turtle as t

def draw_pos(x, y):
    t.hideturtle()
    t.clear()
    t.setpos(x, y)
    t.showturtle()
    t.stamp()

    hl = - (t.window_height() / 2)

    tm = 0
    while True:
        d = (9.8 * tm**2) / 2
        ny = y - int(d)
        if ny > hl :
            t.goto(x, ny)
            t.stamp()
            tm = tm + 0.3
        else :
            break

t.setup(500, 600)
t.shape('circle')
t.shapesize(0.3, 0.3, 0)
t.penup()
t.hideturtle()
s = t.Screen()
s.onscreenclick(draw_pos)
s.listen()

t.mainloop()
'''

#217페이지 Thinking 4번 p230
'''
import turtle as t

def draw_pos(x, y):
    t.hideturtle()
    t.clear()
    t.setpos(x, y)
    t.showturtle()
    t.stamp()
    t.write('y:%5d'%y)
    hl = - (t.window_height() / 2)

    tm = 0
    while True:
        d = (9.8 * tm**2) / 2
        ny = y - int(d)
        if ny > hl :
            t.goto(x, ny)
            t.stamp()
            t.write('y:%5d, d%4d'%(ny,d))
            tm = tm + 0.3
        else :
            break

t.setup(500, 600)
t.shape('circle')
t.shapesize(0.3, 0.3, 0)
t.penup()
t.hideturtle()
s = t.Screen()
s.onscreenclick(draw_pos)
s.listen()

t.mainloop()
'''

#217페이지 Thinking 5번 p231
'''
import turtle as t

def draw_land():
    sx = -(t.window_width() / 2 - 10)
    sy = -(t.window_height() / 2 - 20)
    dist = t.window_width() - 20 # 선분의 길이
    t.hideturtle()
    t.penup()
    t.setpos(sx, sy)
    t.pendown()
    t.forward(dist)
    t.penup()

def draw_pos(x, y):
    t.hideturtle()
    t.clearstamps() # s붙여야함, 선까지 지우면 안 되니까 스템프만 지움
    t.setpos(x, y)
    t.showturtle()
    t.stamp()

    hl = - (t.window_height() / 2)

    tm = 0
    while True:
        d = (9.8 * tm**2) / 2
        ny = y - int(d)
        if ny > hl :
            t.goto(x, ny)
            t.stamp()
            tm = tm + 0.3
        else :
            t.goto(x, ny)
            t.stamp()
            break

t.setup(500, 600)
t.shape('circle')
t.shapesize(0.3, 0.3, 0)
t.penup()
t.hideturtle()
s = t.Screen()
draw_land()
s.onscreenclick(draw_pos)
s.listen()

t.mainloop()
'''
