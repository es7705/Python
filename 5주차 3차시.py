# 137페이지 코딩 프로그래밍 6번
'''
ph  = int(input('pH: '))
if ph >= 0 and ph <= 4 :
    print('강산성')
elif ph >= 5 and ph <= 6: # ph <= 6도 가능
    print('약산성')
elif ph == 7:
    print('중성')
elif ph >= 8 and ph <= 9: # ph <= 9도 가능
    print('약염기성')
elif ph >= 10 and ph <= 14: # ph <= 14도 가능
    print('강염기성')
else :
    print('범위를 벗어났습니다.')
'''


# 138페이지 코딩 프로그래밍 7번
'''
y =  int(input('년도: '))
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 :
    print('윤년')
else:
    print('평년')
'''

# 138페이지 코딩 프로그래밍 8번
'''
h = int(input('키(cm):'))
w = int(input('몸무게(kg):'))
h = h * 0.01 # cm -> m로 변환
bmi = w / (h * h)
if bmi >= 35 :
    grade = '고도비만'
elif bmi >= 30 and bmi < 35: # bmi >= 30도 가능
    grade = '중등도비만'
elif bmi >= 25 and bmi < 30: # bmi >= 25도 가능
    grade = '경도비만'
elif bmi >= 23 bmi < 25: # bmi >= 23도 가능
    grade = '과체중'
elif bmi >= 18.5 and bmi = 23: # bmi >= 18.5도 가능
    grade = '정상'
else :
    grade = '저체중'
print('bmi =', bmi)
print(grade)
'''














