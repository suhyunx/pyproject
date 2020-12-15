score=list(map(int,input("input: ").split())) 
counter = 0

for passnot in score: 
    counter = counter +1 
    if passnot >= 60: 
        print("{}번 학생은 합격입니다.".format(counter))
    else: 
        print("{}번 학생은 불합격입니다.".format(counter))
