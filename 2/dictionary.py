import os
os.system('clear')

nation = {'Korea':"+82", 'US':"+1", 'Japan':"+81"}

print(nation['Korean'])

var = input()

#if('US' in nation):
if(var in nation):
  print('country code =', nation['US'])
else:
  print('something wrong~~~!!!')