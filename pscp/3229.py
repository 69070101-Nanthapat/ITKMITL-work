"""Online game score"""
score = int(input())
bonus = int(input())
day = int(input())
ranking = 0
special_rank = 0

total_score = score + bonus
if day > 3:
    total_score = total_score * 1.5

if total_score >= 1500:
    ranking = 5
elif total_score >= 1000:
    ranking = 4
elif total_score >= 500:
    ranking = 3
elif total_score >= 200:
    ranking = 2
elif total_score < 200:
    ranking = 1

if ranking == 5 and day >= 7:
    special_rank = 99
elif ranking == 4 and bonus > 300:
    special_rank = 88

print(int(total_score))
print(ranking)
print(special_rank)
