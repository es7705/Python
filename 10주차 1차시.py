#208페이지 프로그램 08-01
'''
def comp(src):
    comp_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    seq_comp = ''
    for char in src:
        seq_comp = seq_comp + comp_dict[char]
    return seq_comp

def rev(src):
    seq_rev = ''.join(reversed(src))
    return seq_rev

def rev_comp(src):
    tmp = comp(src)
    return rev(tmp)

src = input('DNA sequence : ')
cnvt = int(input('1(comp), 2(Rev), 3(Rev_Comp) : '))
if (cnvt >= 1 and cnvt <= 3):
    if cnvt == 1:
        rst = comp(src)
    elif cnvt == 2:
        rst =rev(src)
    elif cnvt ==3 :
        rst = rev_comp(src)
    print(src, '->', rst)
else :
    print('1(comp), 2(Rev), 3(Rev_Comp)!!')
'''
import turtle

# 211페이지 Thinking 1번 p229
'''
def comp(src):
    comp_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    seq_comp = ''
    for char in src:
        if char in comp_dict:
            seq_comp = seq_comp + comp_dict[char]
        else:
            seq_comp = seq_comp + '?'
    return seq_comp

def rev(src):
    seq_rev = ''.join(reversed(src))
    return seq_rev

def rev_comp(src):
    tmp = comp(src)
    return rev(tmp)

src = input('DNA sequence : ')
cnvt = int(input('1(comp), 2(Rev), 3(Rev_Comp) : '))
if (cnvt >= 1 and cnvt <= 3):
    if cnvt == 1:
        rst = comp(src)
    elif cnvt == 2:
        rst =rev(src)
    elif cnvt ==3 :
        rst = rev_comp(src)
    print(src, '->', rst)
else :
    print('1(comp), 2(Rev), 3(Rev_Comp)!!')
'''

# 211페이지 Thinking 2번 p229
'''
def comp(src):
    comp_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    seq_comp = ''
    for char in src:
        if char in comp_dict:
            seq_comp = seq_comp + comp_dict[char]
        else:
            seq_comp = seq_comp + '?'
    return seq_comp

def rev(src):
    seq_rev = ''
    n = int(len(src)) - 1

    while n > -1 :
        seq_rev = seq_rev + src[n]
        n =  n - 1
    return seq_rev

def rev_comp(src):
    tmp = comp(src)
    return rev(tmp)

src = input('DNA sequence : ')
cnvt = int(input('1(comp), 2(Rev), 3(Rev_Comp) : '))
if (cnvt >= 1 and cnvt <= 3):
    if cnvt == 1:
        rst = comp(src)
    elif cnvt == 2:
        rst =rev(src)
    elif cnvt ==3 :
        rst = rev_comp(src)
    print(src, '->', rst)
else :
    print('1(comp), 2(Rev), 3(Rev_Comp)!!')
'''

# 220페이지 잠깐코딩 3번 p234
'''
import turtle as t

def write_xy(x,y) :
    t.goto(x,y)
    t.stamp()
    t.write('x:%d, y:%d'%(x,y))

def screen_clear(x, y):
    t.goto(x,y)
    t.clear()

t.setup(600, 600) # 화면크기 설정
s = t.Screen()
t.penup() # 펜 들기

s.onscreenclick(write_xy , 1) # 콜백 함수 마우스 오른쪽 키
s.onscreenclick(screen_clear, 3) # 콜백 함수 마우스 왼쪽 키
s.listen()

t.mainloop()
'''






















































