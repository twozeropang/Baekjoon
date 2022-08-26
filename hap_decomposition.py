# 백준 2225번 합분해 

# 덧셈의 순서가 바뀌는 경우 - 다른 경우
# 한 개의 수를 여러 번 사용 가능 
# dp = K개로 만들수 있는 N의 경우의 수 

n, k = map(int, input().split())

# 문제에서 범위가 200으로 주어졌기 때문에 각각 배열 생성
dp = [[0]*201 for i in range(201)]

# dp[k][n] -> dp[1][n]이라면 1개의 수로만 표현 할 수 있기 때문에 1부터 200까지의 수를 표현할 때 무조건 1
# dp[k][n] -> dp[2][n]이라면 2개의 수로 표현 할 수 있다. 
# ex) dp[2][3] = (2, 1), (1, 2), (3, 0) , (0, 3) -> 4 = k가 2일때 n + 1 
# ex) dp[2][4] = (0, 4), (4, 0), (1, 3), (3, 1), (2, 2) -> 5 = k가 2일 때 n + 1
# 따라서 아래에 공식을 적용하여 초기화 
for i in range(201):    
    dp[1][i] = 1
    dp[2][i] = i + 1


for i in range(2, 201):
    # dp[2][1] ~ dp[200][1] = 1의 합 경우의 수가 결국 i 자기 자신 
    # dp[2][1] = (0,1), (1,0) 2가지, dp[3][1] = (0,0,1) , (0,1,0), (1,0,0) 3가지....
    dp[i][1] = i
    for j in range(2, 201):
        # dp[2][2] = dp[2][1] + dp[1][1] -> 3 = 2 + 1 
        dp[i][j] = (dp[i][j-1]+dp[i-1][j])% 1000000000

print(dp[k][n])
