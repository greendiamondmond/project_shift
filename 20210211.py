print('1' +'='*50)
# 1. 1명의 직원의 한달 스케줄에 D 채우기

def sch(n):
    list_a = []
    for i in range(1, n+1):
        j = 'D'
        list_a.append(j)
    
    return(list_a)

a = sch(31)
print(a)


print('2' + '='*50)
# 2. 1명 직원의 한달 스케줄 보기 좋게 정리 ( D D D D D D D ...)

def print_sch(list_b):
    for i in range(len(list_b)):
        print(list_b[i] + ' ', end='')
    print()

print_sch(a)
print_sch(a)

print('3' + '='*50)
# 3. 1명 직원의 하루 스케줄에 근무형태 랜덤으로 넣기 (D, E, N, O)

import random
s = random.choice(['D', 'E', 'N', 'O'])
print(s)

print('4' +'='*50)
# 4. 3번을 함수로 만들기
def s():
    ss = random.choice(['D', 'E', 'N', 'O'])
    return ss

k = s()
print(k)

print('5' +'='*50)
# 5. 1명 직원의 한달 스케줄에 근무형태 랜덤으로 넣기 (D, E, N, O)

list_c = []
for i in range(31):
    kk = s()
    list_c.append(kk)

print(list_c)

print_sch(list_c) #2번 적용

print('6' +'='*50)
#6. 5번의 내용을 함수로 만들기

def p_list():
    list_c = []
    for i in range(31):
        kk = s()
        list_c.append(kk)
    return list_c

print_sch(p_list())

print('7' +'='*50)
#7. 20명의 직원의 한달 스케줄 랜덤으로 배정하기

n = 20
for i in range(n):
    print(str(i) + ': ', end='')
    print_sch(p_list())
    


