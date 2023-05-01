# 단순 2진 암호 코드

# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

# 어떤 국가에서는 자국 내 방송국에서 스파이가 활동하는 사실을 알아냈다. 스파이는 영상물에 암호 코드를 삽입하여 송출하고 있었다. 스파이의 암호 코드에 다음과 같은 규칙이 있음을 발견했다.
 

# 1. 암호코드는 8개의 숫자로 이루어져 있다.

# 2. 올바른 암호코드는 (홀수 자리의 합 x 3) + (짝수 자리의 합)이 10의 배수가 되어야 한다.

#     ex) 암호코드가 88012346일 경우,
#     ( ( 8 + 0 + 2 + 4 ) x 3 ) + ( 8 + 1 + 3 + 6) = 60은 10의 배수이므로 올바른 암호코드다.

#     ex) 암호코드가 19960409일 경우,
#     ( ( 1 + 9 + 0 + 0 ) x 3 ) + ( 9 + 6 + 4 + 9) = 58은 10의 배수가 아니므로 잘못된 암호코드다. 
 
# 이 암호코드들을 빠르고 정확하게 인식할 수 있는 스캐너를 개발하려고 한다.

# 스캐너는 암호코드 1개가 포함된 직사각형 배열을 읽는다.

# 직사각형 배열은 1, 0으로만 이루어져 있고, 암호코드 이외의 부분은 전부 0으로 주어진다.

# 암호코드에서 숫자 하나는 7개의 비트로 암호화되어 주어진다. 따라서 암호코드의 가로 길이는 56이다. 
 
# 암호코드의 각 숫자가 암호화되는 규칙은 다음과 같다.

# 비정상적인 암호코드(가로 길이가 56이 아닌 경우, 아래 규칙대로 해독할 수 없는 경우)는 주어지지 않는다.
 


# 암호코드 정보가 포함된 2차원 배열을 입력으로 받아 올바른 암호코드인지 판별하는 프로그램을 작성하라.

# [입력]

# 가장 첫줄은 전체 테스트 케이스의 수이다.

# 각 테스트 케이스의 첫 줄에 두 자연수가 주어지는데 각각 배열의 세로 크기 N, 배열의 가로크기 M이다 (1≤N≤50, 56≤M≤100).

# 그 다음 N개의 줄에 걸쳐 N x M 크기의 직사각형 배열이 주어진다.

# [출력]

# 각 테스트 케이스의 답을 순서대로 표준출력으로 출력하며, 각 케이스마다 줄의 시작에 “#C”를 출력하여야 한다. 이때 C는 케이스의 번호이다.

# 주어진 암호코드가 올바른 암호코드일 경우, 암호코드에 포함된 숫자의 합을 출력하라. 만약 잘못된 암호코드일 경우 대신 0을 출력하라.

# [예제 풀이]

# 1번 케이스의 암호코드 정보를 추출하면 아래와 같다.

# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
 
# 이 숫자가 나타내는 정보는 각각 아래와 같다.
# 0111011(7) 0110001(5) 0111011(7) 0110001(5) 0110001(5) 0001101(0) 0010011(2) 0111011(7)
 
# 검증코드가 맞는지 살펴보면, (7 + 7 + 5 + 2) * 3 + 5 + 5 + 0 + 7 = 80 이므로 올바른 암호코드라고 할 수 있다. 따라서 1번의 출력 값은 38이 된다.
 
# 2번 케이스도 같은 방식으로 계산할 경우, 잘못된 암호코드임을 알 수 있다. 따라서 2번의 출력 값은 0이 된다.

# 입력
# 2
# 16 80
# 00000000000000000000000000000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000000000000000000000000000
# 00000000000000011101101100010111011011000101100010001101001001101110110000000000
# 00000000000000011101101100010111011011000101100010001101001001101110110000000000
# 00000000000000011101101100010111011011000101100010001101001001101110110000000000
# 00000000000000011101101100010111011011000101100010001101001001101110110000000000
# 00000000000000011101101100010111011011000101100010001101001001101110110000000000
# 00000000000000011101101100010111011011000101100010001101001001101110110000000000
# 00000000000000011101101100010111011011000101100010001101001001101110110000000000
# 00000000000000000000000000000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000000000000000000000000000
# 11 70
# 00000000000000000000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000000000000000000
# 00000001100101000110100011010111101101110010011001001101110110000000000
# 00000001100101000110100011010111101101110010011001001101110110000000000
# 00000001100101000110100011010111101101110010011001001101110110000000000
# 00000001100101000110100011010111101101110010011001001101110110000000000
# 00000001100101000110100011010111101101110010011001001101110110000000000
# 00000001100101000110100011010111101101110010011001001101110110000000000
# 00000000000000000000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000000000000000000

# 출력
# #1 38
# #2 0

# 해당 암호숫자의 시작 지점까지 빠르게 탐색하는 함수
def find_idx(word):
    for i in range(n):
        # 앞에서부터 탐색할 경우 비효율적으로 탐색하므로 뒤에서부터 1 포함 여부 확인
        for j in range(m-1, 0, -1):
            if pass_info[i][j]: # 이중 for문을 돌면서 1이 포함된 경우
                line = i
                idx = j
                return line, idx
        
# 암호 패턴 반환 함수
def change(password):

    pass_pattern = {
        '0001101' : '0',
        '0011001' : '1',
        '0010011' : '2',
        '0111101' : '3',
        '0100011' : '4',
        '0110001' : '5', 
        '0101111' : '6',
        '0111011' : '7',
        '0110111' : '8', 
        '0001011' : '9'
    }
    return pass_pattern[password]
    

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())

    pass_info = [list(map(int, input())) for _ in range(n)]
    
    # 더욱 빠르게 코드 값을 찾기 위해서 0이 아닌 라인과 인덱스를 구하는 함수 생성

    line = find_idx(pass_info)[0] # 0이 아닌 행 반환

    idx = find_idx(pass_info)[1] # 1이 시작되는 인덱스 반환

    password = pass_info[line][idx-55:idx+1] # 암호화 가로 길이인 56만큼만 slicing

    # 해당 암호 패턴 확인

    # 해독 후 결과 넣을 변수
    answer = ''

    # 암호코드는 7자리기 때문에 7단위로 반복문 실행 
    for i in range(0, len(password), 7):
        tmp = ''
        for j in range(i, i+7):
            tmp += str(password[j]) # 돌면서 7자리씩 0과 1을 넣는다.
        
        answer += change(tmp) # 해당 코드 패턴을 확인해서 answer에 넣는다. 

    # 홀수 짝수 구분

    odd_num = 0
    even_num = 0

    for i in range(7):
        # 인덱스 홀수
        if i % 2:
            even_num += int(answer[i])
        else:
            odd_num += int(answer[i])
    
    # 식 적용 (마지막에 검증 코드 추가)
    check = odd_num * 3 + even_num + int(answer[7])

    # 10의 배수 아닌경우
    if check % 10:
        total = 0
    # 10의 배수인 경우
    else:
        total = 0
        for i in range(8):
            total += int(answer[i])
    
    print(f"#{tc} {total}")
    
    






    
