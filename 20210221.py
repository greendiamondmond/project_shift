
##########################################################################

# 제약조건
#1. 근무형태 : D / E / N / O
#2. 직원 1명당 한달의 의무 O의 개수는 8이상이어야 한다.
#3. 직원은 6명이고 하루에 D는 2명, E는 1명, N은 1명, O는 2명 
#4. N은 2개 연속되어야 한다.
#5. N이 끝나는 날 다음날은 무조건 O여야 한다.
#6. 직원들의 D, E, N, O의 개수는 균등하면 좋다.
#7. 근무를 최대 4번 선 이후에는 O여야 한다. (간격 4개 이하 가능?)

##########################################################################

import random

# 직원 수
n = 6
# 한달 근무일
m = 31 


print("1===================================================")
#1. 직원 한명의 한달 스케줄의 출력하는 함수 

def print_sch(sch_1):
    for i in range(len(sch_1)):
        if sch_1[i] == '':
            print("-", end="")
        else:
            print(sch_1[i], end="")
    print()


print("2===================================================")
#2. 모든 직원의 한달 스케줄 출력하는 함수

def print_sch_a(sch_a):
    # D, E, N 개수 세기 위한 것 포함
    D_stat = [0] * m
    E_stat = [0] * m
    N_stat = [0] * m

    for i in range(len(sch_a)):
        print(("{:02d}".format(i)) + ":", end="")
        print_sch(sch_a[i])

        for j in range(m):
            if sch_a[i][j] == 'D':
                D_stat[j] += 1
            elif sch_a[i][j] == 'E':
                E_stat[j] += 1
            elif sch_a[i][j] == 'N':
                N_stat[j] += 1

    print("D:", D_stat)
    print("E:", E_stat)
    print("N:", N_stat)


print("3===================================================")
#3. 모든 직원의 한달 스케줄 배정 전

sch_a = []
for i in range(n):
    s = []
    for j in range(m):
        s.append('')
    sch_a.append(s)

print_sch_a(sch_a)


print("4===================================================")
#4. N근무 지정

j = 0
for i in range(n):
    sch_a[i][j] = 'N'
    j += 1
    if j >= m: j = 0
    sch_a[i][j] = 'N'
    j += 1
    if j >= m: j = 0
    sch_a[i][j] = 'O'


j = 12
for i in range(n):
    sch_a[i][j] = 'N'
    j += 1
    if j >= m: j = 0
    sch_a[i][j] = 'N'
    j += 1
    if j >= m: j = 0
    sch_a[i][j] = 'O'


j = 24
for i in range(n):
    sch_a[i][j] = 'N'
    j += 1
    if j >= m: break
    sch_a[i][j] = 'N'
    j += 1
    if j >= m: break
    sch_a[i][j] = 'O'


print_sch_a(sch_a)


print("5===================================================")
#5. O근무 지정 - 기준일(첫번째 N연속근무 후 다음날의 O)로부터 4일 간격으로 O근무

#하루동안의 O의 개수를 세는 함수
def count_off(sch, j):
    cnt = 0
    for i in range(len(sch)):
        if sch[i][j] == 'O': cnt += 1
    return cnt

# 기준일로부터 뒤로 이동
for i in range(n):
    j = sch_a[i].index('O') #기준일 (첫번째 N연속근무다음날O)
    j += 4  #기준일로부터 4번째날로 이동
    while j < m:
        if count_off(sch_a, j) >= 2:    #만약 다음 O근무 예정일날에 이미 O인 사람이 2명 이상인경우 (할당량 채운 경우) 
            j -= 1  #그 전날로 이동
        if sch_a[i][j] == '':   #O근무 예정일이 빈칸인 경우에만 O로 지정
            sch_a[i][j] = 'O'
        j += 4

# 기준일로부터 앞으로 이동
for i in range(n):
    j = sch_a[i].index('O') #기준일 (첫번째 N연속근무다음날O)
    j -= 4  #기준일로부터 거꾸로 4번째날로 이동 (4번째 전날)
    while j >= 0:
        if count_off(sch_a, j) >= 2:    #만약 다음 O근무 예정일날에 이미 O인 사람이 2명 이상인경우 (할당량 채운 경우) 
            j += 1  #그 다음날로 이동
        if sch_a[i][j] == '':
            sch_a[i][j] = 'O'
        j -= 4
    
print_sch_a(sch_a)


print("6===================================================")
#6. D. E근무 지정 - 하루에 D 2명, E 1명으로 랜덤 배정 (하루에 D 2명, E 1명, N 1명, O 2명 될 수 있도록)

#하루동안의 빈칸의 개수를 세는 함수
def count_empty(sch, j):
    cnt = 0
    for i in range(len(sch)):
        if sch[i][j] == '': cnt += 1
    return cnt

for i in range(m):
    A = ['D', 'D', 'E']
    if count_empty(sch_a, i) > 3:   #빈칸이 3칸을 초과하면 X 추가 (여기서 X는 O와 같은 내용인데 정해진 OFF와 구별하기 위해서 X로 했음)
        A.append('X')
    random.shuffle(A)   # 랜덤으로 섞기
    j = 0
    while j < n:
        #print(j, A)
        if sch_a[j][i] == '':
            sch_a[j][i] = A.pop()
        j += 1

print_sch_a(sch_a)


print("7===================================================")
#7. 보기 편하게 정리

def print_p(sch):
    for i in range(len(sch)):
        s = sch[i]
        print("{:02d}".format(i) + "직원: ", end="")
        for j in range(len(s)):
            print(s[j], " ", end="")
        print()

print_p(sch_a)