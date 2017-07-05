n = 5
while True:
 x = input("숫자를 입력하세요")
 g = int(x)
 if g > n:
  print("숫자가 너무 커요")
 if g < n:
  print("숫자가 너무 작아요")
  if g == n:
  print("딩동댕")
break