#301페이지
'''
fruit = []
fruit.append('사과')
fruit.append('배')
fruit.append('감')
print(fruit)
for i in range(len(fruit)):
    print(i, fruit[i])

fruit.insert(2, '딸기')
print(fruit)
for i in  range(len(fruit)):
    print(i, fruit[i])
'''

#302페이지
'''
fruit = ['사과', '배', '딸기', '감']
print(fruit, len(fruit))
del fruit[2]
print(fruit, len(fruit))
del fruit[0:2] # 0~1
print(fruit, len(fruit))
fruit.remove('감')
print(fruit, len(fruit))
'''

#302페이지 잠깐코딩 1번 p315
'''
city = []
city.append('부산')
city.append('대구')
city.append('대전')
for i in range(len(city)):
    print(i, city[i])
city.insert(0, '서울')
city.insert(3, '인천')
print(city)
'''

#302페이지 잠깐코딩 2번 p316
'''
city = []
city.append('부산')
city.append('대구')
city.append('대전')
for i in range(len(city)):
    print(i, city[i])
city.insert(0, '서울')
city.insert(3, '인천')
print(city)

city[3] = '울산'
del city[1:3] #1~2
print(city)
'''















