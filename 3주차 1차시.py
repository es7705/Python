
# 76페이지 코딩 프로그래밍
# 4번
'''subject = input('과목 : ')
score = int(input('점수 : '))
print('선호과목 : ', subject, ', 희망점수 : ', score)
a = int(input('정수 1 : '))
b = int(input('정수 2: '))
c = int(input('정수 3 : '))
sum = a + b + c
avg = sum/3
print(sum, avg)'''

# 79 페이지 11번
'''a =  int(input('정수:'))
b = str(a)
print(a, type(a), b, type(b))   '''

# 80페이지 14 번
'''radius = int(input('반지름: '))
import turtle
turtle.shape('turtle')
turtle.circle(radius)
turtle.circle(radius, steps=4)
turtle.mainloop()'''

# 84 페이지 9번
'''import turtle
radius = int(input('반지름 : '))
length = int(input('진행 : '))
turtle.shape('turtle')
for i in range(3):
    turtle.circle(radius)
    turtle.forward(length)

turtle.mainloop()'''