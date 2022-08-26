# 백준 1912번 연속합 

T = int(input())
Arr = list(map(int, input().split()))

# 1부터 시작해주지 않으면 dp에서 이전 인덱스를 참조하여 구현할 때 0 - 1번째 즉 -1 번째 인덱스를 참조해야하기 때문에 오류 발생
for i in range(1, T):
    Arr[i] = max(Arr[i], Arr[i-1] + Arr[i]) 
print(max(Arr))

# 예제 입력 2
# 10
# 2 1 -4 3 4 -4 6 5 -5 1

# for문 돌면서 
# 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
# 2 | 1 |-4 | 3 | 4 |-4 | 6 | 5 |-5 | 1 -> Arr[i] = max(Arr[i], Arr[i-1] + Arr[i])
#   | 3 |-1 | 3 | 7 | 3 | 9 | 14| 9 | 10 -> 이중에서 max함수를 다시 입력하면 두번째 줄 출력 값이 나온다. 