# 백준 2875번 대회 or 인턴 

"""
- 한 팀을 만드는 조건 
    여학생 2명 이상, 남학생 1명 이상 = M+N >= K+3 (팀은 3명이고, 인턴은 K명이 하기 때문)
"""

n, m, k = map(int, input().split())

# 팀 구성 수 
result = 0

# 2명과 1명으로 팀을 구성하고, 인턴쉽도 보내는 것이 가능한 수 일 때 
while n >= 2 and m >= 1 and n + m >= k + 3: 
    n -= 2 # 빼주고
    m -= 1 # 빼준다.
    result += 1 # 팀 수는 하나씩 더해준다. 
    
print(result)