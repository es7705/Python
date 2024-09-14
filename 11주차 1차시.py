#236 페이지 1번
'''
str = input('문자열 : ')
print('문자열 길이 : ', len(str))
print('첫 번째 문자 : ', str[0])
print('두 번째 문자', str[1])
print('마지막 문자 : ', str[len(str) - 1])
'''

#236 페이지 2번
'''
str = input('문자열 : ')
print('개별 문자 출력 : ', end = '')
for i in range(len(str)) : # 18 - 1 = 17 17~0까지
    print(str[i], end = '')
print('') # 줄 바꿈
print('역순 개별 문자 출력 : ', end = '')
for i in range(len(str) - 1, -1, -1): # 17 , -1, -1 17 ~ 0까지
    print(str[i], end = '')
print('')
'''

#237 페이지 3번
'''score = int(input("점수 : " ))
if score >= 0 and score <= 100  :
    if score >= 90:
        degree = 'A'
    elif score >=80:
        degree = 'B'
    elif score >=70:
        degree = 'C'
    elif score >=60:
        degree = 'D'
    else :
        degree = 'F'
    print(score, ':', degree)
else:
    print('입력 가능한 점수 범위는 0 ~ 100입니다.')
'''

#237 페이지 4번
'''
deg = {10 : 'A', 9 : 'A', 8 : 'B', 7 : 'C', 6 : 'D', 5 : 'F', 4 : 'F', 3 : 'F', 2 : 'F', 1 : 'F', 0 : 'F'}
score  = int(input('점수 : '))
if  score >= 0 and score <= 100:
    sco = score // 10
    degree = deg[sco] # 값을 가져옴 sco가 10이면 A가 저장됨
    print(score, ':', degree)
else:
    print('입력 가능한 점수 범위는 0 ~ 100입니다.')
'''

#238 페이지 5번

'''
items = {'라면' : 650 , '우유' : 1100, '콜라' :1200 , '캔커피' : 500, '과자' : 700}
s = 0

while True :
    it = input('제품명 : ')
    if it == '':
        break
    if it in items:
        s  = s + items[it]
        print('[%s:%d] > %d'%(it, items[it], s))
    else:
        print(it, '는 미동록 제품입니다.')
print('총 금액 : ', s)
'''

#242 페이지 3번
'''
engkor_dict = {}
while True:
    eng = input('영어 단어 : ')
    kor = input('한글 단어 : ')
    if eng == '' and kor == '' :
        break
    engkor_dict[eng] = kor
print(engkor_dict)
'''













