menu="""
메뉴
1. 아메리카노: 2500원
2. 카페라떼: 3000원
3. 화이트모카라뗴: 4000원
4. 햄치즈샌드위치: 6000원
5. 음식주문
"""
print(menu)
total=0
while True:
    num=int(input("원하시는 메뉴번호를 입력하세요: "))
    if num==1:
        print("  아메리카노를 주문하셨습니다")
        total+=2500 #total=total+2500
    elif num==2:
        print("  카페라떼를 주문하셨습니다")
        total+=3000
    elif num==3:
        print("  화이트모카라떼를 주문하셨습니다")
        total+=4000
    elif num==4:
        print("  햄치즈샌드위치를 주문하셨습니다")
        total+=6000
    elif num==5:
        print("총 주문하신 금액은 {}입니다".format(total))
        print(" 감사합니다. 기다리시면 곧 나옵니다")
        break
    else:
        print("잘못된 주문입니다.")
