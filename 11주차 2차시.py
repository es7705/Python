# 243페이지 4번
'''
engkor_dict = dict()
while True:
    eng = input('영어 단어 : ')
    if eng == '':
        break
    if len(engkor_dict) > 0:
        if eng in engkor_dict:
            print(eng, ':', engkor_dict[eng])
            continue
        else:
            print(eng, '단어가 등록되어 있지 않습니다.')
    else:
        print('사전이 비어 있습니다.')
    print('단어를 추가합니다.')
    kor = input('한글 단어 : ')
    engkor_dict[eng] = kor
print(engkor_dict)
'''

#238페이지 6번
'''
import time
for i in range(1, 6, 1):
    print(i, end = ' ')
    time.sleep(1)
'''

#239페이지 7번
'''
import math
num = float(input('실수 : '))
print(num, ':', math.ceil(num)) # 올림 연산
print(num, ':', math.floor(num)) # 내림 연산
print(num, ':', math.trunc(num)) # 버림 연산
'''










