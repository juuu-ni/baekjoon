mo = {'a', 'e', 'i', 'o', 'u'}

def is_acceptable(pw):
   
    if not any(ch in mo for ch in pw):
        return False

    for i in range(len(pw) - 2):
        if (pw[i] in mo and pw[i+1] in mo and pw[i+2] in mo) or \
           (pw[i] not in mo and pw[i+1] not in mo and pw[i+2] not in mo):
            return False

    
    for i in range(len(pw) - 1):
        if pw[i] == pw[i+1] and pw[i:i+2] not in ('ee', 'oo'):
            return False

    return True


while True:
    pw = input().strip()
    if pw == 'end':
        break

    if is_acceptable(pw):
        print(f"<{pw}> is acceptable.")
    else:
        print(f"<{pw}> is not acceptable.")
