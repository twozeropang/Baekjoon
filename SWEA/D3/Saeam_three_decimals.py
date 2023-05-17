# 새샘이와 세 소수

# 정수론에서, 세 소수 문제란 다음과 같다.

# “5보다 큰 모든 홀수는 정확히 세 소수의 합으로 표현될 수 있다. (같은 소수를 합에 사용해도 된다.)”

# 예를 들어, 7 = 2 + 2 + 3, 11 = 2 + 2 + 7, 25 = 7 + 7 + 11로 나타낼 수 있다.

# 1939년 러시아 수학자 I. M. Vinogradov는 충분히 큰 홀수는 세 소수의 합으로 표현할 수 있다는 것을 증명했다.

# 여기서 충분히 크다는 것은 3315 ≈ 107000000 이상의 수라는 의미이다.

# 현재 가장 발전된 하한은 약 e3100 ≈ 101346 이상의 수이다.

# 러시아 수학자 I. M. Vinogradov 를 존경하는 새샘이는 직접 세 소수 문제를 풀어보기로 했다.

# 하지만 이 수는 너무 크기 때문에 컴퓨터로도 이 범위까지의 모든 수를 증명할 수는 없었다.

# 대신 어떤 크지 않은 홀수에 대해, 세 소수의 합으로 나타낼 수 있는 경우의 수를 구하기로 했다.

# 5보다 큰 홀수 N을 입력 받아 N = x + y + z (단, x ≤ y ≤ z 이고, x, y, z는 소수) 로 나타나는 경우의 수를 구하는 프로그램을 작성

# 하라.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에 하나의 정수 N ( 7 ≤ N ≤ 999 ) 이 주어진다.

# N은 홀수이다.


# [출력]

# 각 테스트 케이스마다 첫 번째 줄에는 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

# N을 세 소수의 합으로 나타낼 수 있는 경우의 수를 출력한다.

# 입력
# 3
# 7
# 11
# 25

# 출력
# #1 1
# #2 2
# #3 5

# 1. N에 대해서 N보다 작은 소수를 판단한다. (아리스토태네스의 채 이용)

# 2. 판단한 소수 리스트에서 세 합이 N이 되는 경우의 수를 cnt 한다. 

def find_primes(N):
    # 소수를 담을 리스트
    primes = []

    # 2부터 N까지 범위 내 
    for num in range(2, N+1):
        is_prime = True # 소수 확인용
        for i in range(2, int(num ** 0.5) + 1): # 2부터 해당 num의 제곱근의 범위까지
            if num % i == 0: # 나눠 진다는 것은 num이 i의 배수라는 의미이기 때문에 소수가 아니다. 탈락
                is_prime = False
                break # 다음 num을 찾는다.
        
        if is_prime: # 소수인 경우에만
            primes.append(num) # 그 수를 넣는다.
    
    return primes


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 소수 찾는 함수

    primes = find_primes(N)

    # 찾은 소수 리스트를 가지고 세 수의 합이 N과 같은 경우의 수 찾기
    cnt = 0 # 경우의 수

    # 같은 소수의 경우도 합으로 사용할 수 있다는 조건이 문제에 있기 때문에 인덱스의 +1 하지 않는다.
    # 3중 반복문으로 확인
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            for k in range(j, len(primes)):
                if primes[i] + primes[j] + primes[k] == N:
                    cnt += 1
    
    print(f"#{tc} {cnt}")
