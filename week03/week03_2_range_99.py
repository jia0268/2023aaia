# 九九乘法表,有個問題,是數字從0開始到小於9,沒關係先寫
for i in range(9):
  for j in range(9):
    print(i, 'x', j, sep='', end=' ') #sep='' 預設有間隔，改不空格 end=' '結尾預設空格
  print() #換行