# 九九乘法表
# 再開一個對比 range(開始的數字,總共幾個數字)
for i in range(1,10):
  for j in range(1,10):
    print(i, 'x', j, '=', i*j, sep='', end=' ') #sep='' 預設有間隔，改不空格 end=' '結尾預設空格
  print() #換行