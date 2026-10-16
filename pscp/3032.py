"""score"""
amout = int(input())
score = []
count = 0
for i in range(amout):
    student_score = int(input())
    score.append(student_score)

max_score = max(score)
for i in range(amout):
    if score[i] == max_score:
        count += 1
print(max_score)
print(count)
