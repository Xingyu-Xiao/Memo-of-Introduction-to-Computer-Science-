boy_number = int(input())
boy_skills = list(map(int, input().split()))
girl_number = int(input())
girl_skills = list(map(int, input().split()))
boy_skills.sort()
girl_skills.sort()
num = 0
i = j = 0
while i < boy_number and j < girl_number:
    if abs(boy_skills[i] - girl_skills[j]) <= 1:
        num += 1
        i += 1
        j += 1
    elif boy_skills[i] < girl_skills[j]:
        i += 1
    elif boy_skills[i] > girl_skills[j]:
        j += 1
print(num)
