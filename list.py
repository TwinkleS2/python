#-*- coding: utf-8 -*-

while 1:

	money=input("돈을 넣어주세요")

	number=input("음료를 골라주세요\n")

	temp=money

	if number==1:

		#포도주스 100원

		print "포도주스를 선택하셨습니다. 거스름돈은 ",money-100,"원 입니다"

		money=temp-100

		if money<=0:

			break

	elif number==2:

		#오렌지주스 200원

		print "포도주스를 선택하셨습니다. 거스름돈은 ",money-200,"원 입니다"

		money=temp-200

		if money<=0:

			break

	elif number==3:

		#환타 300원

		print ("포도주스를 선택하셨습니다. 거스름돈은 ",money-300,"원 입니다")

		money=temp-300

		if money<=0:

			break

	else:

		#없는 번호

		print "없는 번호입니다. 다시 입력해주세요"