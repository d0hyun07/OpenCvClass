def login(msg, times =3, warn='wrong ID'):
  while True:
    id = input(msg)
    if id in ('user', 'User', 'USER'):
      return True
    times = times -1
    if times < 0:
      print('time out')
      return False
    print(warn)


#각 줄은 무슨 차이가 있을까?
login('#1 : ID를 입력하세요')
# login('#2 : ID를 입력하세요', 2)
# login('#3 : ID를 입력하세요', 2, '다시 도전하세요!!!')