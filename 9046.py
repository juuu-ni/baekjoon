T = int(input())

for _ in range(T):
    s = input()
    count = [0] * 26  # 알파벳 26개

    for ch in s:
        if ch != ' ':  # 공백 제외
            count[ord(ch) - ord('a')] += 1  # 'a' = 0번, 'b' = 1번 

    max_count = max(count)  # 가장 많이 나온 횟수
    if count.count(max_count) > 1:
        print('?')  # 여러 개면 물음표
    else:
        max_index = count.index(max_count)  # 가장 많이 나온 알파벳의 인덱스
        print(chr(max_index + ord('a')))  # 인덱스 -> 문자로 바꾸기
