# Magnetic 문제


# 테이블 위에 자성체들이 놓여 있다.

# 자성체들은 성질에 따라 색이 부여되는데, 푸른 자성체의 경우 N극에 이끌리는 성질을 가지고 있고, 붉은 자성체의 경우 S극에 이끌리는 성질이 있다.

# 아래와 같은 테이블에서 일정 간격을 두고 강한 자기장을 걸었을 때, 시간이 흐른 뒤에 자성체들이 서로 충돌하여 테이블 위에 남아있는 교착 상태의 개수를 구하라.

# 아래는 자성체들이 놓여 있는 테이블을 위에서 바라본 모습이다.
 


 
# A로 표시된 붉은 자성체의 경우 S극에 이끌리면서 테이블 아래로 떨어지게 된다.

# B로 표시된 푸른 자성체의 경우 N극에 이끌리면서 테이블 아래로 떨어지게 된다.

# 나머지 자성체들은 서로 충돌하며, 교착 상태에 빠져 움직이지 않게 된다.

# D로 표시된 자성체들에서 알 수 있듯 한 쪽 방향으로 움직이는 자성체의 개수가 많더라도 반대 방향으로 움직이는 자성체가 하나라도 있으면 교착 상태에 빠져 움직이지 않는다.

# D로 표시된 자성체들과 같이 셋 이상의 자성체들이 서로 충돌하여 붙어 있을 경우에도 하나의 교착 상태로 본다.

# C와 D는 좌우로 인접하여 있으나 각각 다른 교착 상태로 판단하여 2개의 교착 상태로 본다.

# E의 경우와 같이 한 줄에 두 개 이상의 교착 상태가 발생할 수도 있다.

# F의 경우 각각 다른 교착상태로 판단하여 2개의 교착상태로 본다.

# 위의 예시의 경우 테이블 위에 남아있는 교착상태는 7개이므로 7를 반환한다.


# [제약 사항]

# 자성체는 테이블 앞뒤 쪽에 있는 N극 또는 S극에만 반응하며 자성체끼리는 전혀 반응하지 않는다.

# 테이블의 크기는 100x100으로 주어진다. (예시에서는 설명을 위해 7x7로 주어졌음에 유의)

# [입력]

# 10개의 테스트 케이스가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 정사각형 테이블의 한 변의 길이가 주어진다. (이 값은 항상 100이다)

# 그 다음 줄부터 100 x 100크기의 테이블의 초기 모습이 주어진다. 1은 N극 성질을 가지는 자성체를 2는 S극 성질을 가지는 자성체를 의미하며 테이블의 윗부분에 N극이 아래부분에 S극이 위치한다고 가정한다.

# (N극 성질을 가지는 자성체는 S극에 이끌리는 성질이 있다.)

# [출력]

# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 교착 상태의 개수를 출력한다.

# 입력
# 100
# 1 0 0 0 0 0 0 0 2 0 0 0 1 0 1 1 0 2 0 0 1 0 2 0 2 2 1 0 0 0 0 0 1 0 0 2 0 0 0 0 0 1 2 0 0 0 1 1...
# 0 0 0 0 0 0 0 0 0 0 1 0 0 2 0 0 0 0 0 2 0 0 1 0 0 0 0 0 1 2 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0...
# 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 2 2 0 2 0 0 0 0 0 1 0 0...
# 0 0 0 2 0 0 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 1 0 1 0 0 0 0 0 0 2 0 2 0...
# 0 0 0 0 2 0 2 0 0 0 2 0 0 0 0 0 0 2 1 1 0 2 0 0 0 1 2 2 2 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0...
# 0 0 2 0 0 0 1 1 1 0 0 0 0 0 0 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0...
# ...
# 100
# 0 0 0 0 0 0 0 0 0 2 0 0 2 0 0 0 0 0 0 2 0 0 0 1 0 0 0 0 0 0 1 0 2 0 2 0 1 0 1 0 0 0 0 1 0 0 0 0 ...
# 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 ...
# 0 0 0 0 2 0 0 0 1 2 1 0 0 0 0 1 0 0 0 0 0 2 0 0 0 0 0 2 2 1 2 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 ...
# 2 2 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 1 2 0 2 0 0 0 ...
# 0 1 1 0 2 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 2 0 0 0 2 0 0 0 0 ...
# 1 0 0 0 0 1 0 2 0 0 0 0 2 0 2 0 0 0 0 0 0 0 0 0 2 0 0 1 2 0 0 0 0 1 0 0 1 0 0 0 2 0 0 2 2 0 0 0 ...
# ...
                
# 출력
# #1 471
# #2 446
# ...

# 처음 문제를 보고 솔직히 하나씩 움직이는 것을 구현하면서 서로 더 이상 움직일 공간이 없을 때 cnt + 1 증가 방식으로 구현해야하나?
# 라는 엄청 복잡하고 비효율적인 방식을 생각했다.
# 하지만 배열의 크기도 정해져있고, 교착 상태는 색깔만 다른 자성체가 서로 만났을 경우이기 때문에 이는 서로 색깔이 다른 자성체의 경우에만 개수를 세어주는 방식으로 접근하는 것이 효율적이라는 것을 알게되었다. 

for tc in range(1, 11):
    width = int(input())

    matrix = [list(map(int, input().split())) for _ in range(width)]

    # 교착 상태 = 한 열의 1과 2의 개수가 동일
    dead_lock_cnt = 0

    for i in range(width):
        flag = 0
        for j in range(width):
            if matrix[j][i] == 1:
                flag = 1
            elif matrix[j][i] == 2:
                if flag:
                    dead_lock_cnt += 1
                    flag = 0
    
    print(f"#{tc} {dead_lock_cnt}")


