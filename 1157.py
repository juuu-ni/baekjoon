"""
ord('a') = 97
ord('A') = 65
대소 구분 없음 -> .upper()로 접근
"""

word = input().upper().strip()
cnt = [0] * 26

for ch in word:
    cnt[ord(ch)-ord('A')] += 1

max_count = max(cnt)
if cnt.count(max_count) == 1:
    print(chr(cnt.index(max_count)+ord('A')))
else:
    print('?')
