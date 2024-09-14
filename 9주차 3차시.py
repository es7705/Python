#212페이지
'''
comp_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
print(comp_dict)
print(len(comp_dict))
print(comp_dict.keys())
print(comp_dict.values())
print(comp_dict['T'])
'''

#212페이지 잠깐코딩 1번 p233
'''
digit = {1:'일', 2:'이', 3:'삼'}
print(digit)
print(len(digit))
print(digit.keys())
print(digit.values())
print(digit[1])
print(digit[3])
'''

#212페이지 잠깐코딩 2번 p233
'''
fruit = {'사과':100, '바나나':50, '수박':1000}
print(fruit)
print(len(fruit))
print(fruit.keys())
print(fruit.values())
print(fruit['사과'])
print(fruit['수박'])
'''

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

















