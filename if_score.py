score=int(input("your score: "))

if (score>=90):
    grade="A"
elif (score>=80):
    grade="B"
elif (score>=70):
    grade="C"
elif (score>=60):
    grade="D"
else:
    grade="F"

print("당신의 점수는 {}이고 {} 입니다".format(score,score))
print("당신의 점수는",score,"이고",score,"입니다")
print("당신의 등급은 {} 입니다".format(grade))
print("당신의 점수는 %d 입니다." % score)
