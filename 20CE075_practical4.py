# 20CE075 PARTH PARMAR
# Practical 4 Find runner-up from given list
# GitHub link

n = int(input())
scoreList = map(int, input().split())
scoreList = sorted(scoreList)
res = max(scoreList)
scoreList = [i for i in scoreList if i != res]
res = max(scoreList)
print(res)
