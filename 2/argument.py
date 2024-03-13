# *argument는 가변인자 : 별 한개면 리스트
# **argument는 키워드인자 : 별 두개면 딕셔너리

def caffe(beverage, *arguments, **keywords):
  print("Do U have any", beverage, "?")
  for arg in arguments:
    print(arg)
  print("*****")
  for kw in keywords:
    print(kw, ":", keywords[kw])

caffe("coffee", "it's yummy, sir.", "Would you try?",
        barista = "Jay Kime",
        client = "BSSM",
        cup = "Venti-size")