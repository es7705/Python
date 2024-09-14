#248페이지 프로그램 09-01 화재경보기 작동하기
'''
import turtle as t

color_status = ['white', 'blue', 'red']
alter_status = ['정상', '주의', '화재']
tempc = 50

def check_fire():
    if tempc < 80 :
        status = 0
    elif tempc < 120 :
        status = 1
    else :
        status = 2

    t.clear()
    t.home()
    t.pendown()
    t.fillcolor(color_status[status])
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()
    t.goto(-22, 50)
    t.write('%s : %d' %(alter_status[status], tempc))

def keyUp():
    global tempc
    if tempc < 80:
        tempc = tempc + 5
    else:
        tempc = tempc + 10
        check_fire()

def keyDown():
    global tempc
    if tempc <= 80:
         tempc = tempc - 5
    else:
         tempc = tempc - 10
    check_fire()

t.setup(300, 300)
s = t.Screen()
t.hideturtle()
t.speed(0)
check_fire()
s.onkey(keyUp, 'Up')
s.onkey(keyDown, 'Down')
s.onkey(s.bye, 'q')
s.listen()

t.mainloop()
'''

#265페이지
'''
import turtle as t
t.setup(400, 400)
t.delay(1000)
t.shape('turtle')
t.delay(1000)
t.addshape('7s0.gif')
t.shape('7s0.gif')
t.mainloop()
'''

#266페이지 잠깐코딩 3번 p280
'''
import turtle as t
t.setup(400, 400)
t.delay(1000)
t.shape('arrow')
t.delay(1000)
t.shape('turtle')
t.delay(1000)
t.shape('circle')
t.delay(1000)
t.shape('square')
t.delay(1000)
t.shape('triangle')
t.delay(1000)
t.shape('classic')
t.delay(1000)
t.addshape('7s0.gif')
t.shape('7s0.gif')
t.delay(1000)   
t.addshape('7s1.gif')
t.shape('7s1.gif')
'''












