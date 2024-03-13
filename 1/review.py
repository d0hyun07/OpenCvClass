width = 3
height = 5
RectArea = width * height
TriangleArea = width+height/2

print(RectArea)
print(width, '*', height, '=', RectArea)

#중괄호 {}를이용해서 format method를 이용해 출력
print('{0} : {1} * {2}/2 = {3}'.format('Triangle Area',width, height, TriangleArea))

strings = 'it is string'

#문자열 표현 방법-1
print(strings)
print('{0}'.format('it\'s string2'))

#문자열 표현 방법-2
strings = "double and single quotation marks have the same result"
print(strings)

#문자열 표현 방법-3
strings = 'Busan city'
print(strings[0], strings[2])
print(strings[-1], strings[-2], strings[-3])
print(strings[0:5] + strings[-4:1] + strings[-1]) # 특정 구간 표현
print()


