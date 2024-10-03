a = int(input())
words = list(input().split())
line = []
for word in words:
    if len(' '.join(line + [word]).strip()) > 80:
        print(' '.join(line).strip())
        line = [word]
    else:
        line.append(word)
if line:
    print(' '.join(line).strip())
