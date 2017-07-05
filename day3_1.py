
while 1:
    money=input("돈을 넣어주세요")
    number=input("음료를 골라주세요\n")
    temp=money
    if number==1:
        print ("포도주스를 선택하셨습니다. 거스름돈은",money-100,"원 입니다")1
        money=temp-100
        if money<=0:
                break